# coder by fthsec 
# strong password generetor 


import time 
import pyfiglet 
import string 
import random 

print("---------Starting Programm--------")
time.sleep(5)

image_line = pyfiglet.figlet_format("SPG")
print(image_line)


char = "Q@@WQ!!@@@ÜQ!ğ!@@!E@@z!!xA" 



length = int(input("length= "))

print("password genretor..........")
time.sleep(5)

print("|")
print("|")
print("|")

print("-------------------------------------")


password_line = "".join(random.sample(char, length))
print(password_line)


password_line_2 = "".join(random.sample(char, length))
print(password_line_2)

password_line_3 = "".join(random.sample(char, length))
print(password_line_3)


password_line_4 = "".join(random.sample(char, length))
print(password_line_4)

password_line_5 = "".join(random.sample(char, length))
print(password_line_5)


image_line_2 = pyfiglet.figlet_format("finish")
print(image_line_2)

time.sleep(5)


exit()

