def main():
    # i = int(input("Enter a number, the cat will speak that much times: "))
    # while i != 0:
    #     print("meow!")
    #     i -= 1

    # for i in [0, 1, 2]:
    # for i in range(3):
    #     print("meow!")

    # restricting user to only enter a positive integer: use a infinite while loop and break it when the user
    # enter a positive integer 
    while True:
        n = int(input("Enter a number: "))
        # if(n < 0):
        #     continue
        # else:
        #     break
        if(n > 0):
            break

    for _ in range(n):
        print("meow!")

main()