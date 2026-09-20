
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
