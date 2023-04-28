# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LikXzJTq1x2TgQIEcQ1l3E3ufIswsc4c
"""

import time
import os

def wait(sec):
    end_wait = time.time() + sec
    while time.time() < end_wait:
        pass

def design1():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n\t\t\t         TALENT\n")
    print("\t\t\t        EXPLORER")
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

def res(i):
  os.system('cls' if os.name == 'nt' else 'clear')
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("\n\t\t\t         TALENT\n")
  print("\t\t\t        EXPLORER")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("\n\n\t\t\tSorry, Your Answer Is Wrong!!!\n\n\t\t\tYOU ARE OUT OF THE GAME")
  a=(i+1)*1000
  print("\n\n\t\t\t YOU WON CASH OF",a)
  print("\n\n\t\t\t\t  ENJOY!!!")
def reswon(i):
  os.system('cls' if os.name == 'nt' else 'clear')
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("\n\t\t\t         TALENT\n")
  print("\t\t\t        EXPLORER")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("\n\n\t\t\tAll the Answer Are Wright!!!\n\n\t\t\tYOU ARE WINNER OF THE GAME ")
  a=(i+1)*1000
  print("\n\n\t\t\t YOU WON CASH OF",a)
  print("\n\n\t\t\t\t  ENJOY!!!")


class ques:
    def __init__(self, question, optiona, optionb, optionc, optiond, correct, half1, half2, halfans, clue, audience1, audience2, audience3, audience4):
        self.question = question
        self.optiona = optiona
        self.optionb = optionb
        self.optionc = optionc
        self.optiond = optiond
        self.correct = correct
        self.half1 = half1
        self.half2 = half2
        self.halfans = halfans
        self.clue = clue
        self.audience1 = audience1
        self.audience2 = audience2
        self.audience3 = audience3
        self.audience4 = audience4
q = [] # initialize empty list for questions
half = 0
clue_ = 0
audience = 0
name = input("\n\t    ENTER YOUR NAME: ")
status = input("\n ENTER YOUR SCHOOL/COLLEGE NAME: ")
district = input("\n\t ENTER YOUR DISTRICT NAME: ")
# half = 0
# clue = 0
# audience = 0
print("\n\n\t\tHearty Welcome To: TALENT EXPLORER GAME SHOW!\n\n\t\t\tWait For Few Seconds!!\n\n\t\t\tTo Know About This Game!!!")
time.sleep(2)

print("About this game:")
print("\t1. TOTALLY THIS GAME HAVING 15 QUESTIONS......")
print("\t2. EACH QUESTIONS HAVE 4 OPTIONS......")
print("\t3. PRESS '5' TO USE 50-50 OPTION......")
print("\t4. PRESS '6' TO KNOW CLUE FOR THAT QUESTION......")
print("\t5. PRESS '7' TO RECEIVE AUDIENCE REPORT......")
print("\n\tRULES:")
print("\t1. ALL THE LIFE LINES ARE USE ONLY ONE TIME......")
print("\t2. IF YOU ANSWERED WRONG, YOU WILL BE OUT OF THE GAME......")
print("\n\t\t\t\t GET READY!!!")
with open('/content/question.txt', 'r') as fp:
  for i in range(15):
    question = fp.readline().rstrip()
    optiona = fp.readline().rstrip()
    optionb = fp.readline().rstrip()
    optionc = fp.readline().rstrip()
    optiond = fp.readline().rstrip()
    correct = int(fp.readline().rstrip())
    half1 = fp.readline().rstrip()
    half2 = fp.readline().rstrip()
    halfans = int(fp.readline().rstrip())
    clue = fp.readline().rstrip()
    audience1 = fp.readline().rstrip()
    audience2 = fp.readline().rstrip()
    audience3 = fp.readline().rstrip()
    audience4 = fp.readline().rstrip()
    q.append(ques(question, optiona, optionb, optionc, optiond, correct, half1, half2, halfans, clue, audience1, audience2, audience3, audience4))

for i in range(15):
    # clear the screen
    os.system('cls')

    # display the design based on the current question number
    design1()

    # display the question and options
    print(f"\n\n\t\t\t       QUESTIONS No.{i+1} :")
    print(q[i].question)
    print(f"\nOPTIONS:1.){q[i].optiona} 2.){q[i].optionb} 3.){q[i].optionc} 4.){q[i].optiond}")
    a = int(input("\n\t ANSWER: "))

    # check if the answer is correct, or if the 50-50 or clue options have been used
    if q[i].correct == a:
        pass
    elif a == 5:
        if half == 0:
            print("\n\t50-50 OPTIONS:")
            print("\n\nOPTIONS:1.)%s\t 2.)%s" % (q[i].half1, q[i].half2))
            print("\n\n\t ANSWER: ")
            b = int(input())
            if b == q[i].halfans:
                half = 1
            else:
                res(i)
                break
        else:
            print("\n\t\tSorry,You Already Used This Option ")
            print("\nOPTIONS:1.)%s\t2.)%s  3.)%s  4.)%s" % (q[i].optiona, q[i].optionb, q[i].optionc, q[i].optiond))
            print("\n\n\t ANSWER: ")
            b = int(input())
            if b == q[i].correct:
                pass
            else:
                break
    elif a == 6:
      if clue_ == 0:
        print("\n\tCLUE: %s" % q[i].clue)
        print("\nOPTIONS:1.)%s\t2.)%s  3.)%s  4.)%s" % (q[i].optiona, q[i].optionb, q[i].optionc, q[i].optiond))
        print("\n\n\t ANSWER: ")
        b = int(input())
        if b == q[i].correct:
            clue_ = 1
        else:
            res(i)
            break
      else:
          print("\n\t\tSorry,You Already Used This Option ")
          print("\nOPTIONS:1.)%s\t2.)%s  3.)%s  4.)%s" % (q[i].optiona, q[i].optionb, q[i].optionc, q[i].optiond))
          print("\n\n\t ANSWER: ")
          b = int(input())
          if b == q[i].correct:
              pass
          else:
            res(i)
            break
              
    elif a == 7:
        if audience == 0:
            print("\n\tAUDIENCE REPORT:")
            print("\n\nOPTIONS:1.)%s%s\t 2.)%s%s\t3.)%s%s\t 4.)%s%s" % (q[i].optiona, q[i].audience1, q[i].optionb, q[i].audience2, q[i].optionc, q[i].audience3, q[i].optiond, q[i].audience4))
            print("\n\n\t ANSWER: ")
            b = int(input())
            if b == q[i].correct:
                audience = 1
            else:
                res(i)
                break
        else:
            print("\n\t\tSorry, You Already Used This Option ")
            print(f"\nOPTIONS:1.){q[i].optiona}\t2.){q[i].optionb} 3.){q[i].optionc} 4.){q[i].optiond}")
            b = int(input("\n\n\t ANSWER: "))
            if b == 4:
                pass
            else:
                res(i)
                break
    else:
      print("please press the correct option")
    if(i==14):
        reswon(i)
        break
    
# except Exception as e:
#     print("Error: ", str(e))
#     sys.exit()
with open("data.txt", "a+") as fpout:
    fpout.write("\nNAME: " + name)
    fpout.write("\nSCHOOL/COLLEGE NAME: " + status)
    fpout.write("\nDISTRICT NAME: " + district)
    fpout.write("\nANSWERED QUESTIONS: " + str(i))
    fpout.close()
    fp.close()
        # input("Press any key to exit")





