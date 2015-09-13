# The Avatons Simulator
------------------------

# Breif summary: the simulator 
These codes to simulate the steps for the avaton gear.
We assume here the person is moving in his place, no forward steps yet implemented. The task is now more simpler, we only need to send the keypress command whenever the user steps.

========================================================
# The Avatons Emulator

# Phase one:
- Simulating the steps where we issue a keypress command to the computer from the simulator [almost done].
- Implementing this mechanism using the oculus, the person will not step at this point, the simulator does and will initiate the motion in the virtual reality (VR). The simulator Ahmed implemented is a bit slow but efficient (read about Ahmed's simulator in a separate readme file). 

-------------------------------------------------------
# Phase two:
- Build a python based emulator. It takes 'live' input values from external hardware and convert them into specific keypress to control the motion in the virtual reality.
- To build the emulator with python the following packages will be useful:
          - PyKeyboard: needs Xlib (for linux), Quartz, AppKit (for mac) and pywin32, pyHook (for windows)
          - PyMouse: could be useful but not used at the moment.
- This emulator should be executed while the VR is running.
- To be updated ...
