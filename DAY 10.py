# Functions with outputs
# def format_name(f_name, l_name):
"""Takes a first and last name and format it to their title case version"""
#     new_f_name = f_name.title()
#     new_l_name =  l_name.title()
#     return f"{new_f_name} {new_l_name}"
# print(format_name("DanIel", "DANSO"))

# def leap_year(year):
#     """Checks if a year is a leap year or not and returns a Boolean.
#     True for leap and False for not leap"""
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                return True
#             else:
#                return False
#     elif year % 4 == 0:
#         if year % 100 != 0:
#           return True
#         else:
#             return False
#     else:
#       return False

# def days_in_month(year, month):
#    if month > 12 or month < 1:
#         return "Invalid month specified"
#    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#    if leap_year(year) and month == 2:
#       return 29
#    return month_days[month - 1]
         

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# Calculator
 
    # Addition
    # def add(n1, n2):
    #     """Adds given numbers and returns results"""
    #     return n1 + n2
    # # Subtraction
    # def sub(n1, n2):
    #     """Subtracts given numbers and returns results"""
    #     return n1 - n2
    # # Multiplication
    # def mul(n1 , n2):
    #     """Multiplies given numbers and returns results"""
    #     return n1 * n2
    # # Division
    # def div(n1, n2):
    #     """Divides given  numbers and returns results"""
    #     return n1 / n2

    # operation = {
    #     "+": add,
    #     "-": sub,
    #     "*": mul,
    #     "/": div,
    #              }
    # def calculator():
    #     num1 = float(input("What is the first number? "))
    #     for op in operation:
    #         print(op)

    #     stop = True
    #     while stop:
    #         operation_symbol = input("Pick an operarion symbol: ")
    #         num2 = float(input("What is the next number? "))       
    #         calculation = operation[operation_symbol]
    #         answer = calculation(num1, num2)
    #         print(f"{num1} {operation_symbol} {num2} = {answer}")
    #         if input("Do you want to exit calculator? Type 'y' to exit or 'n' to continue" ) == 'y':
    #             stop = False
    #             print("Goodbye")  
                
    #         else:
    #             if input(f"Type 'y' to continue with {answer} or 'n' to start afresh ") ==  'y':
    #                 num1 = answer
    #             else:
    #                 stop = False
    #                 calculator()
    # calculator()