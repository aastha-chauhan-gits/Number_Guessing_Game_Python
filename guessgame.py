#Number guessing game in python
import random
import time

print("""Hi! there, I hope you are doing great.
WELCOME to the NUMBER GUESSING GAME.
I am going to pick a number between 1 and 100.
You have to guess that number within 10 attempts.
GOOD LUCK! """)

time.sleep(2)
print("picking a number....")

#selecting random number
num=random.randint(1,100)

time.sleep(2)
#taking input for guess number
guess=int(input("What's your guess?: "))

count=0

#applying wrong guess condition
while guess!=num:
    count+=1
    if count==10:
        print("""You have finished your attempt limit.
Better Luck Next Time!""")
        break
    elif guess<num:
        guess=int(input("guess the higher number"))
    elif guess>num:
        guess=int(input("guess the lower number"))


#for right guess
if guess==num:
    print(f"CONGRATS! you guess the correct number {num}.you took {count + 1} times to guess the number")
