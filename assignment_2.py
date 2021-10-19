def is_antipalindrome(number):
    end = len(number) - 1
    start = 0

    while start < end:
        if number[start] == number[end]:
            return 0
        start += 1
        end -= 1
    return 1

def test_is_antipalindrome():
    number = input("Read a number:")
    if is_antipalindrome(number) == 1:
        print(True)
    else:
        print(False)

def get_base_2(number):
    number_in_base_2 = ""
    while number > 0:
            if number % 2 == 0:
                number_in_base_2 += "0"
            else:
                number_in_base_2 += "1"
            number = int(number / 2)
    return number_in_base_2
              
def test_get_base_2():
    number_in_base_10 = int(input("Read the number:"))
    print(get_base_2(number_in_base_10))

def main():
    problem = input("Choose a problem:")
    if problem == "7":
        test_is_antipalindrome()
    elif problem == "8":
        test_get_base_2()

if __name__ == '__main__':
    main()
