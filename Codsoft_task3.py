#PASSWORD GENERATOR APPLICATION:
#user can specify the length and complexity
#user input: length of pwd
#generate pwd with random characters of given length
#display the pwd

import random
print("Welcome to the password generator!")
#taking desired length of pwd from user(for safety purposes the minimum length is 3):
userlen=int(input("Please enter the desired length of the password to be generated(length should be greater than 2 for better protection against cyberattacks): "))
#taking user input for the complexity of the password:
usercom=input("Please enter the desired complexity of the password (Easy, Medium or Hard): ")
#A function which generates the passwords based on the chosen complexity by the user
def pwd_gen():
    pwd_list=[]
    if usercom.lower()=="easy":
        char="abcdefghijklmnopqrstuvwxyz"
        for i in range(userlen):
            ran1=random.choice(char)
            pwd_list.append(ran1)
        pwd_list="".join(pwd_list)
        print("Your password is : ", pwd_list)
    
    elif usercom.lower()=="medium":
        char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
        for i in range(userlen):
            ran1=random.choice(char)
            pwd_list.append(ran1)
        pwd_list="".join(pwd_list)
        print("Your password is : ", pwd_list)
    elif usercom.lower()== "hard":
        char="abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()+-={}<>"
        char1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num="1234567890"
        for i in range(userlen-2):
            ran1=random.choice(char)
            pwd_list.append(ran1)
        pwd_list="".join(pwd_list)
        pwd_fin=random.choice(char1)+random.choice(num)+pwd_list
        print("Your password is : ", pwd_fin)

while True:
    if userlen>2:
        pwd_gen()
        break
    else:
        print("Please enter length greater than 2")
        
        