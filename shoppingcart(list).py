from random import shuffle
cart = []

print("""
---------------SHOPPING BASKET OPTIONS-----------------
1. ADD ITEM
2. REMOVE ITEM
3. VIEW BASKET
4. CHECK DISCOUNT
5. DELIVERY FEE
6. SHUFFLE BASKET
7. SEARCH BASKET
8. FIND QUANTITY OF AN ITEM
9. EXIT PROGRAM
""")
print("------------------------------")
option = int(input("enter an option :"))
print("------------------------------")
while option != 9:
    if option==1:
        name = input("Enter name of item :")
        q =int(input("Enter quantity of item :"))
        i=1
        while i <= q:
            cart.append(name)
            i+= 1
    elif option==2:
        name = input("Enter name of item which is to be deleted :")
        if name in cart:
            cart.remove(name)
            print("Your Updated Basket Is ->")
            print(cart)
        else:
            print("Entered Item Is Not Present In The Cart!")
    elif option==3:
            print(cart)
            print("we Have",len(cart),"items in cart")
    elif option==4:
        total=len(cart)
        if total>=10 and total<20:
            print("CONGRATULATIONS! YOU ARE AVAILING 10% DISCOUNT ON THIS ORDER")
        elif total>=20 and total<30:
            print("CONGRATULATIONS! YOU ARE AVAILING 20% DISCOUNT ON THIS ORDER")
        elif total>=30:
            print("CONGRATULATIONS! YOU ARE AVAILING 30% DISCOUNT ON THIS ORDER")
        else :
            print("SORRY! DISCOUNT IS AVAILABLE ONLY ON 10 ITEMS AND ABOVE")
    elif option==5:
         total=0
         total=len(cart)
         if total>=10:
            print("CONGRATULATIONS! YOU ARE ELIGIBLE FOR FREE DELIVERY ON THIS ORDER")
         else:
            print("SORRY! YOU HAVE TO PAY ₹100 DELIVERY FEE AS FREE DELIVERY IS AVAILABLE ONLY ON 10 ITEMS AND ABOVE")
    elif option==6:
        shuffle(cart)
        print("Your Shuffled Basket Is ->")
        print(cart)
    elif option==7:
        term = input("Enter Item To Be Searched :")
        cnt=0
        for i in cart:
            if i == term:
                cnt+= 1
        if cnt>=1:
            print(term," Is Present In The Cart")
        else:
            print("OOPS! ",term," Isn't Present In The Cart")
    elif option==8:
        term = input("Enter Item To Be Counted :")
        cnt=0
        for i in cart:
            if i == term:
                cnt+= 1
        print("The Quantity of", term,"is",cnt)
        
    elif option != 9:
        print("please enter a valid input")
    print("------------------------------")
    option = int(input("enter an option :"))
    print("------------------------------")
else:
    print("THANK YOU FOR USING IT")
    print("Shopping Basket Program Closed")
