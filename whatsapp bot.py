import pyautogui as spam
import time
limit=int(input("enter no of messages:"))
msg=input("enter the message:")

i=0
time.sleep(2)
while i<int(limit):
    spam.typewrite(msg)
    spam.press('enter')
    i+=1
    
