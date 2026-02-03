# Serial Communication and Firmware Extraction
This repo is about developing individual skills in the following topics:
* Serial communication & hardware
* Firmware & software comparison
* Firmware extraction from some common devices
* Machine learning, data processing, and signals
* Machine learning & some applications towards security (ML outside of raw sensor data)
* Wireless communication and modulation

This will be done across three different projects. The repository is made by Anthony Nguyen.

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
Hardware Serial is a wired communication that can transmit and receive at the same time, work while the Arduino is performing other tasks (via UART-to-USB adapter chip), and handle fast baud rates [4].

Software Serial uses serial communication on digital pins of a physical board and software to replicate functionality of hardware serial. Unlike Hardware Serial, multiple software serial ports are possible [1]. It is slightly more unreliable at very slow or very fast speeds due to its problems with timing. 

TTL Cables are wires used for microcontrollers, embedded systems, or DIY electronics. They allow the computer to communicate with devices that use Transistor-Transistor Logic (TTL) signals that are digital and have specific voltages [9]. A logic 0 is usually 0 V while a logic 1 can be 3.3 V or 5 V.

### Build of Materials (1)
* Arduino Uno Board
* USB-B Data Cable
* TTL Cable
* Laptop/Desktop with Arduino IDE

### Media (1)

![alt text](/media/SerialMonitorTest_ArduinoUno/SerialMonitorConnection.jpg)
This figure showcases the USB-B connection to the Arduino Uno board. It also showcases the SoftwareSerial connection using a TTL cable as shown in the TTL Cable Specs sheet below. The connection goes Black-Red for GND, White-Red in Digital Pin 3 for TX, and Green-Orange in Digital Pin 2 for RX. This is based on the code given in [serialMonitorTest.ino](/src/SerialMonitorTest_ArduinoUno/serialMonitorTest.ino).

### Experimental Process (1)
1. Connect USB-B wire to Arduino Uno and Computer Port
2. Connect TTL cable using jumper cables into Arduino Ports and ground.
3. Upload [serialMonitorTest.ino](/src/SerialMonitorTest_ArduinoUno/serialMonitorTest.ino) into the Arduino with COM3 selected in Arduino IDE under Tools -> Port.
4. When the code is done uploading, hit the white or blue button on the Arduino Board within a second.
5. Look at Serial Monitor and select 9600 Baud rate if not already selected.

### Results (1)

The result of the serial upload should be seen like below.

![alt text](/media/SerialMonitorTest_ArduinoUno/SerialMonitorTestOutput1.PNG)

This showcases a successful data upload onto the Arduino via USB-B.

### Discussion (1)

Despite opening a new sketch window and selecting the relevant COM port for Serial Monitor, Arduino IDE 2.3.7 does not support dual Serial Monitoring. This is explored and fixed in Part 2 with [twoCOM.py](/src/SerialMonitorTest_ArduinoUno/twoCOM.py).

----------------------------------------------------
## Project 2: Programming Arduino with TTL Cable
This section involves programming an Arduino with a TTL cable and reading out with Python.

### Short Background (2)
Firmware is code that's embedded within a hardware device to help it function. It is also known as "software for hardware." Firmware delivers instructions for how the hardware device should start, interact with other devices, and execute I/O tasks.

Software is a set of instructions that guide the core operations of a computing device [5].

Hardware is the physical component of a computer that a computer cannot function without. It provides the physical resources required for a computer to function.

Operating System is the system software that runs on the computer and manages all application programs to provide an interface between the user and hardware [6].

Serial Port allows a physical device to send and receive bytes of information in a serial manner with one bit at a time in either a binary format or a text (ASCII) format. Communication is established through the serial port [8].

Serial Data Stream helps receive and process a continuous data stream from a device connected to a USB or serial port rather than simultaneous parallel communication [7].

Reverse Engineering is the process of taking something apart to discover how it works. It normally includes disassembling a complete product and analyzing each component to see how they work together [3].

Boot Loader is a piece of firmware that allows a piece of software to be uploaded onto microcontrollers [2].

### Build of Materials (2)
* Arduino Uno Board
* USB-B Data Cable
* TTL Cable
* Laptop/Desktop with Arduino IDE

