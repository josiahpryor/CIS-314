#Create list and import file text into list to manipulate text
in_data = []
in_file = open("access.log")
in_data = in_file.readlines()
in_file.close()
y=len(in_data)
print("access.log can now be found in the list \"in_data\" with",y,"entries.")


#Loop through list of text, extracting BotPoke
x = 0
while x < len(in_data):
    if in_data[x].find("BotPoke") > 0:
        in_data.pop(x)
    else:
        x+=1
print("BotPoke is now filtered out of the file")
y=len(in_data)
print("There are", y,"log entries remaining.")

#ip_pattern is regex format of an ip address that is at beginning of line
#List is iterated through, with ip being extracted, and then the string of the ip appended 
import re
x=0
ip_list = []
ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
while x < len(in_data):
    ip_address = re.findall(ip_pattern, in_data[x])
    ip_list.append(ip_address[0])
    x+=1
#set filters out duplicates from list
ip_set = set(ip_list)
print("The remaing unique IP addresses are:")
print(ip_set)