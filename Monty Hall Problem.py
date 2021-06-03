#!/usr/bin/env python
# coding: utf-8

# In[47]:


import random

def DoorGenerator(): #generate three random doors
    doors = []
    doors.append(random.random())
    doors.append(random.random())
    doors.append(random.random())
    for i in range(len(doors)):
        if doors[i] == doors[doors.index(max(doors))]:
            doors[i] = 1 #the max random value turns to 1 (prize door)
        else:
            doors[i] = 0 #the other values become 0 (goat door)
    return doors

def PickDoor(doors): #randomly chooses a door (aka the player's choice)
    choosen_door = random.choice([0,1,2])
    return choosen_door

def EliminateDoor(doors,choosen_door): #presenter eliminates one door
    door_to_exclude = choosen_door #forces the function to go through the while loop
    while door_to_exclude == choosen_door or doors[door_to_exclude]==1:
        door_to_exclude = random.choice([0,1,2])
    doors.pop(door_to_exclude)
    
    if choosen_door == 1 and door_to_exclude == 0: #updates the player's door index
        choosen_door = 0
    elif choosen_door == 2:
        choosen_door = 1
    return doors, choosen_door

def ChangeDoor(doors, bin_choice, choosen_door): #changes player's door if bin_choice = 1
    if bin_choice == 1:
        if choosen_door == 0:
            choosen_door = 1
        else:
            choosen_door = 0
    return choosen_door

def Result (doors,choosen_door): #checks if player's door is the prize's door
    if doors[choosen_door] == 1:
        return "Success"
    else:
        return "Failure"

def MontyHallProblem(bin_choice): #call all the functions above to simulate the Monty Hall Problem
    doors = DoorGenerator()
    choosen_door = PickDoor(doors)
    doors, choosen_door = EliminateDoor(doors,choosen_door)
    choosen_door = ChangeDoor(doors, bin_choice, choosen_door)
    return Result(doors,choosen_door)


# In[56]:


success=0
failure=0
i = 0
for i in range (10000):
    if MontyHallProblem(1) == "Success":
        success += 1
    else:
        failure += 1
print ("Successes: " + str(success))
print ("Failures: " + str(failure))
print (str(round(100*success/(success+failure),4))+ "%")

