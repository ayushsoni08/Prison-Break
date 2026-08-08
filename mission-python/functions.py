# def hello(to):
#     print(f"Hello, {to}")


# name = input("What's your name?")
# hello(name)

# If you call a function before defining it, the program returns an error

# def hello(to):
#     print(f"Hello, {to}")

# What if your program requires a lot of function definitions? Then this is an issue. To overcome this issue, we
# can define a main function at the top of the program and then call all the required functions inside it. But to
# make the program do something, we need to call the main funtion at last

def main():
    name = input("What's your name?")
    hello(name)


def hello(to):
    print(f"hello, {to}")


main()