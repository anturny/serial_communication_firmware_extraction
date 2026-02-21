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
Hardware Serial is a wired communication that can transmit and receive at the same time, work while the Arduino is performing other tasks (via UART-to-USB adapter chip), and handle fast baud rates [7].

Software Serial uses serial communication on digital pins of a physical board and software to replicate functionality of hardware serial. Unlike Hardware Serial, multiple software serial ports are possible [1]. It is slightly more unreliable at very slow or very fast speeds due to its problems with timing. 

TTL Cables are wires used for microcontrollers, embedded systems, or DIY electronics. They allow the computer to communicate with devices that use Transistor-Transistor Logic (TTL) signals that are digital and have specific voltages [14]. A logic 0 is usually 0 V while a logic 1 can be 3.3 V or 5 V.

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

Software is a set of instructions that guide the core operations of a computing device [8].

Hardware is the physical component of a computer that a computer cannot function without. It provides the physical resources required for a computer to function.

Operating System is the system software that runs on the computer and manages all application programs to provide an interface between the user and hardware [9].

Serial Port allows a physical device to send and receive bytes of information in a serial manner with one bit at a time in either a binary format or a text (ASCII) format. Communication is established through the serial port [12].

Serial Data Stream helps receive and process a continuous data stream from a device connected to a USB or serial port rather than simultaneous parallel communication [11].

Reverse Engineering is the process of taking something apart to discover how it works. It normally includes disassembling a complete product and analyzing each component to see how they work together [4].

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
This project includes using Arduino as an In-System Programmer where we use an Arduino board to program another Arduino board using the ICSP (In-Circuit Serial Programmer). It is meant to primarily flash new bootloaders.

### Short Background (3)
Tool chain is a set of software tools that work together to complete a process. In our case, the Arduino toolchain is ran to perform the uploading of the code [13].

Debug boards are hardware tools used in electronics to test, verify, and troubleshoot circuits by controlling logic levels or by interfacing with a microcontroller to monitor behavior. It is meant to be apart of a methodical process of locating and eliminating bugs or defects from a computer program [10].

Arduino ISP is a tool to directly program the microcontroller throught the ICSP controller that allows the user to upload sketches and burn the bootloader on any AVR based boards. By uploading a sketch with an external programmer, we can remove the bootloader and use the extra space for our sketch [3].

Hex (short for Hexadecimal) is a numbering system that uses a base-16 representation for numeric values and can represent large numbers with fever digits. It has 16 symbols, or possible digit values 0-9, followed by six alphabetical letters (A, B, C, D, E, and F) [5].

Intel Hex is an ASCII text based file format used to convey binary information that is commonly used for programming microcontrollers and embedded devices. It converts binary data into readable hexadecimal ASCII characters, organizing them into "records" (lines) that contain data, memory addresses, and checksums for error verification [6].

Binary code is a coding system using the binary digits 0 and 1 to represent a letter, digit, or other characters in a computer or other electronic device.

### Build of Materials (3)
* 2 Arduino Uno Board
* USB-B Data Cable
* TTL Cable
* Laptop/Desktop with Arduino IDE
* 5 Female-Female Wires
* 1 Male-Female Wire

### Media (3)
The following reference was used to bridge the connections using female-female wires between two Arduino Unos.

![alt text](/media/SerialMonitorTest_ArduinoUno/ArduinoICSPReference.png)

The following is the real life connection between two Arduino Uno boards using wires to connect the ICSPs.

![alt text](/media/SerialMonitorTest_ArduinoUno/ArduinoISPWired.jpg)

Where
* Purple - Reset (Only Male-Female Wire)
* Red - VCC (Power)
* Grey - MOSI
* White - GND
* Orange - MISO
* Yellow - SCK

