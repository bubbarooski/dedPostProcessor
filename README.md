# 📃 Description
This program is a GUI based post-processor that can take a g-code file exported from Cura and edit it to work on a very specific setup of a wire DED metal 3D printer and CNC machine. When ran, it adds neccesary commands, like turning the laser on/off or retracting the weld wire, and comments in the g-code that help the user with the print, such as length of time for print, min/max dimensions, and the total amount of times the laser has to turn on and off. The program allows the user to add customizable wait times at different spots during the print, like during layer changes or when the printer has to move to a new section of the print. This program is also designed to work with a very specific Cura profile and will most likely not work with a different profile.

# ▶️ Usage
By running the driver file, the post processor will launch.
<p align="center">
  <img src="https://github.com/user-attachments/assets/427b7d2e-3066-4927-ae8a-c69032341d52">
</p>

### Macro Menu
In this section, you can customize the macros that will be inserted into different spots of the code. These macros are understood by the CNC machine and do different things and need to be called at specific times. 
The user can customize the following macros:
- Fast Move: the time between moving to a different spot in the same layer
- Layer move: the time between layers
- Printing: tells the printer to begin printing
- Retract: tells the printer to stop printing and retract wire
- Warming: tells the printer to begin warming the plate
- Outer wall, inner wall, and fill: tells the printer to begin printing but with slightly different settings than standard printing

### Toolbox Menu
Only has the ability to print out the currently selected macros. There were plans for potentially more miscellaneous little scripts that could help, hence the name toolbox.

### Printing File
This allows the user to select a g-code file from anywhere on their computer. Once selected, it will display the file in this section. There is an included test file that shows the capabilities of the program.

### Post-processed File
When the user select a printing file, the program will immediately run the file through the post-processor and display the processed file. This allows the user to look through the file before saving it.

### File Settings
This allows the user to select a file number that will be printed on the first line of the file. There is also a drop down to select the user, which will be added as a comment in the file for a simple verison control system. Once the file is ready, the user can save the file anywhere on their computer.

### Machining File
This section was never implemented as it was unneeded. I threw it into the GUI because there was plans to use it but it never got that far. The same for "Machining" toggle in the File Settings section.

### Test File
There is a test file that when ran, will launch a terminal based version of the program that allows you to select a g-code file to post process. When selected, it will print a ton of diagnostic information about the print to show the user if both the input file is good or if the post-processor is working correctly.
<p align="center">
  <img src="https://github.com/user-attachments/assets/56484bc1-f2a3-46ee-bc9d-72e6e8b69df0">
</p>

