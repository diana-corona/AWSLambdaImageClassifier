# Photo Classificartion Api
Image classification API that uploads, downloads and classify images from s3 using ResNet50 (ImageNet) pretrained neural network.

### To deploy 
1. Run 'serverless deploy' to upload the lambda function to aws

### Endpoints
## /classify-image
1. Classify images uploaded to s3 using ResNet50 (ImageNet) pretrained neural network.

## /upload-image
1. Upload image to s3, creates unique names each time

## /download-image
1. Download image from s3 repository

## /delete-image
1. Delete image from s3 repository