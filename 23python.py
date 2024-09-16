#Exception Handling
def function():
    try:
        a=int(input("Enter a number: "))
        b=int(input("Enter a number: "))
        print(a/b)
    except Exception as e:
        print(f"There is error in inputs: {e}")
    finally:
        print("I will always be executed")

function()

if __name__ == '__main__':
    print("if you will run in a same file then I will execute")#import this 23pythone.py file to another fill and run it It will not execute this part only



