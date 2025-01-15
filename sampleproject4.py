# a=50
# git init  # library
# git add "file name"   git add .
# git commit -m "message"
#--------------------file hub -----------------
# github ----------------------
# pep

# if True :
#     body


# Password=input("enter your password:{}".format("____________"))

#                                               0         1
# print("username:{1} and password: {0}".format(UserName,Password))

# # print(f"username:{UserName} and password: {Password}")


# U="admin"

# P="1234"

# UserName=input("enter your username:"+" "*4)

# Password=input("enter your password:     ")

# if UserName==U and Password==P:
#     print("wellcome")
# else:
#     print("username or password Error")

# UserName=input("enter your username:"+" "*4)


# if UserName==U:
#     Password=input("enter your password:     ")
#     if Password==P:
#         print("wellcome")
#     else:
#         print("username or password Error")
# else:
#     print("username or password Error")


# 0 -3 >0
# 3- 7> 3
# 7-10>10
#10-15>1
#15>score


# score=float(input("enter your score:\t."))
# report=0

# # if score>0 and score<3:
# if 0<score<3:
#     report=0
# elif 3<=score<7:
#         # score=score+3
#     report=score+3
# elif 7<=score<10:
#     report=10
# elif 10<=score<15:
#     report=score+1
# elif 15<=score:
#     report=score
# else:
#     pass
# print(report)

# admin   #user   #guest

# userStat=input("enter username: ")

# if userStat=="admin":
#     pass
# elif userStat=="user":
#     pass
# elif userStat=="guest":
#     pass

# match userStat:
#     case "admin":
#         pass
#     case "user":
#         pass
#     case "guest":
#         pass
#     case _: #default
#         pass

# match userStat:
#     case "admin":
#         print("admin access")
#     case "user":
#         print("user access")

#     case "guest":
#         print("geust access")
        
#     case _: #default
#         print("No access")
        

# num1=int(input("enter first number: "))
# num2=int(input("enter second number: "))
# op=input("enter your command:")
# result=0
# match op:
#     case "+":
#         result=num1+num2
#     case "-":
#         result=num1-num2
#     case "*":
#         result=num1*num2
#     case "/":
#         result=num1/num2
#     case _:
#         print("not a valid oprator")

# print(f"{num1}{op}{num2}={result}")


# print("112321345".isdigit())
# print(type("112321345"))

# class a:
#     def clean(self):
#         pass


# a.clean()

# Money=1000
# Rat=1.20

# Y1=Money*Rat
# print(Y1)

# Y2=Y1*Rat
# print(Y2)

# Y3=Y2*Rat
# print(Y3)

# # # # # # # # # while
# # # # # # # # # for

# while condition :
#     body

# while True:
#     pass

# counter=1
# while counter<30:
#     Y1=Money*Rat
#     print(Y1)
#     Money=Y1
#     counter+=1

# counter=1
# while counter<=1000:
#     print(counter*5)
#     counter+=1

# Num=input("Enter the number=")#one three four
# match Num:
#     case "one":
#         print("Hello")
#     case "two":
#         c=0
#         while c<2:
#             print("Hello")
#             c+=1
#     case "three":
#         c=0
#         while c<3:
#             print("Hello")
#             c+=1
#     case "four":
#         c=0
#         while c<4:
#             print("Hello")
#             c+=1

#     012345
# text="Python"
# c=0
# while c<len(text):
#     print(text[c]+"*",end="")
#     c+=1

# name="bob"
# print(f"hello {name}")

# print("one",end=f"{chr(2665)}")
# print("two")

# 1:0,1
# 2:0,1,2
# 3:0,1,2,3
# .
# .
# .
# 10

# i=1
# while i<=10:
#     j=0
#     print(f"{i}",end=":")
#     while j<=i:
#         if i!=j:
#             print(f"{j}",end=",")
#         else:
#             print(f"{j}",end="")
#         j+=0.1
#     print()
#     i+=1

# text1="python"
# text2="so good"
# number=1934
# score=12.96789

# print(f"{text1}:{text2}",number,score)
# students=[{"name":"alice","score":"12,5"},
#          {"name":"davood","score":"23"},
#          {"name":"bob","score":"20"}]
# i=0
# while i<len(students):

#     print("{name}:{score}"
#           .format(name=students[i]["name"],score=students[i]["score"]))

#     i+=1

# "{}---{}---{}---{}".format(1,2,3,4)
# print("{3}---{3}---{3}---{3}".format(1,2,890,45235))
# okscore=12
# topscore=20
# print("{_4}---{_1}---{_2}---{_3}".format(_1=1,_2=2,_3=okscore,_4=topscore))


# data={
#   "$id": "https://example.com/person.schema.json",
#   "$schema": "https://json-schema.org/draft/2020-12/schema",
#   "title": "Person",
#   "type": "object",
#   "properties": {
#     "firstName": {
#       "type": "string",
#       "description": "The person's first name."
#     },
#     "lastName": {
#       "type": "string",
#       "description": "The person's last name."
#     },
#     "age": {
#       "description": "Age in years which must be equal to or greater than zero.",
#       "type": "integer",
#       "minimum": 0
#     }
#   }
# }

# print(data["properties"]["age"]["description"])

# text1="python"
# text2="so good"
# number=1934
# score=12.96789

# # output="%7.20f"%score
# output="%20s"%text1
# print(output)

#bool (0 False null None "") ----->False

# while i:=int(input("enter a number: ")):
#     print("less")


# break           close
# continue
# pass
# return
# yield

# while True:
#     i=input("enter any number to persume or nothing to exit: ")
#     if i==False or i==None or i=="":
#         break
#     else:
#         print("another try: ")


# i=0
# while i<100:
#     if i%2==0:
#         print(i)
#     else:
#         i+=1
#         continue
#     i+=1


# i=-1
# while i<100:
#     i+=1
#     if i%2==0:
#         print(i)
#     else:     
#         continue
# answer=int(input("answer of the turn: "))

# while True:
#     i=input("enter any number to persume or nothing to exit: ")
#     if i==False or i==None or i=="":
#         break
#     i=int(i)
#     if i>answer:
#         print("guess less")
#     elif i<answer:
#         print("guess more")
#     else:
#         print("ok")
#         break


# i=0

# while i<5:
#     print(i)
#     i+=1
# else:
#     print("reach")


# i=10

# if i<20:
#     print(True)
# else:
#     print(False)

# print(True) if i<20 else print(False)


# if () {
#     command;
# }


# for counter in object:
#     body


# text="python"

# for alireza in text:
#     print(alireza)


# numbers="123456789"

# for i in numbers:
#     print(i)

# range(start,stop,step)

# R=range(1,10,1)
# print(list(R))

# for r in R:
#     print(r)

# s=""
# for i in range(10):
#     s=s+str(i)
# print(s)

s=""
for i in range(ord("A"),ord("Z")+1):
    s+=chr(i)
print(s)