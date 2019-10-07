

# iiwaPy

A python librarry used to control KUKA iiwa robots, the 7R800 and the 14R820, from an external computer using python 2.7.

Using the iiwaPy the utilizer can control the iiwa robot from his/her computer without a need for programming  the industerial manipulator.

A basic knowledge of using python is required.


--------------------------------------

# Required packages

The iiwaPy is a Python wrapper for the KUKA sunrise toolbox, [found in here](https://github.com/Modi1987/KST-Kuka-Sunrise-Toolbox).
To utilize the iiwaPy, you have to install the [KST Sunrise Server Application, click here](https://github.com/Modi1987/KST-Kuka-Sunrise-Toolbox/tree/master/KUKA_Sunrise_server_source_code) into the Kuka iiwa controller.


--------------------------------------

# Video tutorials

Video tutorials on controlling IIWA from python [are available in here](https://www.youtube.com/watch?v=QkUe8JIs63A&list=PLz558OYgHuZdRoxkqQ-M9LOdksZnEWbKq&index=2&t=0s).


--------------------------------------

# To test the iiwaPy

To test the iiwaPy follow the steps:

## On PC side:
1- Establish a peer to peer connection between the PC and the robot, [described in videos 1 and 2 of the play list](https://www.youtube.com/playlist?list=PLz558OYgHuZd-Gc2-OryITKEXefAmrvae);

2- Synchronise the [KST Sunrise Server Application](https://github.com/Modi1987/KST-Kuka-Sunrise-Toolbox/tree/master/KUKA_Sunrise_server_source_code) into the robot controller;

## On the robot side:
1- Run the application "MatlabToolboxServer" from the smartPad of the robot.

2- You have 60 seconds to connect from the Python script before the server is shut down automatically.

## From Python on your PC
From inside python IDE run the tutorial script [Tutorial_getters, available here](https://github.com/Modi1987/iiwaPy/blob/master/python_client/Tutorial_getters.py), you shall see dara acquired from the robot controller printed inside python console.

--------------------------------------

Copyright: Mohammad Safeea, first commit 8th-April-2019

