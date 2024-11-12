#print("This program checks numbers provided it and tell if they are even or odd")
#num= int(input("What number would you like to check? "))
#if num % 2 == 0:
   #print("Number is even")
#else:
   #print("Number is odd")

#print("Welcome to the BMI calcualtor")
#weight= float(input("What is your weight in kg? "))
#height= float(input("What is your height in m?"))
#BMI= round(weight / (height ** 2))

#if BMI <= 18.5:
    #print(f"You have a BMI of {BMI} which is underweight")
#elif BMI < 25:
    #print(f"You have a BMI of {BMI} which is a normal weight")
#elif BMI < 30:
    #print(f"You have a BMI of {BMI} which is overweight")
#elif BMI < 35:
    #print(f"You have a BMI of {BMI} which is obese")
#else:
    #print(f"You have a BMI of {BMI} which is clinically obese")

#print("This program determines if a year is a leap year or not")
#year= int(input("What year would you like to check? "))

#if year % 4 == 0:
    #if year % 100 == 0:
        #if year % 400 == 0:
            #print("Year is a leap year")
        #else:
            #print("Year is not a leap year")
#elif year % 4 == 0:
    #if year % 100 != 0:
        #print("Year is a leap year")
    #else:
        #print("Year is not a leap year")
#else:
    #print("Year is not a leap year")

#print("Welcome to pizza deliveries")
#sizes = "S","M","L"
#size =input("What size of pizza would you want? S,M and L? ")
#bill = 0
#pep = input("Would you like pep? Y or N? ")
#cheese = input("Would you like cheese? Y or N? ")

#if size == "S":
    #bill = 15
    #if pep == "Y":
        #bill+= 2
    #else:
        #bill= 15
    #if cheese == "Y":
        #bill+=1
    #else:
        #bill= 15
    #print(f"Your Bill is{bill}")
#elif size == "M":
    #bill= 20
    #if pep == "Y":
        #bill+= 3
    #else:
        #bill= 20
    #if cheese == "Y":
        #bill+=1
    #else:
        #bill= 20
    #print(f"Your Bill is {bill}") 
#elif size == "L":
    #bill= 25
    #if pep == "Y":
        #bill+= 3
    #else:
        #bill= 25
    #if cheese == "Y":
        #bill+=1
    #else:
        #bill= 25
    #print(f"Your Bill is {bill}")  
#else:
    #print("Your order is invalid") 

#print("Welocome to the love calculator")
#name1= input("What is your name?\n ").lower()
#name2= input("What is their name?\n ").lower()
#t= name1.count("t")
#r= name1.count("r")
#u= name1.count("u")
#e= name1.count("e")
#l= name1.count("l")
#o= name1.count("o")
#v= name1.count("v")
#e= name1.count("e")
#t1= name2.count("t")
#r1= name2.count("r")
#u1= name2.count("u")
#e1= name2.count("e")
#l1= name2.count("l")
#o1= name2.count("o")
#v1= name2.count("v")
#e2= name2.count("e")
#love_score= str(t+r+u+e+l+o+v+e) + str(t1+r1+u1+e1+l1+o1+v1+e2)

#if love_score < str(10) or love_score> str(90): 
    #print(f"Your love score is {love_score}, you go togethher like coke and mentos.")
#elif love_score >=str(40) and love_score <=str(50):
    #print(f"Your love score is {love_score}, you are alright together.")
#else:
    #print(f"Your love score is {love_score}")



#print("Welcome to Treasure Island\nYour mission is to find the treasure" )
#direction= input("Which way would you like to move? Left or Right? " ).lower()
#if direction == "left":
    #print("You have come across a turbulent river.")
    #ans1= input("Would you like to swim or wait for a boat? ").lower()
    #if ans1 == "wait":
        #print("Good! Now upon you are three doors. Red, blue and yellow.")
        #ans2= input("Which door would you enter next? ").lower()
        #if ans2 == "yellow":
            #print("You won!")
        #elif ans2 == "red":
            #print("You fell into a lake of fire. Game Over!")
        #else:
            #print("You entered a room of powerful beast and got devoured.Game Over!")
    #else:
        #print("The river was full of disturbing rocks and crocs.Game Over!")
#else:
    #print("Right directions are not always right! Game Over!")


    





