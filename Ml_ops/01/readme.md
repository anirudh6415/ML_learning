# Simple Docker Repository for Image Inference with Timm Library

This repository provides a simple Docker setup for making inferences on an image using the Timm library.

## How to Use this Repository

1. **Install Docker:**
   - Before using this repository, ensure that [Docker](https://docs.docker.com/engine/install/) is installed on your system.

2. **Build the Docker Image:**
   - Open a terminal and navigate to the repository directory.
   - Run the following command to build the Docker image:
     ```bash
     docker build --tag timm_inference:latest .
     ```

3. **Run the Docker Container:**
   - After successfully building the Docker image, run the following command to execute the Docker container:
     ```bash
     docker run -it timm_inference:latest model=$model_name image=$image_link
     ```
     Replace `$model_name` with the desired model name and `$image_link` with the link to the image you want to perform inference on.

## Example Usage

```bash
docker run -it timm_inference:latest model=resnet50 image=https://example.com/image.jpg
```


This Markdown format provides clear instructions on how to use the Docker repository for image inference with the Timm library. Replace placeholder values like `$model_name` and `$image_link` with your specific model name and image link.
