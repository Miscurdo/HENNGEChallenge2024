# HENNGE Applicant Test
## Marco Seidenberg 24/11/2024

# Will recursively loop through each element in that specific test case and sum up the squares of the values
# When reaches the end of the available integers it will return the total sum back up
def calc(list, index, sum, num_elem):
    if num_elem == 0: return 0

    elem = int(list[index])

    # If the value is not negative or a zero value add its sum
    if (elem > 0):
        sum += pow(elem, 2)
    index += 1 
    if index < num_elem:
        return calc(list, index, sum, num_elem)
    return sum   

# Recursively loop through calling calc() on every test case, then add the calculated sum to the list
# Curr stars at 1 and increases each iteration as this makes it simpler to find the required index
# For example 5 test cases and currently at index 2; the number of elements on that test line is found at index
# 2 * 2 - 1 = 3 (2 due to the way python handles arrays) and the list of elements to be squared is found at 
# 2 * 2 = 4 (3 due to the way python handles arrays) - this way it is simpler and easier to get to the right element
def handle_test_cases(num_cases, curr, list, sum_list = ""):
    if num_cases == 0: return ""
    num_elem = int(list[curr * 2 - 2])
    new_list = list[curr * 2 - 1].split()
    sum_list = sum_list + str(calc(new_list, 0 ,0 , num_elem)) + "\n"

    curr += 1

    if curr < num_cases + 1:
        return handle_test_cases(num_cases, curr, list, sum_list)
    return sum_list

    
# Handler and calling function for the sum of squares logic
# Gets the number of test cases and removes that part of the array for the test case function
# as it is unneccesary.
def sum_of_squares(input):
    list = input.split("\n")
    num_cases = int(input[0])
    del list[0]
    return handle_test_cases(num_cases, 1, list).rstrip()

def main():
    test_input = "2\n4\n3 -1 1 14\n5\n9 6 -53 32 16"
    print(sum_of_squares(test_input))

if __name__ == "__main__":

    main()