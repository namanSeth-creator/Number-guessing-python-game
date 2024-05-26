import random,math
n=input("Enter your name ")
print("Good luck",n)
a=int(input("Enter lower range of number "))
b=int(input("Enter upper range of number "))
x=random.randint(a,b) #to pick random number
n=0 #to count number of chances done by user
q=0 #for while loop to work
z=round(math.log(b-a+1,2)) #algorithm to calculate least number of chances user should have
print("You have only",z,"tries")
while q==0:
    c=int(input('Enter number '))
    if c==x:
        print("Correct answer !")
        n+=1
        q=1
    elif c>x:
        print("Number guessed is larger than the number I thought of")
        n+=1
    elif c<x:
        print("Number is smaller than the number I thought of")
        n+=1
if n>z:
    print("You correctly guessed the number in",n-z,"more tries")
elif n<z:
    print("You correctly guessed the number in",z-n,"less tries")
elif n==z:
    print("You correctly guessed the number in exactly",n,"tries, congo")

print('Thanks for playing the game. Have a good day',n)
