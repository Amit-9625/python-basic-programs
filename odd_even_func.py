def check_even_odd(*args):
    for i in args:
        if(isinstance(i,int)):
            if(i%2==0):
                print(f"{i} is even")
            else:
                print(f"{i} is odd")
        else:
            print(f"invalid input")
check_even_odd(2,8,43,7)
