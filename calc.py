# get two integer parameters
# return sum
def plus(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def div(x, y):
    return x/y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus 2:subtract 3:multiplication 4:divide")
        check = int(input())
        if check == 1:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", plus(x,y))
        elif check == 2:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", sub(x,y))
        elif check == 3:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", mul(x,y))
        elif check == 4:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", div(x,y))
        elif check>4:
            print("Unsupported")

if __name__ == "__main__":
    main()