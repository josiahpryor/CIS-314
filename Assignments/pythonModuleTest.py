import os
#directory
currentDirectory=os.getcwd()
print(currentDirectory)

#storage drives on pc
drives=os.listdrives()
print(drives)

#current logged in user
user=os.getlogin()
print(user)

#process id
processID=os.getppid()
print("Proccess ID", processID)

#excutes command in subshell
command="ipconfig"
executeCommand = os.system(command)
print(executeCommand)

#creates and then removes pythonTest folder
testFolder="pythonTest"
os.makedirs(testFolder)
os.startfile(testFolder)



