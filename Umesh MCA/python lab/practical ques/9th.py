# Implement a function using **kwargs that accepts variable keyword-value pairs and iterates through
# them to display key-value pairs.

def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


display(name="Sagar", marks=59.53, age=20)