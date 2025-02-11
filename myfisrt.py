# # program asks for name 
# print("Hello")
# print("Write your name ")
# print()
# name_user=input()
# print(" Your name is " + name_user )
# lenght_name= len(name_user)
# print(' lenth of your name is : ' + str(int(lenght_name)) )
# print(" what is your age ")
# age_user=input()
# print("Your age is "+ str(int(age_user)+1) + " next year ")
# -----------------------------------if and input------------------------------------ 
# print("Hello, hope you are doing well")
# print("Enter Username")
# user_name=input() 
# if user_name=="Ahmed":
#     print("Enter Password")
#     user_pass=input()
#     if user_pass== "ahmedali":
#         print("Access granted")
#     else:
#         print("Wrong Password")
# else: 
#     print("Wrong Username")
# ----------------------------If and elif and boolean-----------------------------------
# welcome message
# print("Hello, hope you are doing well")
# #User enter his name
# print("Enter Username")
# user_name=input()
# # user enter password 
# print("Enter Password")
# pass_word=input()
# if user_name=="ahmed" and pass_word=="ahmedali":
#     print(" Welcome "+user_name)
# elif user_name=="ganna" and pass_word=='gannaheeba':
#     print("Welcome "+user_name)
# else:
#     print("Access denied")
# -----------------------If and elif-----------------------------------------
# welcome message
# print("Hello,Please enter username")
# user_name=input()
# if user_name=="ahmed":
#     print("Enter your password,"+user_name)
#     pass_word=input()
#     if pass_word=="12345678":
#         print("Welcome "+ user_name)
#     else:
#         print("Wrong Password")
# elif user_name=="ganna":
#     print("Enter your password,"+user_name)
#     pass_word=input()
#     if pass_word=="2468":
#         print("Welcome "+ user_name)
#     else:
#         print("Wrong Password")
# else:
#     print("User is not registered")
# -----------------------While Loop------------------------------------------------
# print("Hello,Please enter username")
# user_name=input()
# while user_name!="ahmed":
#     print("Wrong!,please enter username")
#     user_name=input()
# print("Enter your password, "+ user_name)
# pass_word=input()
# while pass_word!="123456789":
#     print("Wrong password, "+ user_name)
#     pass_word=input()
# print("Welcome "+user_name)
# -----------------------For LOOPS--------------------------
# total = 0
# for num in range(101):
#     total=total+num
# print(total)
# ##-------------------------------Chapter 3 ----------------------------------###  
# def hello():
#     print("hello")
#     print("Howdy")
#     print("what is your name")
# hello()
# ---------------------------------------------------------------
# def hello(name):
#     print("Hello " + name)
#     print("HOW are you, "+ name)
# hello("ahmed")
# ------------------------------------------------
# import random as rd
# def opponent(move):
#     if move==1:
#         return "Rock"
#     elif move==2:
#         return "Paper"
#     elif move==3:
#         return "Scissors"
# r=rd.randint(1,3)
# move=opponent(r)
# print(move)
# --------------------------------------------------------------------------
# print(type(None))
# ------------------------------------------------------
# print("hello","ahmed","ali","ganna","manar",sep=",")
# ----------------------------------------------------------
# def ahmed():
#     print("ahmed start")
#     ali()
#     mohamed()
#     print("ahmeed returns")
# def ali():
#     print("ali start")
#     mostafa()
#     print("ali returns")
# def mostafa():
#     print('mostafa start')
#     print('mostafa returns')
# def mohamed():
#     print('mohamed starts')
#     print('mohamed returns')
# ahmed()
# -------------------------------------------------
# def spam():
#     eggs=337
# spam()
# print(eggs) #error
# --------------------------------------------------------
# def spam():
#     eggs=998
#     bacon()
#     print(eggs)
# def bacon():
#     ham=101
#     eggs=-0    
# spam() #998
# --------------------------------------------------------------
# def spam():
#     print(eggs)
# eggs=42
# spam()
# print(eggs) #42
# ---------------------------------------------------------------------
# def spam():
#     eggs='spam local'
#     print(eggs)
# def bacon():
#     eggs='local bacon'
#     print(eggs)
#     spam()
#     print(eggs)
# eggs='global'
# bacon()
# print(eggs)  
# #local bacon
# # spam local
# # local bacon
# # global
# -------------------------------------------------
# def spam():
#     global eggs 
#     eggs='spam'
# eggs='global'
# spam()
# print(eggs) #spam
# def trial(one_trial):
#     return 100/one_trial
# try:
#     print(trial(10))
#     print(trial(1))
#     print(trial(15))
#     print(trial(0))
#     print(trial(20))
# except ZeroDivisionError:
#     print('ERROR')
# --------------------------------------------------------
# def trial(one_trial):
#     try:
#         return 100/one_trial
#     except ZeroDivisionError:
#         print("Error")
# print(trial(10))
# print(trial(1))
# print(trial(15))
# print(trial(0))
# print(trial(20))
# ---------------------------------------------------------
# import time
# import sys
# space=0
# space_increasing=True
# try:
#     while True:
#         print(" "*space,"********")
#         time.sleep(.1)
#         if space_increasing:
#             space=space+1
#             if space==20:
#                 space_increasing=False
#         else:
#             space=space-1
#             if space==0:
#                 space_increasing=True
# except KeyboardInterrupt:
#     sys.exit()
# -----------------------------------------------
# import sys
# def collatz(number):
#     if number%2==0:
#         return number//2
#     else:
#         return (number*3)+1
# try:
#     while True:
#         print("Enter number")
#         response=input()
#         x=collatz(int(response))
#         print(x) 
#         if x==1:
#             sys.exit()
# except ValueError:
#     print("You must enter an integer")
##---------------------------------------##Chapter 4##--------------------------------------##    
# spam=[14,15,16,17,18,17]
# print(spam[1])
# print(spam[-4])
# print(spam[1:4])
# print(spam[1:])
# print(spam[:])
# spam[1]=22
# print(spam[0:-1])
# ---------------------------------------------
# spam=[1,32,5,96,658,9,5498] + [14,15,126,215,25,22]
# del spam[1]
# print(spam)
# --------------------------------------------------------
# cat_names=[]
# while True:
#     print('Enter the name of cat '+ str(len(cat_names)+1))
#     name=input()
#     if name=='':
#         break
#     elif name=='delete':
#         del cat_names[:]
#         print('cats are deleted')
#     else:
#         cat_names=cat_names+[name]
# print("the cat name are:")
# for name in cat_names:
#     print(name)
# --------------------------------------------------------
# spam=[0,1,23,3,56,59,6,9]
# for name in spam:
#     print(name)
# ---------------------------------------
# supply=['pens','man','so','kjh','ks','sdw','dsdrew']
# for i in range(len(supply)):
#     print("index",str(i),'in suuplies is',supply[i])
# ------------------------------------------------------
# spam=['ali','moug','015','5646']
# if 'moug' in spam:
#     print("hi")
# -----------------------------------------------------------------------
# mypets=['cat','mat','pat','dog','lion']
# print('please type a pet name')
# name=input()
# if name in mypets:
#     print(name,'is my pet')
# else:
#     print('I dont have a pet called',name)
# --------------------------------------------------------------------
# size,color,namr=14,'blue','ahmed'
# print(size)
# -------------------------------------
# [ahmed,name,size]=['ali','ahmed',14]
# print(ahmed)
# --------------------------------------
# supply=['ahmed','ali','mohamed','aliu8i','r;lkigj','rtg','dfhjy','ytre6','ety','hf','hdr','jyrf']
# for index,item in enumerate(supply):
#     print(index,item)
# -------------------------------------------------------------------------------
# import random as rd
# supply=['ahmed','ali','mohamed','aliu8i','r;lkigj','rtg','dfhjy','ytre6','ety','hf','hdr','jyrf']
# print(rd.choice(supply))
# rd.shuffle(supply)
# print(supply)
# ------------------------------------------------------
# spam=24
# spam%=5
# print(spam) 
# -------------------------------------------
# supply=['ahmed','ali','mohamed','aliu8i','r;lkigj','rtg','dfhjy','ytre6','ety','hf','hdr','jyrf']
# print(supply.index('rtg'))
# ---------------------------------------------------
# supply=['ahmed','ali','mohamed','aliu8i','r;lkigj','rtg','dfhjy','ytre6','ety','hf','hdr','jyrf']
# supply.append("mostafa")
# supply.insert(4,125)
# supply.remove(125)
# supply.sort()
# supply.sort(reverse=True)
# print(supply)
# ---------------------------------------------------------
# supply=['J','A','F','B','E','f','x','c','j']
# supply.sort()
# print(supply)
# --------------------------------------------------------------------
# supply=['J','A','F','B','E','f','x','c','j']
# supply.sort(key=str.upper)
# print(supply)
# ----------------------------------------------
# import random
# messages = ['It is certain',
#     'It is decidedly so',
#     'Yes definitely',
#     'Reply hazy try again',
#     'Ask again later',
#     'Concentrate and ask again',
#     'My reply is no',
#     'Outlook not so good',
#     'Very doubtful']
# print(messages[random.randint(0, len(messages) - 1)])
# ----------------------------------------------------------
# name='zophie'
# print(name[0])
# print(name[-2])
# print(name[0:4])
# print('zo' in name)
# for i in name:
#     print('*******',i,'********')

