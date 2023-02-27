2-CH-Relay-HAT from seengreat:www.seengreat.com
 =======================================
# Ⅰ  Instructions
## 1.1、Product Overview
This product is a 2-ch relay Raspberry Pi expansion board, suitable for Raspberry Pi Zero/Zero W/Zero WH/2B/3B/3B+/4B, four relays on board, can control shutdown separately.<br>
## 1.2、Product parameters
Supply voltage:3.3V&5V<br>
Relay allows access to the load:250V/5A<br>
With relay working indicator, it is convenient to check the working status of the relay<br>
Optocoupler isolation circuit, strong anti-interference ability, stable work<br>
Open source demo codes available for Raspberry Pi<br>
## 1.3、Product dimensions
|Size	|56mm(Length)*34mm(width)|
|-----------|-------------------------------|
|Weight	|25g|
# Ⅱ  Usage
## 2.1、Hardware interface configuration description
The sample program in the Raspberry Pi motherboard uses the wiringPi pin definitions. The definition of the connection with the Raspberry Pi motherboard is shown in the following table：<br>
|2-CH Relay HAT	|Pin function	|BCM 	|wiringPi| 
|----------------------|-----------------------|----------|---------|
|5V	|3.3V&5V	|3.3V&5V	|3.3V&5V|
|GND	|GND	|GND	|GND|
|CH1	|Channel 1	|26	|P25|
|CH2	|Channel 2	|19	|P24|

Table2-1 2-CH Relay HAT and Raspberry Pi pin<br>
The Resource Profile is shown in the figure below:<br>
![image](https://github.com/seengreat/2-CH-Relay-HAT/blob/main/2-CH-Raley-HAT-1.png)<br>
Figure 2-1 2-CH Relay HAT Resource Profile on diagram<br>
1->Relay control signal level and amplitude sliding switch, available 3.3V or 5V.<br>
2->Relay working indicator: when the light is on, it means that the normally open end of the relay is closed, the normally closed end is disconnected, and when the light is off, it means that the normally open end of the relay is disconnected and the normally closed end is closed.<br>
3->Relay
4->Relay output
5->Power indicator
6->PH2.0 4PIN Module wire
7->2.54mm 4PIN connector
Relay wiring diagram is as follows:<br>
![image](https://github.com/seengreat/2-CH-Relay-HAT/blob/main/2-CH-Raley-HAT-2.png)<br>
Relay wiring instruction diagram<br>
## 2.2、Demo Codes Usage
Wiringpi library installation：<br>
sudo apt-get install wiringpi<br>

wget https://project-downloads.drogon.net/wiringpi-latest.deb  #<br>
Version 4B upgrade of Raspberry Pi<br>
sudo dpkg -i wiringpi-latest.deb<br>
gpio -v #<br>
If version 2.52 appears, the installation is successful <br>
#For the Bullseye branch system, use the following command:<br>
git clone https://github.com/WiringPi/WiringPi<br>
cd WiringPi<br>
. /build <br>
gpio-v<br>
#Running gpio - v will result in version 2.70. If it does not appear, it indicates an installation error<br>
If the error prompt "ImportError: No module named 'wiringpi'" appears when running the python version of the sample program, run the following command<br>
#For Python 2. x version <br>
pip install wiringpi<br>
#For Python version 3. X<br>
pip3 install wiringpi<br>
Note: If the installation fails, you can try the following compilation and installation:<br>
git clone --recursive https://github.com/WiringPi/WiringPi-Python.git<br>
Note: The -- recursive option can automatically pull the submodule, otherwise you need to download it manually.<br>
Enter the WiringPi Python folder you just downloaded, enter the following command, compile and install:<br>
#For Python 2. x version<br>
sudo python setup.py install<br>
#For Python version 3. X<br>
sudo python3 setup.py install<br>
If  error occurs:<br>
At this time, enter the command sudo apt install swig to install swig. After that, compile and install sudo python3 setup.py install. If a message similar to the following appears, the installation is successful.<br>

Execute the sample program<br>
Python:<br>
Go to the Python directory:<br>
cd /home/pi/2-ch_relay/python<br>
performance:<br>
sudo python3 2-ch-relay.py<br>
C:<br>
Go to the C directory:<br>
cd /home/pi/2-ch_relay/c<br>
performance:<br>
sudo make clean<br>
sudo make<br>
sudo ./main<br>
__Thank you for choosing the products of Shengui Technology Co.,Ltd. For more details about this product, please visit:
www.seengreat.com__

