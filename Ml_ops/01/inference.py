from timm.models import create_model
import requests
from PIL import Image
import torchvision.transforms as transforms
import torch
import json

import hydra
from omegaconf import DictConfig
import logging
import json
import io


@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg: DictConfig):
    # print(cfg)
    model = create_model(cfg.model , pretrained=True)
    model.eval()

    response = requests.get(cfg.image).content
    img = Image.open(io.BytesIO(response))

    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        normalize,
    ])

    img = transform(img)
    img = img.unsqueeze(0)

    with torch.no_grad():
        pred = model(img)
        probs = torch.nn.functional.softmax(pred, dim=1)
        con_sco, classes = torch.max(probs, 1)


    idx2label = []
    cls2lablel = {}

    with open("imagenet_class_index.json",'r') as jsonfile:
        class_idx = json.load(jsonfile)
        # print(class_idx)
        idx2label = [class_idx[str(k)][1] for k in range(len(class_idx))]
        cls2lablel = {class_idx[str(k)][0]: class_idx[str(k)][1]
                    for k in range(len(class_idx))}

    out_dict = {}
    out_dict['predicted'] = str(idx2label[classes.cpu().numpy()[0]])
    out_dict['confidence'] = float(con_sco.cpu().numpy()[0] *100)

    json_object = json.dumps(out_dict, indent=4)
    print(json_object)

if __name__ == '__main__':
    logging.disable(logging.CRITICAL)
    main()

