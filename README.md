# Serial Communication and Firmware Extraction
This repo is about developing individual skills in the following topics:
* Serial communication & hardware
* Firmware & software comparison
* Firmware extraction from some common devices
* Machine learning, data processing, and signals
* Machine learning & some applications towards security (ML outside of raw sensor data)
* Wireless communication and modulation

This will be done across three different projects.

## Table of Contents
* [Project 1: Interfacing with Serial](#project-1-interfacing-with-serial)
* [Short Background](#short-background-1)
* [Build of Materials](#build-of-materials-1)
* [Media](#media-1)
* [Experimental Process](#experimental-process-1)
* [Results](#results-1)
* [Discussion](#discussion-1)
----------------------------------------------------
* [Project 2: Programming Arduino with TTL Cable](#project-2-programming-arduino-with-ttl-cable)
* [Short Background](#short-background-2)
* [Build of Materials](#build-of-materials-2)
* [Media](#media-2)
* [Experimental Process](#experimental-process-2)
* [Results](#results-2)
* [Discussion](#discussion-2)
----------------------------------------------------
* [Project 3: Arduino as programmer/debug board with Arduino ISP](#project-3-arduino-as-programmerdebug-board-with-arduino-isp)
* [Short Background](#short-background-3)
* [Build of Materials](#build-of-materials-3)
* [Media](#media-3)
* [Experimental Process](#experimental-process-3)
* [Results](#results-3)
* [Discussion](#discussion-3)
----------------------------------------------------
* [Citations and References](#citations-and-references)


## Project 1: Interfacing with Serial
This project's about serial interfacing with hardware serial, software serial, and a TTL cable using a basic Arduino Uno kit. We will setup and run a software serial script. 

### Short Background (1)
Hardware Serial is a wired communication that can transmit and receive at the same time, work while the Arduino is performing other tasks (via UART-to-USB adapter chip), and handle fast baud rates [https://www.martyncurrey.com/arduino-serial-a-look-at-the-different-serial-libraries/#:~:text=Using%20AltSoftSerial%20Sketch-,Hardware%20Serial,serial%20monitor%20when%20using%20usb.].

Software Serial uses serial communication on digital pins of a physical board and software to replicate functionality of hardware serial. Unlike Hardware Serial, multiple software serial ports are possible [https://docs.arduino.cc/learn/built-in-libraries/software-serial/]. It is slightly more unreliable at very slow or very fast speeds due to its problems with timing. 

TTL Cables are wires used for microcontrollers, embedded systems, or DIY electronics. They allow the computer to communicate with devices that use Transistor-Transistor Logic (TTL) signals that are digital and have specific voltages [https://www.romtronic.com/what-is-a-usb-to-ttl-serial-cable/]. A logic 0 is usually 0 V while a logic 1 can be 3.3 V or 5 V.

### Build of Materials (1)
* Arduino Uno Board
* USB-B Data Cable
* TTL Cable
* Laptop/Desktop with Arduino IDE

### Media (1)

### Experimental Process (1)

### Results (1)

### Discussion (1)

----------------------------------------------------
## Project 2: Programming Arduino with TTL Cable
Introduction

### Short Background (2)

### Build of Materials (2)

### Media (2)

### Experimental Process (2)

### Results (2)

### Discussion (2)

----------------------------------------------------
## Project 3: Arduino as programmer/debug board with Arduino ISP
Introduction

### Short Background (3)

### Build of Materials (3)

### Media (3)

### Experimental Process (3)

### Results (3)

### Discussion (3)

----------------------------------------------------
## Citations and References
[1] Test