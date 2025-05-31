# SomeRandomStranger123
# Force devices with KACE agent 9.0+ and > 14 to check into KACE.
#7/2/2021

# Import necessary modules.
import os
import sys
import csv
import datetime
import getpass

# Set global variables.
MIA = []  # List to store hostnames of devices.
fields = []  # List to store field names from CSV.
user = getpass.getuser()  # Get current user.
runkbot = r'"C:\\Program Files (x86)\\Quest\\KACE\\runkbot.exe"'  # Path to runkbot executable.
runamp = r'"C:\\Program Files (x86)\\Quest\\KACE\\AMPTools.exe"'  # Path to AMPTools executable.
filename = "C:\\Users\\" + user + "\\Downloads\\devices(2).csv"  # CSV file path.
location = "C:\\Users\\" + user + "\\Downloads\\"  # Location to save files.

# Read the CSV file and gather hostnames within the file.
def readfile(filename):
    with open(filename, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')  # Delimiter is a comma in the given file.
        fields = next(data)  # Remove the first line and store it into a list called fields.
        for row in data:  # Iterate through each row and append the hostname to the MIA list.
            MIA.append(row[0])

## Define function to process the Inventory Update for individual machines and
## deploy any waiting managed installs.
def ampTools(test, user):
    # Run AMPTools commands.
    os.chdir("C:\\Program Files (x86)\\Quest\\KACE\\")
    # Run conf.
    file1 = open("C:\\Users\\" + user + "\\Downloads\\Kace_Inv_Log.txt", "a")  # Append mode.
    file1.write("\n\nRunning AMPTools.exe -resetconf host=**YOURHOSTNAME**")
    file1.close()
    os.system('psexec.exe \\\\' + test + " cmd /c " + runamp + ' -resetconf host=**YOURHOSTNAME** 1>> C:\\Users\\' + user + '\\Downloads\\Kace_Inv_Log.txt 2>>&1')
    # Run InvUpdate.
    InvUpdate(test, user)

def InvUpdate(test, user):
    # Run kbot 6 0.
    file1 = open("C:\\Users\\" + user + "\\Downloads\\Kace_Inv_Log.txt", "a")  # Append mode.
    file1.write("Running runkbot 6 0")
    file1.close()
    os.system('psexec.exe \\\\' + test + " cmd /c " + runkbot + ' -s 6 0 1>> C:\\Users\\' + user + '\\Downloads\\Kace_Inv_Log.txt 2>>&1')
    # Run kbot 3 0.
    file1 = open("C:\\Users\\" + user + "\\Downloads\\Kace_Inv_Log.txt", "a")  # Append mode.
    file1.write("Running runkbot 3 0")
    file1.close()
    os.system('psexec.exe \\\\' + test + " cmd /c " + runkbot + ' -s 3 0 1>> C:\\Users\\' + user + '\\Downloads\\Kace_Inv_Log.txt 2>>&1')
    # Run kbot 4 0.
    file1 = open("C:\\Users\\" + user + "\\Downloads\\Kace_Inv_Log.txt", "a")  # Append mode.
    file1.write("Running runkbot 4 0")
    file1.close()
    os.system('psexec.exe \\\\' + test + " cmd /c " + runkbot + ' -s 4 0 1>> C:\\Users\\' + user + '\\Downloads\\Kace_Inv_Log.txt 2>>&1')

# For every machine in the file, do a ping. If ping is successful, run the InvUpdate module.
def testmachines(MIA, user):
    x = 0
    for machines in MIA:
        test = MIA[x]
        x = x + 1
        response = os.system("ping -c 1 -n 3 " + test)
        if response == 0:
            # Output hostname, date, and time to file.
            timestamp = datetime.datetime.now()
            file1 = open("C:\\Users\\" + user + "\\Downloads\\Kace_Inv_Log.txt", "a")  # Append mode.
            file1.write("Testing computer: " + str(test) + " at " + str(timestamp))
            file1.close()
            # Run AMPTools.
            ampTools(test, user)

# Start the program.
readfile(filename)
testmachines(MIA, user)
