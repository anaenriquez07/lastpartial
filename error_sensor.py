https://replit.com/join/iemkaxyjtl-ana-lucialuc103 

counts = 0
readings = int(input("How many readings do you have? "))

for i in range(readings):
  temperature = int(input(f"Insert the temperature for reading {i + 1}: "))
  if 10 < temperature < 40:
    counts += 1

print ("The server went wrong",counts,"times")
error_rate = (counts/readings) * 100
print ("The sensor error rate is",error_rate) 
