

print('*'*80)
print('*'*8)
print('\t''\t''CUSTOMER ORDER SYSTEM')
print('*'*80)
print('*'*8)


Name= input('Enter Your Full_Name:')
Phone_Number= input('Enter Your Phone_Number:')
Product= input('Enter  Product_Name:')
Quantity= int(input('Enter Quantity:'))
Item_Price= float(input('Price Per Item:'))
Discount= 10.00
Sub_Total= Quantity * Item_Price
Discount_Amount= Sub_Total * Discount/100

print('\n')
print('*'*80)
print('\t''\t''ORDER RECEIPT')
print('*'*80)

print('name:', Name .strip().title())
print('Phone_Number:',Phone_Number.strip())
print('\n')

print('Product:', Product.strip().title())
print('Quantity:', Quantity)
print("Item_Price:",Item_Price)
print('\n')

print('Discount:',Discount)
print('Discount_Amount:', Discount_Amount)
print('Sub_Total:',Sub_Total)
print('Final_Price:',Sub_Total - Discount_Amount )
print('\n')

print('Thanks for your purchase !')
print('*'*30)
print('*'*6)


