# MotionSensorApp
A Motion Sensor iOS App using Python and AWS Python SDKs on a Raspberry Pi.

## Sensor.py
The Python script responsible in invoking an AWS Lambda function which then sends a remote notification to an iOS App.
The invokation occurs when the Infrared Motion Sensor from the Raspberry Pi Kit made by [Freenove](https://www.freenove.com/index.html) senses motion.

## AWS Lambda
To make your AWS Lambda function, you can follow this [tutorial made by Pusher Beams](https://pusher.com/tutorials/push-notifications-ios-python-aws-lambda/) or this [tutorial](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html) straight from the Amazon AWS Documentation website. I would say both are worth looking at to understand AWS Lambda better.

## Connecting Python script to AWS Lambda
In ```Sensor.py``` make sure that the ```client.invoke()``` function has your correct AWS Lambda function name. When running the script, you will be able to see your invokation in your AWS console.
