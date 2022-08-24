import random
from re import T
def preprint(word,list):
    for x in range(len(word)):
            if word[x] in list:
                print(word[x], end=" ")
            else:
                print("_", end=" ")
    print("")
keyword = ["dog","cat","banana","apple","tomato"]

password = random.choice(keyword)

set_pass = set(password)
know = []
health = 7
while set_pass != set(know):
    preprint(password, know)
    letter = input("choose letter:")
    if letter in password:
        know.append(letter)
    else:
        health -= 1
    if health == 0:
        print("looser")
        break 
    print(f"your hearts:{health}")
preprint(password, know)

