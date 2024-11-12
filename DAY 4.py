import random
integer= random.randint(0,1)

if integer == 0:
   print("Head")
else:
   print("Tail")

names= input("Give me the names of everyone separated by a comma. ")
name= names.split(", ")
length= len(name)
choice=random.randint(0, length-1)
pay_person= name[choice]
print(f"{pay_person} pays")

row1= ["😀", "😄", "😇"]
row2= ["😗", "🤪", "😎"]
row3= ["🥺", "☹️", "👻"]
map= [row1,row2,row3]
print(f"{row1}\n {row2}\n {row3}")
position= input("Where do you want to put the treasure? ") 

horizontal= int (position[0])
vertical = int(position[1])
map [vertical-1][horizontal-1]= "X"
print(f"{row1}\n {row2}\n {row3}")
















