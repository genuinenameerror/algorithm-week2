def cycle(string):
    start = len(string)//2
    counter=0
    # 8글자일 때는 4번째와 5번째 즉 3번과 4번 비교
    # len(string)은 8, start는 4, start-1과 len(string)-start 비교 
    # 9글자일 때에는 4번째와 6번째 즉 3번과 5번 비교
    # len(string)은 9, start는 4, start-1과 len(string)-start 비교 
    while start>0:
        if string[start-1] != string[len(string)-start]:
            return False
        start-=1         
    return True
print(cycle("abcba"))
