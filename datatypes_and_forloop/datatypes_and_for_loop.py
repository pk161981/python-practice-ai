#variables are used to store data in python
#varaible is container that holds data some value
#variable in python is an Object that can hold different types of data like numbers, strings,
#  lists, etc.
revenue=50
expenses=20
print("Revenue is:", revenue)
type_of_revenue=type(revenue)
print("Type of revenue is:", type_of_revenue)

#to calculate profit
profit=revenue-expenses
print("Profit is:", profit)

margin=profit/revenue
print("Margin is:", margin)
type_of_margin=type(margin)
print("Type of margin is:", type_of_margin) #float

#every variable you create in python is an object and every object has a unique id
#id() function is used to get the memory address of the variable
print("ID of margin is:", id(margin))    

#string is a sequence of characters enclosed in single or double quotes
expenses_description="Expenses are the costs incurred in the process of earning revenue"
print("Expenses description is:", expenses_description)
type_of_expenses_description=type(expenses_description)
print("Type of expenses description is:", type_of_expenses_description) #string

#to get the length of the string
expenses_description_length=len(expenses_description)
print("Length of expenses description is:", expenses_description_length) #length of string

#to create a multi-line string, you can use triple quotes (''' or """)
expenses_description = '''
Expenses are the costs incurred in the process of earning revenue.
They represent the resources consumed to generate income.
'''
print("Expenses description is:", expenses_description)
type_of_expenses_description=type(expenses_description)
print("Type of expenses description is:", type_of_expenses_description) #string

#Naming conventions in Python is usually snake_case, 
# which means that words are separated by underscores. 
# For example, variable names like revenue, expenses, profit_margin, and total_revenue follow this convention.

#LIST
#A list is a collection of items that are ordered and changeable. 
# In Python, lists are defined using square brackets [] 
# and can contain elements of different data types. 
# Here's an example of how to create a list to store the revenues for each quarter:
revenues_list=[50, 100, 150, 200, 250] #indexing starts from 0..
print("Revenues list is:", revenues_list)
type_of_revenues_list=type(revenues_list)
print("Type of revenues list is:", type_of_revenues_list) #list

#to get the first element of the list
first_revenue=revenues_list[0]
print("First revenue is:", first_revenue)

#to get the last element of the list
last_revenue=revenues_list[-1]
print("Last revenue is:", last_revenue)

#to get the second element of the list
second_revenue=revenues_list[1]
print("Second revenue is:", second_revenue)

#to get the length of the list
revenues_list_length=len(revenues_list)
print("Length of revenues list is:", revenues_list_length)

#to get the Q2 and Q3 of the list
q2_revenue=revenues_list[1:3] #slicing the list from index 1 to 3 (not including 3)
print("Q2 revenue is:", q2_revenue)

q3_revenue=revenues_list[2:4] #slicing the list from index 2 to 4 (not including 4)
print("Q3 revenue is:", q3_revenue)

revenues_list.append(300) #to add an element to the end of the list
print("Revenues list after appending 300 is:", revenues_list)

#create a revenues and expenes list
revenues=[50, 100, 150, 200, 250]
expenses=[20, 40, 60, 80, 100]

#FOR LOOP 
#A for loop is a control flow statement that allows you to iterate over a 
# sequence of elements, such as a list, tuple, or string. 
# In Python, the for loop is used to execute a block of code repeatedly for each element
#  in the sequence. 
# Here's an example of how to use a for loop to iterate over the revenues and expenses lists:
#print the revenues one by one using a for loop..
for revenue in revenues:
    print("Revenue is:", revenue) #here its based on indentation
    #format string is a way to format strings in python using f-strings, 
    # which allows you to embed expressions inside string literals, 
    # using curly braces {}. 
    # Here's an example of how to use f-strings to print the revenue:
    print(f"Revenue is: {revenue}")

#print the expenses one by one using a for loop..
for expense in expenses:
    print("Expense is:", expense)
    #print using python format string
    print(f"Expense is: {expense}")

