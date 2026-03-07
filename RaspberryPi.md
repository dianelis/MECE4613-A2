Industrial Automation
Department of Mechanical Engineering
Columbia University
Ali Dadgar


# Setting up your Single Board Computer

The following instructions may be used to set up your USB Flash Drive or SD Card.

It is highly recommended that each student have his/her own disk.


# Install Respberry Pi OS:

Use a fresh USB flash drive or SD card.

Follow the directions here:
https://www.raspberrypi.com/software/

Once complete, you may follow the next steps.

# Turn on your Raspberry Pi (RP)

Insert your flash drive into USB port of RP.
Plug the RP's power.
Plug the external monitor into HDMI port.
Attach a USB mouse.
Follow the instructions ...


Create user by entering username, passwords ...

The username must be your_uni - e.g. am3469

Connect to wifi ...

Choose Browser: choose Firefox

Enable Raspberry Pi Connect: slide to accept it.

Once finished, restart RP.



# NOTE:

1. When you see Dollar Sign ($), it shows command line start in terminal.
  You do not have to type in that sign.
  For example, when you see the following line:
  $ vim
  it means that you have to type 'vim' in your terminal.
2. When you see something inside angle brackets such as <something>, it means
   that 'something' should be replaced by your parameter.
   Example: If my uni is am3469, then: <your_uni> = am3469


Open your terminal and adjust the settings:
$ sudo raspi-config
  select "Interface Options"
      Enable: "SSH"
      Enable: "VNC"
      Enable: "I2C"

It is a good engineering (and scientific) practice to familiarize yourself with 'vim' or 'vi'.
It is a quick, light and ubiqutous editor that can be found almost all industrial servers.
Other editors such as vscode are easy and graphical UIs but won't be functional in many cases.
Then, we'll need to install vim first to start working with it:
$ sudo apt install vim

Reboot the system:
$ reboot

Now, get the IP Address of your RP.
This is your computer unique ID that your network is assigning to your robot's computer.
$ hostname -I
(e.g. 192.168.124.97)

You will be able to connect to your RP - using ssh, from a remote computer on the same network:
$ ssh <your_uni>@<your_ip_address>

If this does not work, or you receive "connection refused" error, you should adjust your settings:
    1. First, you can check if - for instance, "ssh" is enabled:
       $ sudo systemctl status ssh
       This will tell you if the command is running in your RP or not.

       If you do not see "running", you may activate it manually:
       $ sudo systemctl start ssh

    2. Second, check if the ssh config file located at /etc/ssh/sshd_config contains permits:
       NOTE: in order to open that file use vi (https://cs.stanford.edu/people/miles/vi.html):
       $ sudo vi /etc/ssh/sshd_config
           search for PermitRootLogin
           Following lines should be present in this file - if not modify it:
           PermitRootLogin yes
           PermitRootLogin prohibit-password
       save the file and exit.

    3. Third, restart systemctl:
       $ sudo systemctl restart ssh
       Now, you can the status if it's running:
       $ sudo systemctl status ssh
       You should see that it's running ...

    4. Last, you can ssh from a local computer:
        $ ssh your_uni@your_ip_address



# Setting up the Adafruit CRICKIT HAT (CH)

CH is an additional electronics to be attached to your RP to enhance robotic mechanical works.

Reference manual: https://learn.adafruit.com/adafruit-crickit-hat-for-raspberry-pi-linux-computers

1. Update the firmware as it's indicated in that manual.
   You may use your powerbank's cable to connect CH to your computer.
   - Follow all the instructions in the a/m link - under 'Update Your Crickit' tab.

2. When RP is off, put CH on its GPIO - very carefully.

3. Connect CH power using USB A from power bank to the power jack input of CH.

4. Switch on CH. Check the LED is green.

5. In your RP's terminal check the bus connection's address:
    $ i2cdetect -y 1
    This should show 0x49 hexadecimal address as below:
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:                         -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- -- 49 -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --
    
    NOTE:
    i2c (Inter-Integrated Circuit) is a bus communication protocol used in microcontrollers and embedded systems 
    to connect and communicate with multiple peripheral devices. The above command checks the connection of RP's 
    GPIO and gives he hexadecimal address of the connected devices.
    For more information about i2c, refer to: https://learn.sparkfun.com/tutorials/i2c


# reboot

Now, update your RP using its terminal and reboot it:
   $ sudo ap update
   $ sudo apt upgrade
   $ sudo apt autoremove
   $ sudo reboot


# create virtual environment

Create a python virtual environment to install our required packages.
   $ python3 -m venv ~/pyenv
   $ ~/pyenv/bin/pip install adafruit-circuitpython-crickit

Make activation of environments easier:
   $ echo "alias activate='source ~/pyenv/bin/activate'" >> ~/.bashrc
   Now when you type 'activate' in your python terminal, it'll activate pyenv which you created.
   Activate your pyenv:
   Open a new terminal and:
   $ activate
   Ideally, you'd want the activation is done automatically; meaning that when you turn your board on, and
   open the terminal, or ssh to your machine, it goes directory to your envrionment. For this purpose, open
   your bashrc and add activate to the last line.


# check installed software

Check CH software and installation:
   $ python
   $ from adafruit_crickit import crickit
   use Ctrl + D to exit the terminal
 
