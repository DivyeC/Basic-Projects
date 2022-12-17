print("""------- LETS PLAY WITH WORDS--------""")
print("""1.TO EXTRACT 3 MIDDLE LETTERS FROM A STRING.
2.FOR FORMATING THE CASE OF A STRING.
3.SORT A STRING WITH LOWER CASE FIRST.
4.COUNT NUMBER OF ALPHABETS/NUMBERS/SYMBOLS IN A STRING.
5.CHECK WETHER A STRING CONTAINS ALL THE LETERS OF ANOTHER STRING.
6.EXIT
""")

choice = int(input("Enter your choice from options above :"))
while choice!=6:
    if choice == 1:
        sampleStr = input("Enter String Greater Than 4 Letters:")
        middleIndex = int(len(sampleStr) //2)
        print("Original String is", sampleStr)
        middleThree = sampleStr[middleIndex-1:middleIndex+2]
        print("Middle three charecters are", middleThree)

    if choice == 2:
        print("""-> ENTER 1 FOR UPPERCASE
-> ENTER 2 FOR LOWERCASE
-> ENTER 3 FOR TITLE""")
        option=int(input("Enter a choice from above :"))
        str1=input("enter string which is to be converted :")
        if option==1:
            print("new string is",str1.upper())
        elif option==2:
            print("new string is",str1.lower())
        elif option==3:
            print("new string is",str1.title())

    if choice ==3:
        str1=input("Enter string Which Is To Be Arranged :")
        lower = []
        upper = []
        for char in str1:
            if char.islower():
                lower.append(char)
            else:
                upper.append(char)
        sorted_string = ''.join(lower + upper)
        print("Sorted string ->")
        print(sorted_string)
    if  choice==4:
        str1=input("Enter string Which Is To Be Analysed :")
        charCount = 0
        digitCount = 0
        symbolCount = 0
        for char in str1:
            if char.islower() or char.isupper():
                    charCount+=1
            elif char.isnumeric():
                digitCount+=1
            else:
                symbolCount+=1
        print("total counts of Charecters, Digits,& Symbols ")      
        print("Chars = ", charCount, "    Digits = ", digitCount, "    Symbol = ", symbolCount)
    if choice==5:
        s1=input("Enter string 1 :")
        s2=input("Enter string 2 :")
        flag = True
        for char in s1:
            if char in s2:
                continue
            else:
                flag = False
        if flag==True:
            print("s2 contains all charecters of s1")
        else:
            print("s2 doesn't contains all charecters of s1")
            
    choice = int(input("Enter your choice from options above :"))
print("THANK YOU FOR USING THE PROGRAM!")



  



