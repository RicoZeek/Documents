# python practice problems: https://www.practicepython.org/

import random


# EXERCISE 1: Character Input
# Name = input("what is your name?:")
# Age = int(input("What is your age?:"))

def what_year(name, age, copies):
    year = (100 - age) + 2023
    sent = f"Hello {name} you will be 100 in {year} \n"
    terminal = copies * sent
    print(terminal)


# EXERCISE 2: odd or even

# number = int(input("Give me a random number:"))
# divider = int(input("Give me another number to divide it by:"))
def num_div(num, div):
    if num % 4 == 0:
        print("this number is a multiple of four")
    elif num % 2 == 0:
        print("this number is even")
    else:
        print("this number is odd")
    if num % div == 0:
        print(f"{num} is dividable by {div}!")
    else:
        print(f"{num} is NOT dividable by {div}!")


# EXERCISE 3 return values less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
rest_num = int(input("give me a number:"))


def less_than_rest_num(my_list, num):
    new_list = []
    for i in my_list:
        if i < num:
            new_list.append(i)
    print(new_list)


# write it in one line with filter() function
oneLine = filter(lambda i: i < 5, a)

print(oneLine)
less_than_rest_num(a, rest_num)

# EXERCISE 4: Divisor

dividend = int(input(" Lets find the divisors for: "))


def divisor(div):
    actual_dividends = []
    # we make the list start with 1 to avoid an error
    divisors = list(range(1, div + 1))
    for x in divisors:
        if div % x == 0:
            actual_dividends.append(x)

    print(actual_dividends)


divisor(dividend)

# Exercise 5: List Overlap
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def list_overlap(list_a, list_b):
    c = []
    d = []
    # finding similar items
    for x in list_a:
        if x in list_b:
            c.append(x)
    # remove duplicates
    for i in c:
        if i not in d:
            d.append(i)
    print(d)


list_overlap(a, b)

# ONE LINER
print([num for num in b if num in a])

# Exercise 6: String lists

sentence = input("give me a something:")


def is_palindrome(str):
    rev = str[::-1]
    if str[:] == rev[:]:
        print("the string is a palindrome")
    else:
        print("The string is not a palindrome")


is_palindrome(sentence)

# Exercise 7: List comprehension
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list_c = []


def even_list(list_a):
    list_b = []
    for i in list_a:
        if i % 2 == 0:
            list_b.append(i)
    print(list_b)


even_list(a)

# One Liner
print([i for i in a if i % 2 == 0])

# exercise 8: Rock paper scissors
print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')

# exercise 9:


user = int(input("guess a number between 1 and 9:"))
rand = random.randint(1, 10)

if user == rand:
    print("exactly wight!")
elif user <= rand:
    print("too low")
elif user >= rand:
    print("too high")

print(rand)

# exercise 10: list overlap comprehension

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# exercise 11
# find prime numbers

def divisor(div):
    actual_dividends = []
    # we make the list start with 1 to avoid an error
    divisors = list(range(1, div + 1))
    for x in divisors:
        if div % x == 0:
            actual_dividends.append(x)
    return actual_dividends


dividend = 45


def find_prime(div):
    not_prime = True
    div_list = divisor(div)
    if len(div_list) < 3:
        print(f"{div} is a prime")
    else:
        print(f"{div} is not a prime")


# exercise 12
a = [5, 10, 15, 20, 25]


def first_last(list):
    list1 = list[0]
    list2 = list[-1]
    new_list = []
    new_list.append(list1)
    new_list.append(list2)
    return new_list


# exercise 13
int = []


