def main():
    n = int(input("enter the size of brick square: "))
    print_square(n)


def print_square(size):
    for i in range(size):
        # for j in range(size):
        #     print("#", end="")
        # print()
        print_row(size)

def print_row(width):
    print("#" * width)

main()