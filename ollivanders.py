https://replit.com/join/wcvlloramu-ana-lucialuc103

client = input("Does a client come in? ")
clientn = 0
buy_number = 0
which = 0
bought = []
HawthornWand = 0
WillowWand = 0
ElderWand = 0
HollyWand = 0

while client == "yes":
  clientn += 1
  buy = input("Buy something? ")
  if buy == "yes":
    buy_number += 1 
    list = ["1. Elder Wand", "2. Hawthorn Wand", "3. Willow Wand", "and 4. Holly Wand"]
    print (list)
    which = int(input("Which wand did they buy? (1, 2, 3, 4) "))
    if which == 1:
      ElderWand += 1
    if which == 2:
      HawthornWand += 1
    if which == 3:
      WillowWand += 1
    if which == 4:
      HollyWand += 1
  client = input("Does a client come in? ")
  

print (f"The customers who came in where: {clientn}")
print (f"The customers who bought something where: {buy_number}")
print(f"The wands that were bought were: {ElderWand}, {HawthornWand}, {WillowWand}, {HollyWand}")
print ("What a great day for ollivanders!")
