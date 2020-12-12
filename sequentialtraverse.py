finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_sequential(target, array):
    counter=0
    for number in array:
        counter+=1
        if target == number:
            print("연산 횟수는",counter)
            return True
    print("연산 횟수는",counter)
    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True
