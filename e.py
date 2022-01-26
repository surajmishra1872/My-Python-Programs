#       resturent bill
##a=input("Enter the price 1:")
##b=input("Enter the price 2:")
##c=input("Enter the price 3:")
##tax_percent=input("Enter the tax %:")
##if "." in a or b or c or tax_percent:
##        a=float(a)
##        b=float(b)
##        c=float(c)
##        tax_percent=float(tax_percent)
##        product_price=a+b+c         
##        Tax_amount=tax_percent*product_price/100
##        Tax_amount=float(Tax_amount)
##        print(f"total price is :{Tax_amount+product_price}")
##        
##else:
##        a=int(a)
##        b=int(b)
##        c=int(c)
##        tax_percent=int(tax_percent)
##        product_price=a+b+c         
##        Tax_amount = tax_percent*product_price/100
##        Total=int(Tax_amount+product_price)
##        print(f"total price is :{Total}")

#weight and height converter

##a=input("Enter the height feet part:")
##b=input("Enter the height inch part:")
##c=input("Enter the weight in kg:")
##a=int(a)
##b=int(b)
##if "." in c:
##        c=float(c)
##else:
##        c=int(c)
##d=a*12
##height=d*2.54+b*2.54
##weight=round(c*2.2,1)
##print(f"Height in cm:{height}")
##print(f"Weight in pounds:{weight}")


#eval function:
##eval = eval(input("Enter any number of your choice"))
##print(eval)
##print(2+eval)

#chess quibe finder 1

##a=int(input("Enter the tray’s length:"))
##b=int(input("Enter the tray’s width:"))
##c=int(input("Enter the side of cube:"))
##areaoftray=a*b
##areaofcube=c*c
##cubes=int(areaoftray/areaofcube)
##print(f"Number of cubes:{cubes}")

#chess quibe finder 1
a=int(input("Enter the tray’s length:"))
b=int(input("Enter the tray’s width:"))
c=int(input("Enter the side of cube:"))
cubes=int(a/c)*int(b/c)
print(f"Number of cubes:{cubes}")



