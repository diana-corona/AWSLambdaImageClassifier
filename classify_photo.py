import json
import boto3
import numpy as np
import PIL.Image as Image

import tensorflow as tf
import tensorflow_hub as hub

IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224

IMAGE_SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT)
model = tf.keras.Sequential([hub.KerasLayer("model/")])
model.build([None, IMAGE_WIDTH, IMAGE_HEIGHT, 3])

imagenet_labels= np.array(open("model/ImageNetLabels.txt").read().splitlines())
s3 = boto3.resource("s3")

def readImageFromBucket(image_key, bucket_name):
  bucket = s3.Bucket(bucket_name)
  object = bucket.Object(image_key)
  response = object.get()
  return Image.open(response["Body"])

def lambda_handler(event, context):

  bucket_name = event["queryStringParameters"]["bucket_name"]
  image_key = event["queryStringParameters"]["image_key"]

  img = readImageFromBucket(image_key, bucket_name).resize(IMAGE_SHAPE)
  img = np.array(img)/255.0

  prediction = model.predict(img[np.newaxis, ...])
  predicted_class = imagenet_labels[np.argmax(prediction[0], axis=-1)]

  print("ImageName: {0}, Prediction: {1}".format(image_key, predicted_class))
  
  image_classification =  {
    "bucket_name": bucket_name,
    "image_key":   image_key,
    "prediction":   predicted_class
  }
  return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(image_classification),
    }
