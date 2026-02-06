
def add(a,b):
    return a+b;
def subtract(a,b):
    return a-b;
def multiply(a,b):
    return a*b;
def divide(a,b):
    if(b==0):
        print("Enter a valid choice")
        return None
    return a/b;
operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculate():
    continue1=True
    num1=float(input("What is the first number:"))
    while continue1:
        for symbol in operation:
            print(symbol)
        operation_choice=input("Enter the operation:")
        num2=float(input("What is the second number:"))
        ans=operation[operation_choice](num1,num2)
        if ans is None:
            print("Calculation stopped.")
            return   
        print(f"{num1} {operation_choice} {num2}={ans}")
        next_choice=input(f"Type 'y' to continue calculating with {ans} and 'n' to start a new calculation and 'e' to exit calculator:")
        if(next_choice=='y'):
            num1=ans;
        elif(next_choice=='e'):
            return
        elif(next_choice=='n'):
            continue1=False
            calculate()
calculate()           
    
    
    
