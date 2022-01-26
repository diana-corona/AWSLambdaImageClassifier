# Photo Classificartion Api
API to upload, download, and classify photos from s3

### To deploy 
1. Run 'serverless deploy' to upload the lambda function to aws

### Endpoints
## /classify-image
1. Classify images uploaded to s3 using ResNet50 (ImageNet) pretrained neural network.

## /upload-image
1. Upload image to s3, creates unique names each time

## /Download-image
1. Download image from s3
