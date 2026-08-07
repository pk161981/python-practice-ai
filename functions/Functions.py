#Functions
#Functions are blocks of code that can be reused multiple times throughout a program. 
# They help to organize code, make it more readable, and reduce redundancy. 
# In Python, functions are defined using the `def` keyword 
# followed by the function name and parentheses.

#returning one value
def calculate_margin(revenue, expenses):
    """
    This function calculates the profit margin based on revenue and expenses.
    
    Parameters:
    revenue (float): The total revenue generated.
    expenses (float): The total expenses incurred.
    
    Returns:
    float: The profit margin as a percentage.
    """
    if revenue == 0:
        return 0.0  # Avoid division by zero
    profit = revenue - expenses
    margin = (profit / revenue) * 100
    print(f"Profit Margin: {margin:.2f}%")
    return margin

calculate_margin(1000, 600)

# Calling the function with different values using variables
revenue = 2000
expenses = 1500
margin = calculate_margin(revenue, expenses)
print(f"Profit Margin: {margin:.2f}%")

#returning multiple values. return values can be returned as a tuple, list, or dictionary.
def calculate_profit_and_margin(revenue, expenses):
    """
    This function calculates both the profit and profit margin based on revenue and expenses.
    
    Parameters:
    revenue (float): The total revenue generated.
    expenses (float): The total expenses incurred.
    
    Returns:
    tuple: A tuple containing the profit and profit margin as a percentage.
    """
    if revenue == 0:
        return 0.0, 0.0  # Avoid division by zero
    profit = revenue - expenses
    margin = (profit / revenue) * 100
    print(f"Profit: {profit}, Profit Margin: {margin:.2f}%")
    return profit, margin #it will return both values as a tuple

# Calling the function with different values using variables
revenue = 2000
expenses = 1500
profit, margin = calculate_profit_and_margin(revenue, expenses)
print(f"Profit: {profit}, Profit Margin: {margin:.2f}%")

response = calculate_profit_and_margin(3000, 1000)
print(type(response))  # Output: <class 'tuple'>
print(f"Profit: {response[0]}, Profit Margin: {response[1]:.2f}%")

#give hint to the variable names to make it more readable
#type hints
def calculate_profit_and_margin_with_hint(revenue: float, expenses: float) -> tuple:
    """
    This function calculates both the profit and profit margin based on revenue and expenses.
    
    Parameters:
    revenue (float): The total revenue generated.
    expenses (float): The total expenses incurred.
    
    Returns:
    tuple: A tuple containing the profit and profit margin as a percentage.
    """
    if revenue == 0:
        return 0.0, 0.0  # Avoid division by zero
    profit = revenue - expenses
    margin = (profit / revenue) * 100
    print(f"Profit: {profit}, Profit Margin: {margin:.2f}%")
    return profit, margin #it will return both values as a tuple

#Function with dynamic number of arguments. 
# *args allows you to pass any number of arguments to a function, 
# which are then accessible as a tuple within the function.
def print_values(*args):
    for value in args:
        print(value)

print_values(1, 2, 3, 4, 5)

def calculate_total_expenses(*args):
    total = sum(args)
    print(f"Total Expenses: {total}")
    return total

result = calculate_total_expenses(100, 200, 300)
print(result)  # Output: 600

#**kargs allows you to pass a variable number of keyword arguments to a function,
# which are then accessible as a dictionary within the function.
# any number of keyword arguments can be passed to the function, 
# and they will be stored in a dictionary where the keys are the argument names 
# and the values are the argument values.
def total_expenses(rent, phone_bill):
    """
    This function calculates the total expenses based on rent and phone bill.
    
    Parameters:
    rent (float): The rent expense.
    phone_bill (float): The phone bill expense.
    
    Returns:
    float: The total expenses.
    """
    total = rent + phone_bill
    print(f"Total Expenses: {total}")
    return total

#calculate_total_expenses(rent=1000, phone_bill=100)  # Output: 1100
#TypeError: calculate_total_expenses() got an unexpected keyword argument 'rent'

#Using **kwargs to accept variable keyword arguments
def calculate_total_expenses(**kwargs):
    total = sum(kwargs.values())
    print(f"Total Expenses: {total}")
    return total

result = calculate_total_expenses(rent=1000, phone_bill=100)
result = calculate_total_expenses(rent=1000, phone_bill=100, internet_bill=50, groceries=200)
print(result)  # Output: 1350

#accessing individual keyword arguments as a dictionary
def calculate_total_expenses_with_access(**kwargs):
    total = sum(kwargs.values())
    print(f"Total Expenses: {total}")
    # Access individual keyword arguments
    total = 0
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        total += value # += means total = total + value..
                        #adding the value of each keyword argument to the total
    return total

result = calculate_total_expenses_with_access(rent=1000, phone_bill=100, internet_bill=50, groceries=200)
print(result)  # Output: 1350