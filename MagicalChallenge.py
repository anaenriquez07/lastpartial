https://replit.com/join/bapqjoslfo-ana-lucialuc103

number_of_events = int(input("Enter the number of events in the Quidich game: "))

goals = 0
snitchs = 0
fouls = 0
goalg = 0
snitchg = 0
foulg = 0

quidditch_events = ["goal","snitch","foul"]

for i in range(number_of_events):
  event = input(f"Enter the event {i + 1} (foul, snitch, goal)") 
  team = input("Which team scored? (slytherin or gryffindor)")
  if team == "slytherin" and event == quidditch_events[0]:
    goals += 1 
  if team == "slytherin" and event == quidditch_events[1]:
    snitchs += 1 
  if team == "slytherin" and event == quidditch_events[2]:
      fouls += 1 
  if team == "gryffindor" and event == quidditch_events[0]:
      goalg += 1 
  if team == "gryffindor" and event == quidditch_events[1]:
      snitchg += 1 
  if team == "gryffindor" and event == quidditch_events[2]:
      foulg += 1 

pointss = int(fouls)*-30 + int(goals)*10 + int(snitchs)*150

pointsg = int(foulg)*-30 + int(goalg)*10 + int(snitchg)*150

print("Griffindor: ",pointsg)
print("Slytherin: ",pointss)

if pointss > pointsg:
  print ("Slytherin wins!")
elif pointsg > pointss:
  print("Gryffindor wins!")
else:
  print ("It's a tie!")
