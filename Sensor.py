#!/usr/bin/env python3
# -------------------------------------------------
# Ernani Raffo
# Sensor.py
# Program that sends a notification to an iOS app
# from a Raspberry Pi using AWS Lambda when motion
# is detected.
# -------------------------------------------------

import boto3  # AWS Python SDK
import RPi.GPIO as GPIO

ledPin = 11       # define ledPin
sensorPin = 18    # define sensorPin

client = boto3.client("lambda")


def setup():
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)    # set ledPin to OUTPUT mode
    GPIO.setup(sensorPin, GPIO.IN)  # set sensorPin to INPUT mode


def loop():
    while True:
        if GPIO.input(sensorPin) == GPIO.HIGH:
            GPIO.output(ledPin, GPIO.LOW)  # turn off led
            print('led turned off >>>')
            client.invoke(
                    FunctionName='your-function-name',
                    Payload='{"title": "ALERT", "message": "Motion detected at front door!"}'
                    )
        else:
            GPIO.output(ledPin, GPIO.HIGH)  # turn on led
            print('led turned on <<<')


def destroy():
    GPIO.cleanup()                     # Release GPIO resource


if __name__ == '__main__':     # Program entrance
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