#Calculate the margin for each of the quarters for revenues and expenses
#range is a built-in function that generates a sequence of numbers, 
# which can be used to iterate over a sequence of elements in a list. 
# In this case, we are using range(len(revenues)) to generate a sequence of numbers 
# from 0 to the length of the revenues list (which is 5), 
# and then using that sequence to access each element in the revenues and expenses lists
#  by index.
for i in range(len(revenues)):
    print(f"Revenue is: {revenues[i]}")
    #print(f"Expense is: {expenses[i]}")
    revenue=revenues[i]
    print(f"Revenue for Quarter {i+1} is: {revenue}")
    #expense=expenses[i]
    #profit=revenue-expense
    #margin=profit * 100 /revenue
    #print(f"Quarter {i+1}: Revenue={revenue}, Expense={expense}, Profit={profit}, Margin={margin:.2f}")
    #print(f"Margin for Quarter {i+1} is: {margin:.2f}%") 
    #:.2f is used to format the float to 2 decimal places

    #If I want to store the margins in a list, I can create an empty list before the loop and then append the margin for each quarter to that list inside the loop. Here's how you can do it:
    margins=[] #python list to store the margins for each quarter
    for i in range(len(revenues)):
        revenue=revenues[i]
        expense=expenses[i]
        profit=revenue-expense
        margin=profit * 100 /revenue
        margins.append(margin) #append the margin to the list
    print("Margins for all quarters are:", margins)

    #DICTIONARY
    #A dictionary is a collection of key-value pairs, 
    # where each key is unique and maps to a value. 
    # In Python, dictionaries are defined using curly braces {} 
    # and key-value pairs are separated by colons. 
    # Here's an example of how to create a dictionary to store the revenues and expenses
    #  for each quarter:
    financial_q1 = {
        "revenue": 50,
        "expenses": 20
    }
    type_of_financial_q1=type(financial_q1)
    print("Type of financial_q1 is:", type_of_financial_q1) #dict

    #to calculate profit and margin for Q1
    profit_q1=financial_q1["revenue"]-financial_q1["expenses"]
    margin_q1=profit_q1 * 100 / financial_q1["revenue"]
    print(f"Quarter 1: Revenue={financial_q1['revenue']},Expenses={financial_q1['expenses']}, Profit={profit_q1}, Margin={margin_q1:.2f}%")

    #to add an element into a dict object
    financial_q1['profit'] = profit_q1
    print("financial_q1 dictionary is:", financial_q1)

    #create a list of dictionaries
    financials = [
        {"revenue": 50, "expenses": 20}, #q1
        {"revenue": 60, "expenses": 30}, #q2
        {"revenue": 55, "expenses": 35}, #q3
    ]
    print("Financials list of dictionaries is:", financials)

    for fin in financials:
        revenue=fin["revenue"]
        expense=fin["expenses"]
        profit=revenue-expense
        margin=profit * 100 / revenue
        print(f"Revenue={revenue}, Expense={expense}, Profit={profit}, Margin={margin:.2f}%")
        print(f"Margin is: {margin:.2f}%")

    #to create a Nested Dictionary, you can create a dictionary 
    # where the values are themselves dictionaries. 
    # Here's an example of how to create a nested dictionary to store the 
    # revenues and expenses for each quarter:
    financials_nested = {
        "Q1": {"revenue": 50, "expenses": 20}, #value of each key is a dictionary
        "Q2": {"revenue": 60, "expenses": 30},
        "Q3": {"revenue": 55, "expenses": 35},
    }
    print("Financials nested dictionary is:", financials_nested)

    #to access the values in the nested dictionary:
    q1_revenue = financials_nested["Q1"]["revenue"]
    q1_expenses = financials_nested["Q1"]["expenses"]
    q1_profit = q1_revenue - q1_expenses
    print(f"Q1 Revenue: {q1_revenue}, Q1 Expenses: {q1_expenses}, Q1 Profit: {q1_profit}")

    #to access the values in the nested dictionary:
    q2_revenue = financials_nested["Q2"]["revenue"]
    q2_expenses = financials_nested["Q2"]["expenses"]
    q2_profit = q2_revenue - q2_expenses
    print(f"Q2 Revenue: {q2_revenue}, Q2 Expenses: {q2_expenses}, Q2 Profit: {q2_profit}")

    #to access the values in the nested dictionary:
    q3_revenue = financials_nested["Q3"]["revenue"]
    q3_expenses = financials_nested["Q3"]["expenses"]
    q3_profit = q3_revenue - q3_expenses
    print(f"Q3 Revenue: {q3_revenue}, Q3 Expenses: {q3_expenses}, Q3 Profit: {q3_profit}")

    #to iterate over the nested dictionary: key and value pairs
    for quarter, data in financials_nested.items():
        revenue = data["revenue"]
        expenses = data["expenses"]
        profit = revenue - expenses
        print(f"{quarter}: Revenue={revenue}, Expenses={expenses}, Profit={profit}")
        margin = profit * 100 / revenue if revenue != 0 else 0
        print(f"{quarter}: Revenue={revenue}, Expenses={expenses}, Profit={profit}, Margin={margin:.2f}%")

    financials_nested = {
            "Q1": {"revenue": 50, "expenses": 20}, #value of each key is a dictionary
            "Q2": {"revenue": 60, "expenses": 30},
            "Q3": {"revenue": 55, "expenses": 35},
            "Q4": {"revenue": -10, "expenses": 35}
        }

    #to iterate over the nested dictionary: key and value pairs
    #skip the quarter if revenue is negative
    for quarter, data in financials_nested.items():
        if data["revenue"] < 0:
            print(f"{quarter}: Revenue is negative, skipping calculation.")
            continue
        revenue = data["revenue"]
        expenses = data["expenses"]
        profit = revenue - expenses
        print(f"{quarter}: Revenue={revenue}, Expenses={expenses}, Profit={profit}")
        margin = profit * 100 / revenue if revenue != 0 else 0
        print(f"{quarter}: Revenue={revenue}, Expenses={expenses}, Profit={profit}, Margin={margin:.2f}%")    

     #Tuples
    #A tuple is a collection of items that are ordered and unchangeable.
    #Tuples are defined using parentheses () and can contain elements of different data types.
    #Tuples are Immutable whereas Lists are Mutable. 
    # This means that once a tuple is created, its elements cannot be changed, added, or removed. 
    # In contrast, lists can be modified after creation.
    #Create a tuple for RGB color values
    rgb_color = (255, 0, 0) #red color
    print("RGB color tuple is:", rgb_color)

