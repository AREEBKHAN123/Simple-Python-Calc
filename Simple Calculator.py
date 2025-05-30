print('''
     Guide...Enter two numbers and these symbols for operations:
     + for addition
     - for subraction
     / for division
     * for multiplication
     ''')
a = float(input("Enter a Number: "))
b = float(input("Enter another Number: "))
op = input("Enter your operator(+,-,/,*): ")
if op == "+" :
 print(f"The Result Is {a + b}")
if op =="-":
    print(f"The Result Is {a - b}")
if op =="/":
    print(f"The Result Is {a / b}")
if op == "*":
    print(f"The Result IS {a * b}")
if op!="+" and op!="-" and op!="/" and op!="*": 
    print(f"{op} Is Not A Valid Operator...")
    #Yep learning Python On 5th May,2025 By Areeb Khan ;D
print("Mini Project By Areeb Khan :)")


