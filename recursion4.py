def cycle(string):
    start = len(string)//2
    # 8글자일 때는 4번째와 5번째 즉 3번과 4번 비교
    # len(string)은 8, start는 4, start-1과 len(string)-start 비교 
    # 9글자일 때에는 4번째와 6번째 즉 3번과 5번 비교
    # len(string)은 9, start는 4, start-1과 len(string)-start 비교 
    #print(string[0],'vs',string[len(string)-1])
    #print(string[0]==string[len(string)-1])
    if string[0]!=string[len(string)-1]:
        print("회문이 아니다")
        return 
        
    newstring=""
    for i in range(1,len(string)-1):
        newstring+=string[i]
    
    if newstring=='':
        print("회문이다")
        return
    
        #return True    

    #print(newstring)
    cycle(newstring)
    
cycle("소주만병만주소")
