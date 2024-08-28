#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Password  = ""

# for _ in range(0,nr_letters):
#   char = random.choice(letters)
#   Password += f"{char}"
# for _ in range (0,nr_symbols):
#   symb = random.choice(symbols)
#   Password += f"{symb}"
# for _ in range (0,nr_numbers):
#   num = random.choice(numbers)
#   Password += f"{num}"
# print(Password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

Password  = []

for _ in range(0,nr_letters):
  Password.append(random.choice(letters))
for _ in range (0,nr_symbols):
  Password.append(random.choice(symbols))
for _ in range (0,nr_numbers):
  Password.append(random.choice(numbers))
psw = ''.join([a for a in Password])
print(psw)