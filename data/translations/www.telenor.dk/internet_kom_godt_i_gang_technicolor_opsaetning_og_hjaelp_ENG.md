# Setting up your Technicolor TG799 xtreme

## What type of connection do you have?

You can see what type of connection you have in the order confirmation you received from us when you ordered your new internet service.

More

Telephone socket (DSL) Fiber

## Watch this short video guide and get started (DSL)

## **Written guide**

**How to connect your router**

  1. Connect the grey plug into the grey DSL port on the router
  2. Connect the other end of the plug into the telephone socket on the wall. If you have a three-pin telephone socket, you need to use the three-pin adapter. Connect the adapter to your main socket and then the telephone cable to the adapter. If you live in a house and have multiple telephone sockets, the main socket is usually the one closest to the road. Sometimes there may be a TDC or TeleDanmark logo in the socket. If you have a double socket (three-pin telephone socket at the bottom and KAP socket above), it also indicates that it is a main socket. If you live in an apartment, the main socket is most often located near the back stairs or on the back of the building if there are no back stairs.
  3. Turn on the router

**How to connect to the internet wirelessly with your devices**

  1. Find your network name (Network Name) and password (Wireless Key) by looking at the bottom of your router
  2. Search for wireless networks on your device and select your network name (Network Name)
  3. Enter the password (Wireless Key)

**How to connect to the internet with a cable**

  1. Plug a network cable into one of the yellow ports
  2. Plug the other end of the network cable into your device

Enjoy your new internet!

## Guide

**How to connect your router**

  1. Connect the network cable with the red end into the red network port (WAN) on the router
  2. Connect the network cable to your fiber box
  3. Plug the router into the power outlet - this is done as follows: turn off the power outlet, mount the cable in the router, mount it in the power outlet and finally turn on the power outlet

**How to connect to the internet wirelessly with your devices**

  1. Find your network name (Network Name) and password (Wireless Key) by looking at the bottom of your router
  2. Search for wireless networks on your device and select your network name (Network Name)
  3. Enter the password (Wireless Key)

**How to connect to the internet with a cable**

  1. Plug a network cable into one of the yellow ports
  2. Plug the other end of the network cable into your device

Enjoy your new internet!

## What the LEDs (lights) on the router mean

Status

If the status light is on:

**Green:** there is a connection to the internet  
 **Orange** : the router is starting up  
 **Red:** there is no connection to the internet  
 **Blue:** the router is set up with GIP/GIP+

Broadband

The light flashes when the router is trying to start up, and it lights up steadily when there is a DSL connection. If the router is used for a fiber connection, the light will light up as soon as there is a connection to the fiber box. In this case, the light does not indicate whether there is a connection to the internet, only that there is a connection between the router and the fiber box.

Internet

The light indicates whether an internet connection has been established.

**The light:**  
 **Lights up green:** when an IP connection has been established  
 **Blinking:** when there is traffic on the internet connection  
 **Lights up red:** if there is a connection error  
 **Is off:** if there is no IP connection

Wireless 2.4 Ghz

Shows whether the 2.4Ghz signal is on. The light is constantly on when the signal is on and blinks with traffic on the 2.4Ghz network.

Wireless 5 Ghz

Shows whether the 5Ghz signal is on. The light is constantly on when the signal is on and blinks with traffic on the 5Ghz network.

WPS

If the light is on, it indicates that a WPS connection has been established.

Ethernet

If the light is on, it indicates that equipment is connected and turned on in one of the four Ethernet ports on the router. The light blinks with traffic.

Voice

Lights up green if the router is set up with a VoIP profile.

## More settings

How to change the router's name and password

  1. Open your browser and enter **http://10.0.0.1:2033** press **Enter** to open the login page
  2. Enter your code, which you can find on the underside of your router under **Accesskey**, and then press **Sign in**
  3. Press **Wireless** in the upper right corner
  4. Here the code is changed under **Wireless Password**, and your WiFi name can be changed under **SSID name**
  5. Then press **Save** and your change is now saved. It may take about 10 minutes for changes to take effect

How to reset the router

  1. Gently insert the end of a paperclip (or similar) into the small hole at Reset. Hold the button down for about 10 seconds and release the button again
  2. When the button is released, all lights will go out and the status will start to blink shortly after
  3. The router may take several minutes to start up and will blink in status while doing so
  4. Once the router is set up, you can log in with the router's original network name and password and reinstall your personal settings

