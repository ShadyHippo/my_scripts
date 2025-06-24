#!/bin/bash

echo "sudo apt update"
echo "sudo apt upgrade -y"
echo "sudo apt install python3-gpiozero"


echo "run sudo raspi-config"
echo "navigate to Interface Options"
echo "  -> Enable SPI"
echo "  -> Enable I2C"
echo "reboot afterward"
