def get_minimum_possible_number_to_get__prime_number(a,b):
    if (a == 0) and (b == 0):
        return 1
    k = a + b
    for i in range(1, k): #4
        minimum_possible_number = k + i #11
        minimum_possible_number_list = []
        for j in range(2, minimum_possible_number):
            if (minimum_possible_number % j) == 0:
                minimum_possible_number_list.append(minimum_possible_number)
                break
        if len(minimum_possible_number_list) == 0:
            return i

def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    minimum_possible_number_to_get__prime_number = get_minimum_possible_number_to_get__prime_number(a,b)
    print(minimum_possible_number_to_get__prime_number)

main()