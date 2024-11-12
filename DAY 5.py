import random
fruits = ["Apple", "Peach", "Pear"]
for i in fruits:
    print(i)
    print(i + " Pie")

student_heights = input("Input a list of student heights ").split()
sum_height = 0
average_height = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum_height =  sum_height + student_heights[n]
average_height = round(sum_height / len(student_heights))
print(f"Your average height is: {average_height}")

student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
max_score = student_scores[0]
for score in student_scores:
    if max_score > score:
        max_score = max_score
    else:
        max_score = score
print(f"Your highest score is: {max_score}")

even_numbers = 0
for n in range(2,101,2):
    even_numbers+= n
print(even_numbers)

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz") 
    
    else:
         print(n)

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','+']
print("Welcome to the pypassword generator.")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols =int(input("How many symbols would you like in your password?\n"))

password = ""
for i in range(0,nr_letters):
    c = random.choice(letters)
    password = password + c
for n in range(0,nr_numbers):
    d = random.choice(numbers)
    password = password + d
for k in range(0,nr_symbols):
    e = random.choice(symbols)
    password = password + e
newpassword = (list(password))
random.shuffle(newpassword)
print (''.join(newpassword))

