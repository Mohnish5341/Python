#Exception Handling
try:
    print("Hellow world")
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    print(a/b)
    if b>199:
        raise Exception("This number is greater than 199")
except ValueError:
    print("Value error occured")
except ZeroDivisionError:
    print("This is a zero division error")   
except Exception as e:
    print(f"There is error in inputs: {e}")
else:
    print("Try was successful")
print("There is no error")





