# MotionSensorApp
A Motion Sensor iOS App using Python and AWS Python SDKs on a Raspberry Pi.

## SenseLED.py
The Python script responsible in invoking an AWS Lambda function which then sends a remote notification to an iOS App.
The invokation occurs when the Infrared Motion Sensor from the Raspberry Pi Freenove Kit made by [Freenove](https://www.freenove.com/index.html) senses motion.
