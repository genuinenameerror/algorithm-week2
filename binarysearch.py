finding_target = 0
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    index = len(array) // 2
    margin = len(array) // 2
    eliminated = 0
    while eliminated<len(array):
        print(index,margin)
        if array[index]==target:
            return True
        elif array[index]<target:
            if margin//2<1:
                eliminated+=1
                margin=margin//2
                index+=1
            else:
                eliminated+=margin
                margin = margin//2
                index+=(int(margin))            
        else:
            if margin//2<1:
                eliminated+=1
                margin=margin//2
                index-=1
            else:
                eliminated+=margin
                margin = margin//2
                index-=(int(margin))        

    
    # 구현해보세요!
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
#print(len(finding_numbers))
