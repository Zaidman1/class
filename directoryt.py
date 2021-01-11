import os.path

#adding these inputs to library
dir_path = input("\nEnter  path of the directory : ")
filename = input("Enter name of file : ")

#finding out if the directory exists
if not os.path.isdir(dir_path):
    os.makedirs(dir_path)   

#inpit for full path
full_path = dir_path + filename
#create new path unless arleady exists
file_1 = open(full_path, 'a')

#inputs for name, address, phone
name = input("Enter the name : ")
file_1.write(name + ',') 

address = input("Enter the address : ")
file_1.write(address + ',')

phone = input("Enter the phone number : ")
file_1.write(phone)
file_1.close()

#read created file
file_2 = open(full_path, 'r')
output = file_2.readlines()
#print file path
print("You created a file here : \n", output)
file_2.close()