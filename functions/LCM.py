LCM_ID = "lcm "

def lcm(*args):

    max_num = max(args)
    current = max_num
    
    while True:
        if all(current % num == 0 for num in args):
            return current
        current += max_num




