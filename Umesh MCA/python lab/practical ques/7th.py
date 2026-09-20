# Create a program demonstrating function calls with positional arguments, keyword arguments(name= "Sagar", marks = 59.53)
# and default parameter values(b = 10)


def student(name, marks, b = 10):
    print("Name", name)
    print("Marks", marks)
    print("value of b:>", b)


student("Sagar", 59.53, 20)  # Positional argument
student(name="Sagar", marks=59.53, b= 30)  # Keyword argument
student("Sagar", 59.53)   # Default argument
