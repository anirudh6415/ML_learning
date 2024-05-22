<div align="center">
# Generated from the [![template](https://img.shields.io/badge/template-lightning--hydra--template-blue?logo=github)](https://github.com/ashleve/lightning-hydra-template)

I have added the Dockerfile to the project, making it more portable and easier to deploy. Docker allows you to containerize your application, ensuring that it runs consistently across different environments. By using Docker, you can encapsulate all dependencies and configurations within a container, facilitating smoother development workflows and simplified deployment processes.

The original repository did not include a Dockerfile. I have made enhancements to the source files and implemented Docker to enhance the project's portability and deployment capabilities.
</div>

## How to run

Train model with default configuration

```bash
cd docker_for_cifar10/
make build
docker image ls 
docker run -it -v `pwd`:/workspace/project/ {DOCKER IMAGE_NAME}  bash
```
To train the model on CIFAR10 dataset
```bash
Python src/train.py
```
To validate the model

```bash 
python src/eval.py
```

Feel free to adjust the instructions as needed for your specific project and Docker setup.

---------------------------------------------------------------------------
<div align="center">
# Lightning-Hydra-Template

[![python](https://img.shields.io/badge/-Python_3.8_%7C_3.9_%7C_3.10-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pytorch](https://img.shields.io/badge/PyTorch_2.0+-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)
[![lightning](https://img.shields.io/badge/-Lightning_2.0+-792ee5?logo=pytorchlightning&logoColor=white)](https://pytorchlightning.ai/)
[![hydra](https://img.shields.io/badge/Config-Hydra_1.3-89b8cd)](https://hydra.cc/)
[![black](https://img.shields.io/badge/Code%20Style-Black-black.svg?labelColor=gray)](https://black.readthedocs.io/en/stable/)
[![isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) <br>
[![tests](https://github.com/ashleve/lightning-hydra-template/actions/workflows/test.yml/badge.svg)](https://github.com/ashleve/lightning-hydra-template/actions/workflows/test.yml)
[![code-quality](https://github.com/ashleve/lightning-hydra-template/actions/workflows/code-quality-main.yaml/badge.svg)](https://github.com/ashleve/lightning-hydra-template/actions/workflows/code-quality-main.yaml)
[![codecov](https://codecov.io/gh/ashleve/lightning-hydra-template/branch/main/graph/badge.svg)](https://codecov.io/gh/ashleve/lightning-hydra-template) <br>
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/ashleve/lightning-hydra-template#license)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/ashleve/lightning-hydra-template/pulls)
[![contributors](https://img.shields.io/github/contributors/ashleve/lightning-hydra-template.svg)](https://github.com/ashleve/lightning-hydra-template/graphs/contributors)

A clean template to kickstart your deep learning project 🚀⚡🔥<br>
Click on [<kbd>Use this template</kbd>](https://github.com/ashleve/lightning-hydra-template/generate) to initialize new repository.

_Suggestions are always welcome!_

</div>