def fibonacci(int):
    fib = []
    i = 1
    if int == 0:
        fib = []
    elif int == 1:
        fib = [1]
    elif int == 2:
        fib = [1, 1]
    elif int > 3:
        fib = [1, 1]
        while i < (int - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1
    return fib


# exercise 14

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def remove_dupli(list_a, list_b):
    d = []
    c = []
    for x in list_a:
        if x in list_b:
            c.append(x)
    # remove duplicates
    for i in c:
        if i not in d:
            d.append(i)
    return (d)


print(remove_dupli(a, b))


# exercise 15

def reverse_string(x):
    y = x.split()
    y.reverse()
    return " ".join(y)


# exercise 16 generate random password:

import random

user = input("how strong do you want your password?")
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
sym = ['!', ',', '*', '$', '&']
num = ["1", "2", "3", "4", "5"]


def gen_pass(user):
    password = []
    if user == "weak":
        while len(password) < 4:
            password.append(random.choice(num))
            password.append(random.choice(abc))
            password.append(random.choice(sym))
    elif user == "strong":
        while len(password) < 12:
            password.append(random.choice(num))
            password.append(random.choice(abc))
            password.append(random.choice(sym))
    random.shuffle(password)
    password = "".join(password)
    return password


def list_overlap(list_a, list_b):
    c = []
    d = []
    # finding similar items
    for x in list_a:
        if x in list_b:
            c.append(x)
    # remove duplicates
    for i in c:
        if i not in d:
            d.append(i)
    return d


print(list_overlap(a, b))

# exercise 17

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

for link in soup.find_all('h3'):
    print(link.text)
# or

page = "https://www.nytimes.com/"
url = requests.get(page)
result = url.content
soup = BeautifulSoup(url.text, 'lxml')
titles2 = soup.find_all("h3", {"class": "css-codfme e1lsht870"}, {"size": "200"})
titles1 = soup.find_all("h3", {"class": "css-xxaj7r e1lsht870"}, {"size": "400"})
titles = titles1 + titles2
for titel in titles:
    print(f'{titel.text}\n')

# exercise 18:


# exercise 19:
url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

for link in soup.find_all('p'):
    print(link.text)

# exercise 20 :


a = [1, 3, 5, 30, 42, 43, 500]


def ask_num(a):
    user = int(input("Number?"))
    if user in a:
        print(f"{user} in list!")
    else:
        print(f"{user} not in list")


# Exercise 21

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')

filename = input("File to save to: ")

with open(filename + ".txt", 'w') as f:
    for link in soup.find_all('h3'):
        f.write(link.text)

# exercise 22

counter_dict = {}
with open("C:/Users/zamca/OneDrive/Documents/pythontxt.txt") as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line = f.readline()

print(counter_dict)


# Exerxise 23

def filetolistofints(filename):
    list_to_return = []
    with open(filename) as f:
        line = f.readline()
        while line:
            list_to_return.append(int(line))
            line = f.readline()
    return list_to_return


primeslist = filetolistofints('primenumbers.txt')
happieslist = filetolistofints('happynumbers.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)

# Exercise 24
# we use the solution from exercise 17
# this will be the text you will be importing

grid_count = int(input("How many square grids do you want? "))
cool = grid_count + 1

horizontal = " ---"
vertical = "|   "

i = 0

while i < grid_count:
    print(horizontal * grid_count)
    print(vertical * cool)
    i +=1

print(horizontal * grid_count)

# 25 Guessing game two:
import random as rd

def guess():
    correct = False
    num = rd.randint(0,100)
    while correct == False:
        print(num)
        ques = input("was the number correct?")
        if ques == "no":
            ran = input("was the number too low or high")
        else:
            correct = True
        if ran == "low":
            num = rd.randint(num, 100)
        elif ran == "high":
            num = rd.randint(0, num)

# Exercise 26 check tic tact toe
import numpy as np

game = np.array([[9, 5, 7], [6, 1, 7], [4, 2, 3]])

tH = game[0]
mH = game[1]
bH = game[2]

lC = game[0, 0], game[1, 0], game[2, 0]
mC = game[0, 1], game[1, 1], game[2, 1]
rC = game[0, 2], game[1, 2], game[2, 2]

lD = game[0, 0], game[1, 1], game[2, 2]
rD = game[0, 2], game[1, 1], game[2, 0]
game_over = False
while game_over == False:
    print(game)
    if sum(tH) == 3 or sum(mH) == 3 or sum(bH) == 3:
        print("user1 win!")
        game_over == True
    elif sum(lC) == 3 or sum(mC) == 3 or sum(rC) == 3:
        print("user1 win!")
        game_over = True
    elif sum(rD) == 3 or sum(lD) == 3:
        print("user1 win!")
        game_over = True
    elif sum(tH) == 6 or sum(mH) == 6 or sum(bH) == 6:
        print("user2 win!")
        game_over = True
    elif sum(lC) == 6 or sum(mC) == 6 or sum(rC) == 6:
        print("user2 win!")
        game_over = True
    elif sum(rD) == 6 or sum(lD) == 6:
        print("user2 win!")
        game_over = True
    else:
        print("No one wins")
        game_over = True

# Exercise 27 get user input


# exercise 28
def max_num(n1, n2, n3):
    current = n1
    if n2 > current:
        current = n2
    if n3 > current:
        current = n3
    print(current)

max_num(2,1,4)
