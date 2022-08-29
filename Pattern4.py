'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

row = int(input())
column = int(input())
for i in range(0,row):
    for j in range(0,i+1):
        print(i+1,end="")
    print()
