#What are Data Tyes?
# Data Types tell us the type of values We Are working With.
         #TYpes Of Data Types
#1. integer (int)
#2. Strings (str)
#3. Boolean (bool)
#4. Float
#5. Dubble
#6. List
#7. Tuple 
#8. Dictionary (dict)
#9. None 

#Variables an data type Values
Name = "Benjamin Paul"
Height = 43.5
Age =  50
Calculate = 2+2
AreYouAStudent = True
Price_Shirt = None

print (Name)
print (Height)
print(Age)
print(Calculate)
print(AreYouAStudent)
print(Price_Shirt)
        #Checking our variables/DataType Using the (type)Funtion
print(type(Name))
print(type(Height))
print(type(Age))
print(type(Calculate))
print(type(AreYouAStudent))
print(type(Price_Shirt))

        #WORKING WITH STRINGS

# Convering INterger to String using (str) Method
print('Your Age is:'+str(Age))
Age= str(Age)
print(type(Age))

#converting String to interger
Age = int(Age)
print(type(Age))



# CONVERT THIS NUMBER T A CLEAN NUMBER "+49(176)12-4567"
         #the (replace)Method
Store = "+49(176)12-4567$09@89@678"
print(Store.replace("(", "")
      .replace("-", "")
      .replace("$", "")
      .replace("@", "")
      .replace(")", "")
      .replace("+", "00"))





#replace this 4729UBER876908 with Hope UYeh

value ="4729UBER876908"
print(value.replace("4729UBER876908", "HOPE UYEH"))





#Password
Password = input("Your Password:")

          #USing (Len) funtion
if len(Password)<10:
       print("Error Your Password Must be Up to 10 Characters")
       print(Password)

          #Math with Strings 

text = """ hope is learning python.
hope want to be good at backend development.
hope wish to get a good paying job.
hope pray t be successful in life.
hope wish for good things to locate her"""

           #the (count) Method
#How many times is hope appearing in my (text)
print(text.count("hope"))

#Srings (CONCATINATE) Funtion JOING 2 STRINGS VALUES TOGETHER
name= 'hope'
sur_name = 'uyeh'
birth_month = '2005_08_15'
job = 'pharmacy=remote+me+12987*0987'
complextion = 'darkskin'
occupation = 'studnt'
nationality = 'nigeria'
state_of_origin = 'akwa ibom'
age = 21

# USING THE PLUS OR (ADDITION)FUNTION CONCATINATION

print(name,''+'',sur_name)
print(" name is " + name  + " i am " + str(age) + " yrs old " + " i hail from " + state_of_origin + " i am " + complextion + " in complexion " + " i am a " + occupation)

#using the format funtion {f}to join diffrent strings together, 
# the sytax print(f "i am {variable}"). output= i am pretty.
#key nate: always put ur sring variables in a curly bracket{}
print(f" name is {name }, i am {age} yrs old, i hail from {state_of_origin}, i am {complextion} in complexion, i am a {occupation} " ".")
print(f"2+3= {2+3}")
print(f"{{my name is hope, i am 20yrs old, i reside in lagos, am from akwa ibom state}}")

#Spliting our CSV files with split Method
#keynote: split method can only split or seperate one split value at a time .
# e.g .split(-), it's best used when the file u want to split have same indictor, just like a (CSV) file

print(job.replace("=", "\n").replace("+", "\n").replace("*", "-"))
stamp="hope,john,faith,joy,imoh,akpan,ola"

print(stamp.replace(",", "\n"))

#How to get or extract a particular value from our string , by using indexing count.
#indexing start from "[0,2,3,4,5,6,7,8],an soon "
#the indexting also start from nagetive number from the left hand side 
# e.g "[-1,-2,-3,-4,-5,-6,-7,-8,-9], an soon". 
# remember ! the positive number start from the right while the nagetive number start from the left hand side.
#slicing value fumtion sytax print(value[2:6]) or ([-1:-8])

print('*'*80)
print('\t''CREATING NEW LIST OF NAMES FROM THE WORD, "COMMUNICATON VALUE"')
print('*'*80)
pay= "COMMUNICATING VALUE"
print(f"1:{pay[3]}{pay[-4]}{pay[5]}")
print(f"2:{pay[-5]}{pay[-4]}{pay[-3]}{pay[-9]}{pay[7]}{pay[8]}{pay[9]}{pay[-1]}")

print()

#using the fuctions an method have learn on (strings) to seperate, Extract values.

customer1='ID-100|miraAde|mira.ade@gmail.com|lagos-Nigeral|python,sql,fastapi,active'

customer2='ID - 002|davidjohn|.john@yahoo.com|abujah-nigeria|python,java,sql|inacive'
customer3= 'Zara'
customer4='David'
#funtion an Method used (print),(.replace),(upper) , indexing(1:2) an ('\n') for add space
print(customer1)
print('WEcome to Miras World'
      ,'\n',customer1.upper()
      .replace('-' , ':')
      .replace('|' , '\n')
      .replace(',' , '\n'),'\n'
      ,customer1[24:29],'\n'
      ,customer1[7:11],'\n',customer1[11:14],
      '\n',customer1[15:23])
print(customer2.upper()
      ,'\n',customer2.upper()
      , customer2.replace(',' , '\n')
      .replace('|' , '\n')
      .replace('-' , ',')
      .replace('.' ,'')
      .replace('oo', 'oo.'))

print(f'my name is {customer4} {customer3}')

comment= input('ur comment:')
if len (comment) >5:
    print('Error Not more than 5 Characters')
if len (comment) <2:
    print('nahhh')

print( 'Hello How Are You?' '\n'*3)


import math

price=344.9800
print(math.floor(price))
print(math.ceil(price))
print(math.sqrt(price))
print(math.pow(price, 2))
print(math.asin(price))
print(math.cos(price))
print(math.log(price))
print(math.trunc(price))
print(math.dist)

import random
print(random.randint(1, 100))
