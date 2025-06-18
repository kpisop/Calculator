basic_ID = ("add ", "subtract ", "multiply ", "divide ")

def add(*args):
    return sum(args)

def subtract(*args):
    return args[0] - sum(args[1:])

def multiply(*args):
    return eval('*'.join(map(str, args)))

def divide(*args):
    return eval('/'.join(map(str, args))) 


