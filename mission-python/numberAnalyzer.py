def main():
    # initialize a empty list, this list will be used to store all the numbers entered by the user
    numbers = []
    count = 0
    while True:
        try:
            n = int(input("Enter a number: "))
            numbers.append(n)
            count += 1

            # after every 5 valid inputs, ask the user if they want to continue
            # using count variable to hit this functionality after every 5 valid user inputs
            if count == 5:
                ans = input("To continue, enter a yes else no: ").lower()
                if ans == "yes":
                    count = 0
                    continue
                else:
                    break

        except ValueError:
            print("Invalid input.")
            ans = input("To continue, enter a yes else no: ").lower()

            if ans == "yes":
                continue
            else:
                break

    list_len = len(numbers)

    if list_len > 0:
        largest = get_max(numbers)
        smallest = get_min(numbers)
        total = get_sum(numbers)
        # average = get_average(numbers)
        average = float(total/list_len)
        positives = get_positives(numbers)
        zeroes = get_zeroes(numbers)
        negatives = get_negatives(numbers)

        print("-----Results-----")
        print(f"Numbers entered: {len(numbers)}")
        print(f"Largest: {largest}")
        print(f"Smallest: {smallest}")
        print(f"Sum: {total}")
        print(f"Average: {round(average, 2)}")
        print(f"Positive: {positives}")
        print(f"Zeroes: {zeroes}")
        print(f"Negatives: {negatives}")

def get_max(nums):
    maxi = nums[0]

    for num in nums[1:]:
        if num > maxi:
            maxi = num

    return maxi

def get_min(nums):
    mini = nums[0]

    for num in nums[1:]:
        if num < mini:
            mini = num

    return mini

def get_sum(nums):
    addition = 0

    for num in nums:
        addition += num

    return addition

# def get_average(nums):
#     avg = 0
#     n = len(nums)
#     temp = 0
#     for num in nums:
#         temp += num

#     avg = temp/n
#     return avg    

def get_positives(nums):
    ans = 0

    for num in nums:
        if num > 0:
            ans += 1

    return ans

def get_zeroes(nums):
    ans = 0

    for num in nums:
        if num == 0:
            ans += 1

    return ans

def get_negatives(nums):
    ans = 0

    for num in nums:
        if num < 0:
            ans += 1

    return ans


main()