### Media (2)

This figure shows the output read from [readCOM.py](/src/SerialMonitorTest_ArduinoUno/readCOM.py) when connected to COM3.

![alt text](/media/SerialMonitorTest_ArduinoUno/readCOM_output.PNG)

This figure shows the output read from [loopCOM.py](/src/SerialMonitorTest_ArduinoUno/loopCOM.py).

![alt text](/media/SerialMonitorTest_ArduinoUno/loopCOM_output.PNG)

This figure shows the output read from [twoCOM.py](/src/SerialMonitorTest_ArduinoUno/twoCOM.py).

![alt text](/media/SerialMonitorTest_ArduinoUno/twoCOM_output.PNG)

### Experimental Process (2)
1. Connect USB-B wire to Arduino Uno and Computer Port
2. Connect TTL cable using jumper cables into Arduino Ports and ground.
3. Upload [serialMonitorTest.ino](/src/SerialMonitorTest_ArduinoUno/serialMonitorTest.ino) into the Arduino with COM3 selected in Arduino IDE under Tools -> Port.
4. When the code is done uploading, hit the white or blue button on the Arduino Board within a second.
5. Look at Serial Monitor and select 9600 Baud rate if not already selected.
6. Run [readCOM.py](/src/SerialMonitorTest_ArduinoUno/readCOM.py) in a Python Terminal to inspect.
7. Run [loopCOM.py](/src/SerialMonitorTest_ArduinoUno/loopCOM.py) in a Python Terminal to inspect.
8. Run [twoCOM.py](/src/SerialMonitorTest_ArduinoUno/twoCOM.py) in a Python Terminal to inspect.

Note: Steps 6-8 does not have to be done in order. The Arduino IDE used to upload the [serialMonitorTest.ino](/src/SerialMonitorTest_ArduinoUno/serialMonitorTest.ino) should be closed in order to run these .py codes. 

### Results (2)

The TTL cable works as expected by communicating both COM3 (USB-B for Arduino) and COM4 (TTL Cable). It showcases how the two COMs can communicate serial data from one Arduino microcontroller with Python through VSCode.

### Discussion (2)

Flipping the TX and RX cable did not work the first time, but it worked the second time. Nonetheless, this Part 2 showcases how some shortcomings of original microcontroller firmware can be adjusted within Python.

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
1. ArduinoDocs. (2022, June 15). SoftwareSerial Library. Arduino.cc. https://docs.arduino.cc/learn/built-in-libraries/software-serial/
2. ArduinoDocs. (2024, February 8). Bootloader. Arduino.cc. https://docs.arduino.cc/retired/hacking/software/Bootloader/
3. Autodesk. (2024, January 8). Reverse Engineering Software | What is Reverse Engineering? | Autodesk. Autodesk.com. https://www.autodesk.com/solutions/reverse-engineering 
4. Curry, M. (2018, December 20). Arduino Serial: A Look at the Different Serial Libraries – Martyn Currey. Martyncurrey.com. https://www.martyncurrey.com/arduino-serial-a-look-at-the-different-serial-libraries/
5. Flinders, M., & Smalley, I. (2024, September 25). Firmware vs. software. Ibm.com. https://www.ibm.com/think/insights/firmware-vs-software
6. GeeksforGeeks. (2020, December 8). Difference between Hardware and Operating System. GeeksforGeeks. https://www.geeksforgeeks.org/operating-systems/difference-between-hardware-and-operating-system/
7. Hopcroft, M. A. (2022, May 29). serialDataStream - File Exchange - MATLAB CentralFile Exchange - MATLAB Central. Mathworks.com. https://www.mathworks.com/matlabcentral/fileexchange/31958-serialdatastream
8. Mathworks. (n.d.). Serial Port Overview - MATLAB & Simulink. Www.mathworks.com. https://www.mathworks.com/help/instrument/serial-port-overview.html
9. Wu, S. (2024, July 15). What is a USB to TTL Serial Cable? | Romtronic. Romtronic. https://www.romtronic.com/what-is-a-usb-to-ttl-serial-cable/