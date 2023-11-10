https://replit.com/join/qrdiapzrce-ana-lucialuc103

animal = 0
baby = 0
young = 0
semiold = 0
old = 0

while True:
  do = input("Do you want to add another animal? ")
  if do == "yes":
    age = int(input("How old is the animal? "))
    animal += 1
    if age <= 2:
      baby += 1
    if 2 < age <= 5:
      young += 1
    if 5 < age < 10:
      semiold += 1
    if age >= 10:
      old += 1
  if do == "no": 
    break
    
babytotal = float(baby) / float(animal) * 100
youngtotal = float(young) / float(animal) * 100
semioldtotal = float(semiold) / float(animal) * 100
oldtotal = float(old) / float(animal) * 100

print("The percentage of animals who are babies is: ",babytotal)
print("The amount of babys is: ",baby)
print("The percentage of animals who are young is: ",youngtotal)
print("The amount of young animals is: ",young)
print("The percentage of animals who are semi-old is: ",semioldtotal)
print("The amount of semi-old animals is: ",semiold)
print("The percentage of animals who are old is: ",oldtotal)
print("The amount of old animals is: ",old) 
