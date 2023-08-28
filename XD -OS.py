import time
import os

print(""" 
██╗░░██╗██████╗░  ██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
╚██╗██╔╝██╔══██╗  ██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
░╚███╔╝░██║░░██║  ██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
░██╔██╗░██║░░██║  ██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
██╔╝╚██╗██████╔╝  ███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚═╝░░╚═╝╚═════╝░  ╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝
      """)
print("""
[1] continue with setup
[2] I've already done setup
      """)
setup = input("[?]: ")
if setup == '1':
     name = input(str("Please enter your User Name To Be Displayed: "))
     pas = input(str("Please enter your password to Login: ")) 

     with open('user/username.txt', 'w') as f:
        f.writelines(name)


     with open('user/password.txt', 'w') as f:
         f.writelines(pas) 
     print("Setup Complete!!!")
     input("Press Enter To Close Window")


if setup == '2':
   login_pass = open('user/password.pass')
   login_name = open('user/username.pass')
   l_p = login_pass.read()
   l_n = login_name.read() 


while True:
 login = input(str("Please Enter Your Password To " + l_n + ": ")) 
 if login == l_p:
      os.startfile("home.py")
      break
 else:
      print("wrong password!") 
