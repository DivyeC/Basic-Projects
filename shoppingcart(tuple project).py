from random import shuffle
cart = ()

print("""
---------------SHOPPING BASKET OPTIONS-----------------

1. CREATE BASKET
2. INCREASE QUANTITY OF AN ITEM
2. VIEW BASKET
3. CHECK DISCOUNT
4. DELIVERY FEE
5. SEARCH BASKET
6. FIND QUANTITY OF AN ITEM
7. EXIT PROGRAM
""")
print("------------------------------")
option = int(input("enter an option :"))
print("------------------------------")


while option != 7:
    
    if option == 1:
        temp1 =input("ENTER ITEMS YOU WANT TO ADD (separated with commas :")
        temp2 = temp1.split(",")
        cart = tuple(temp2)

                     
    elif option==2:
            print(cart)
            print("we Have",len(cart),"items in cart")

            
    elif option==3:
        total=len(cart)
        if total>=10 and total<20:
            print("CONGRATULATIONS! YOU ARE AVAILING 10% DISCOUNT ON THIS ORDER")
        elif total>=20 and total<30:
            print("CONGRATULATIONS! YOU ARE AVAILING 20% DISCOUNT ON THIS ORDER")
        elif total>=30:
            print("CONGRATULATIONS! YOU ARE AVAILING 30% DISCOUNT ON THIS ORDER")
        elif total==0:
            print("OOPS!! .. YOU NEED TO CREATE A BASKET FIRST IN ORDER TO VIEW IT, KINDLY USE OPTION '1.' ")
        else :
            print("SORRY! DISCOUNT IS AVAILABLE ONLY ON 10 ITEMS AND ABOVE")

            
    elif option==4:
         total=0
         total=len(cart)
         if total>=10:
            print("CONGRATULATIONS! YOU ARE ELIGIBLE FOR FREE DELIVERY ON THIS ORDER")
         elif total==0:
            print("OOPS!! .. YOU NEED TO CREATE A BASKET FIRST IN ORDER TO CHECK DELIVERY FEE, KINDLY USE OPTION '1.' ")
         else:
            print("SORRY! YOU HAVE TO PAY ₹100 DELIVERY FEE AS FREE DELIVERY IS AVAILABLE ONLY ON 10 ITEMS AND ABOVE")

            
    elif option==5:
        term = input("Enter Item To Be Searched :")
        cnt=0
        for i in cart:
            if i == term:
                cnt+= 1
        if cnt>=1:
            print(term," Is Present In The Cart")
        else:
            print("OOPS! ",term," Isn't Present In The Cart")


    elif option==6:
        term = input("Enter Item To Be Counted :")
        cnt=0
        for i in cart:
            if i == term:
                cnt+= 1
        print("The Quantity of", term,"is",cnt)


    elif option != 7:
        print("please enter a valid input")
    print("------------------------------")
    option = int(input("enter an option :"))
    print("------------------------------")

    
else:
    print("THANK YOU FOR USING IT")
    print("Shopping Basket Program Closed")
