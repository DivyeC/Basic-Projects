import random
print("""----------WELCOME TO NOTEBOOK MANAGER----------""")
while True:
    print("""MAIN MENU
1. Select Notebook I
2. Select Notebook II
3. Select Notebook III
4. Select a Random Notebook
5. Exit""")
    choice1=int(input("Enter your choice for selecting a notebook :"))
    def p1():
        if choice1 ==(1):
            print("--> Notebook I selected")
            f1=open("nb1.txt",'a+')
            while True:
                print("""
    1. Type notes
    2. Clear all notes
    3. Overwrite notes
    4. Show Notes
    5. Go back to Main Menu

    """)
                choice2=int(input("Enter choice from above :"))
                if choice2==1:
                    f1=open("nb1.txt",'a+')
                    input1=input("enter notes for Notebook I: ")
                    f1.write('\n')
                    f1.write(input1)
                    print('--> Notes Entered')
                    f1.close()
                elif choice2==2:
                    f1=open("nb1.txt",'w+')
                    a=""
                    f1.write(a)
                    print("--> Notes Cleared")
                elif choice2==3:
                    f1=open("nb1.txt",'w+')
                    input1=input("enter notes for overwritting in Notebook I: ")
                    f1.write(input1)
                    f1.close()
                    print("--> Notes Overwritten")
                elif choice2==4:
                    f1=open("nb1.txt",'r')
                    print("Notebook I Notes -->")
                    print(f1.read())
                elif choice2==5:
                    break
    def p2():            
        if choice1==2:
                print("--> Notebook II selected")
                f2=open("nb2.txt",'a+')
                while True:
                    print("""
    1. Type notes
    2. Clear all notes
    3. Overwrite notes
    4. Show Notes
    5. Go back to Main Menu

    """)
                    choice2=int(input("Enter choice from above :"))
                    if choice2==1:
                        f2=open("nb2.txt",'a+')
                        input1=input("enter notes for Notebook II: ")
                        f2.write('\n')
                        f2.write(input1)
                        print('--> Notes Entered')
                        f2.close()
                    elif choice2==2:
                        f2=open("nb2.txt",'w+')
                        a=""
                        f2.write(a)
                        print("--> Notes Cleared")
                    elif choice2==3:
                        f2=open("nb1.txt",'w+')
                        input1=input("enter notes for overwritting in Notebook II: ")
                        f2.write(input1)
                        f2.close()
                        print("--> Notes Overwritten")
                    elif choice2==4:
                        f2=open("nb2.txt",'r')
                        print("Notebook II Notes -->")
                        print(f2.read())
                    elif choice2==5:
                        break
    def p3():
        if choice1 ==(3):
            print("--> Notebook III selected")
            f1=open("nb3.txt",'a+')
            while True:
                print("""
    1. Type notes
    2. Clear all notes
    3. Overwrite notes
    4. Show Notes
    5. Go back to Main Menu

    """)
                choice2=int(input("Enter choice from above :"))
                if choice2==1:
                    f3=open("nb3.txt",'a+')
                    input1=input("enter notes for Notebook III: ")
                    f3.write('\n')
                    f3.write(input1)
                    print('--> Notes Entered')
                    f1.close()
                elif choice2==2:
                    f3=open("nb3.txt",'w+')
                    a=""
                    f3.write(a)
                    print("--> Notes Cleared")
                elif choice2==3:
                    f3=open("nb3.txt",'w+')
                    input1=input("enter notes for overwritting in Notebook III: ")
                    f3.write(input1)
                    f3.close()
                    print("--> Notes Overwritten")
                elif choice2==4:
                    f3=open("nb3.txt",'r')
                    print("Notebook III Notes -->")
                    print(f3.read())
                elif choice2==5:
                    break
    if choice1==1:
        p1()
    if choice1==2:
        p2()
    if choice1==3:
        p3()
    if choice1==4:
        x=random.randint(1,3)
        if x==1:
            choice1=1
            p1()
        if x==2:
            choice1=2
            p2()
        if x==3:
            choice1=3
            p3
            ()
    if  choice1==5:
        break
print('''---------Thanks for using Notebook manager---------
EXITING PROGRAM''')
