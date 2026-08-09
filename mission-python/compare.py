def main():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    compare(x, y)

def compare(x, y):
    # if x < y:
    #     res = "x is lesser than y"
    # if x > y:
    #     res = "x is greater than y"
    # if x == y:
    #     res = "x is equal to y"

    #The code written above with three if statements is okay, but there is better approach to do what the above
    #code does. The idea is to ask lesser questions in the program

    # if x < y:
    #     res = "x is lesser than y"
    # elif x > y:
    #     res = "x is greater than y"
    # elif x == y:
    #     res = "x is equal to y"

    #much better
    # if x > y:
    #     res = "x is lesser than y"
    # elif x > y:
    #     res = "x is greater than y"
    # else:
    #     res = "x is equal to y"


    #removing one elif: at max 2 questions
    # if x > y or x < y:
    #     res = "x is not equal to y"
    # else:
    #     res = "x is equal to y"

    #better: only 1 question
    if x != y:
        res = "x is not equal to y"
    else:
        res = "x is equal to y"

    print(res)


main()