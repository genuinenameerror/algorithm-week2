numbers = [1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1,1, 1, 1, 1, 1]
target_number = 28
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    maximum_value = len(array) #최댓값은 모든 1을 더하는 경우 하나
    if target>maximum_value: # 최댓값보다 더 큰 목표값은 방법 0 
        return 0
    elif target==maximum_value: # 30개의 1로 30을 구하는 방법은 전부 더해서 나오는 최댓값 하나뿐 
        return 1
    number_of_minus = maximum_value-target
 
    #n개 중에 r개를 선택하는 조합 nCr = n! / (n-r)!r!
    # factorial(len(array)) / ( factorial(len(array)-(len(array)-target) * factorial(len(array)-target))  )
    #5C2 = 5*4*3*2*1 / 3*2*1*2*1
    
    # 구현해보세요!
    return int( factorial(len(array)) / (factorial( len(array) - number_of_minus) * factorial(number_of_minus)))


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number)) 
