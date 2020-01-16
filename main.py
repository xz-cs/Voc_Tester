# Vocabulary Tester 1.0
# Created By Zhang Xun at Jan 16 2020 with IDLE
# © 2020 Zhang Xun. All Rights Reserved.


import random

print("Welcome to use the Vocabulary Tester 1.0!")

#mode choice
mode=input("\nMode 1: English Test\nMode 2: Chinese Test\nPlease Choose one: ")
while(mode!="1" and mode!="2"):
  mode=input("Please input 1 or 2: ")


#note
print("\nNote 1: If you want to stop the test in the middle, simply input '#' !")
if(mode=="1"):
  print("Note 2: In this mode, upper and lower case numbers are regarded as the same!\n")
else:
  print("Note 2: In this mode, you can input whichever Chinese translation you set before!\n")

#file handling
f=open("source.txt","r") #open the file
src=[] #create an array
for line in f:
  src.append(line.replace("\n","")) #fill the array with file contents
f.close()


#main test
score,total=0,0
for i in range(len(src)):
  Str=random.choice(src)             #choose an element randomly
  src.remove(Str)                    #remove the element from src
  en=Str.split(":")[0]               #get the English word
  cn=Str.split(":")[1].split("/")    #get its Chinese translation
  if(mode=="1"):
    ans=input(random.choice(cn)+": ")
    if(ans.lower()==en.lower()):
      print("Well done!\n")
      score+=1
      total+=1
    elif(ans=="#"):
      break
    else:
      print("Sorry, wrong answer!\n")
      total+=1
  else:
    ans=input(en+": ")
    if(ans in cn):
      print("Well done!\n")
      score+=1
      total+=1
    elif(ans=="#"):
      break
    else:
      print("Sorry, wrong answer!\n")
      total+=1


#test result
try:
  print("\nRight answer(s): {}\nWrong answer(s): {}\nGrade: {} %\n".format(score,total-score,(score/total)*100))
except:
  print("\nYou haven't did the test!\n")