Fixed LAN IP

Fixed LAN IP is used if it is important that your device has a specific IP address. This could be a sound system or a computer that needs to be set up with port forwarding.

  1. Log in to your router  
Open your browser and type: [https://10.0.0.1:2033](https://10.0.0.1:2034)  
 **NOTE:** A warning may appear on the page, ignore this and continue  
 **Username:** admin  
 **Password:** Enter the password for your router. The code is on the underside of the router and is called "Access Key" (if you have created a personal code, use that instead)

  2. Click on the **Local network** menu  

  3. Under the **Static Leases** section, you can set up, delete or edit the fixed IP addresses
  4. Click the **Add New Static Lease** button  

  5. **Fill in Hostname** : You decide the name yourself and it is intended to make it easier to remember what the rule is

**MAC Address:** Here you can choose between the devices that are already connected to the router. Under the **IP** field, the router will also show you the IP that the device has already been assigned  
If the device is not already on the list, you can enter the MAC address of the device you want to create a fixed LAN IP for.

**IP:** Choose the IP device that has already been assigned, or enter the IP you want the device to have. If you choose a different IP, you must restart the router before the change takes effect  
Press the **Add** button

6\. To edit a rule, press the **Edit** button, and to delete a rule, press the cross

Port Forwarding

If your multiplayer game on, for example, PlayStation or X-Box has problems connecting online via the router, it may help to open ports in the router.

  1. Log in to your router by opening a web browser and typing: **https://10.0.0.1:2033**  
 **NOTE:** A warning may appear on the page, ignore this and continue.  
 **Username:** admin  
 **Password:** Enter the password for your router. The code is on the underside of the router and is called "Access Key" (if you have created a personal code, use that instead)

2\. As an alternative to setting a fixed IP on the device itself, you can use the **Static Lease** function on the router. If you have already specified a fixed IP on your device, you can skip this step  
Select **Add New Static Lease**  
Specify what hostname the device should have. e.g. "Chromecastistuen"  
Select **MAC address** on the device in the **MAC Address** dropdown menu  
In the **IP** field, enter the IP that the device should be assigned  
 **NOTE** : This IP must be within the DHCP pool that is defined under **DHCP Start - End**  
Save the setup by pressing the small plus at the end of the line or cancel by pressing the cross next to it

3\. Click on the **WAN Services** menu

4\. Under the **IPv4 Port Forwarding Table**  
Here you get an overview of the rules that have already been created. This is also where the rules are created, edited and deleted.  
 **NOTE:** To ensure that the rules work, you should have a fixed IP on the device to which the rule is created

5\. Click the **Add New IPv4 Port Mapping** button and write the name you want

6\. **Protocol** : select which protocol the rule should use

7\. **WAN Port and LAN Port** : filled in with the port to be forwarded.

8\. **Destination IP** : write the IP of the computer or device the rule should point to.  
Press the **Add** button, which is marked with a small plus

9\. To edit a rule, press the **Edit** button, and to delete a rule, press the **cross**

Router specifications

**Router specs:**

  * 1x RJ11/RJ14 DSL port
  * 4x 1Gbit LAN port

  
**WiFi connection:**

  * IEEE 802.11b/g/n/ac/

Did this page help you?

Yes __

No

Thank you for letting us know.

We would greatly appreciate it if you would tell us why the article did not help you.

It wasn't what I was looking for.

There are not enough examples.

The information is difficult to understand.

The information does not solve my problem.

Other

Send __

We are glad that this article was helpful.

Thank you for your feedback.

### Do you still have questions?

If you are in doubt about anything, you are always welcome to contact our customer service

- We are available Monday to Friday from 8 am to 8 pm.

[ ](/kundeservice/kontakt/)

[ ](/)

[ ](https://www.linkedin.com/company/telenor-group)

### The servers are teasing

It's a little embarrassing, but we promise to get it fixed as soon as possible.

[ Go to the front page ](/) Close

### You need to log in again

We automatically log you out when you have been inactive for a while. Just for security.

[ Log in ](/mit-telenor/profil/)

Close

### Your session has expired

Refresh the page or log in again

[ Refresh ](/mit-telenor/profil/) Close