### Experimental Process (3)
1. Define one Arduino board as your debugger board (Ard. 1).
2. Connect USB-B data cable to Ard. 1 and upload any sketch in Arduino IDE to this board. (Remember to hit the button within 8 seconds to flash the memory).
3. Make the connections as shown in [Media (3)](#media-3) with 5 Female-Female wires and 1 Male-Female wire between Ard. 1 and Ard. 2 (referring to the Debugger Arduino and Arduino to write to).
4. Download [AVRDUDESS](https://blog.zakkemble.net/avrdudess-a-gui-for-avrdude/) in order to setup the ISP programming.
5. Open AVRDUDESS and select your Programmer (Arduino or arduino_as_isp). Then select your port (know which one from Arduino IDE). Then select baud rate in accordance to your board (9600 baud for Arduino Uno).
6. Select "Detect" under MCU and it should automatically detect. 
7. Under "Flash", select "Read" then create any .hex file somewhere you can access. Set the format to "Intel Hex". Then hit "Go." A new file should appear where you save it to.
8. We now replace our second Arduino (Ard. 2) with another Arduino to flash the code to. Remake the same connections as in step 3.
9. Under "Flash", set to "Write" then select the "Program" button. This should flash the debug onto the new Arduino board. 


### Results (3)
The experiment is incomplete as of 2/21/2026, but we should expect the Arduino board (Ard. 1) that we flashed the initial sketch into to be our debugger board. By making an ICSP connection with another Arduino board coupled with the AVRDUDESS program, we should be able to upload into any other microcontroller what we uploaded as a sketch into Ard. 1. This will help us unbrick any board or fix any bricked bootloaders in the future.

### Discussion (3)
This experiment was the hardest of any on this page due to the nature of experimenting with new software and hardware. As of 2/21/2026, the experiment still has not been complete due to my personal COM3 port having connections with detecting an MCU within the AVRDUDESS app. I will reconvene and finish it soon.

This project was meant to help users understand the importance of in-system programmers and how it transfers data as an Intel Hex file. 

----------------------------------------------------
## Citations and References
1. ArduinoDocs. (2022, June 15). SoftwareSerial Library. Arduino.cc. https://docs.arduino.cc/learn/built-in-libraries/software-serial/
2. ArduinoDocs. (2024a, February 8). Bootloader. Arduino.cc. https://docs.arduino.cc/retired/hacking/software/Bootloader/
3. ArduinoDocs. (2024b, March 14). Arduino ISP. Arduino.cc. https://docs.arduino.cc/retired/boards/arduino-isp/
4. Autodesk. (2024, January 8). Reverse Engineering Software | What is Reverse Engineering? | Autodesk. Autodesk.com. https://www.autodesk.com/solutions/reverse-engineering
5. Awati, R. (2022, June). What is hexadecimal? - Definition from WhatIs.com. WhatIs.com. https://www.techtarget.com/whatis/definition/hexadecimal
6. Binary Encoding Techniques Across Programming Languages. (2025, November 23). Intel HEX with Scala | Binary Encoding Techniques Across Programming Languages. Binary Encoding Techniques across Programming Languages. https://mojoauth.com/binary-encoding-decoding/intel-hex-with-scala#understanding-intel-hex-format
7. Curry, M. (2018, December 20). Arduino Serial: A Look at the Different Serial Libraries – Martyn Currey. Martyncurrey.com. https://www.martyncurrey.com/arduino-serial-a-look-at-the-different-serial-libraries/
8. Flinders, M., & Smalley, I. (2024, September 25). Firmware vs. software. Ibm.com. https://www.ibm.com/think/insights/firmware-vs-software
9. GeeksforGeeks. (2020, December 8). Difference between Hardware and Operating System. GeeksforGeeks. https://www.geeksforgeeks.org/operating-systems/difference-between-hardware-and-operating-system/
10. GeeksforGeeks. (2023, January 17). What is Debuggers? GeeksforGeeks. https://www.geeksforgeeks.org/operating-systems/what-is-debuggers/
11. Hopcroft, M. A. (2022, May 29). serialDataStream - File Exchange - MATLAB CentralFile Exchange - MATLAB Central. Mathworks.com. https://www.mathworks.com/matlabcentral/fileexchange/31958-serialdatastream
12. Mathworks. (n.d.). Serial Port Overview - MATLAB & Simulink. Www.mathworks.com. https://www.mathworks.com/help/instrument/serial-port-overview.html
13. Tutorial 6: Arduino Tool Chain Overview - Academy for Arduino. (2019). Academy for Arduino. https://learnarduinonow.com/tutorial-6-arduino-tool-chain
14. Wu, S. (2024, July 15). What is a USB to TTL Serial Cable? | Romtronic. Romtronic. https://www.romtronic.com/what-is-a-usb-to-ttl-serial-cable/