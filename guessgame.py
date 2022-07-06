import random
import time

print("""Hi! there, I hope you are doing great.
WELCOME to the guessing game.
I am going to pick a number between 1 and 100""")

time.sleep(3)
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
    if guess<num:
        guess=int(input("guess the higher number"))
    if guess>num:
        guess=int(input("guess the lower number"))

#for right guess
print(f"CONGRATS! you guess the correct number {num}.you took {count}times to guess the number")
