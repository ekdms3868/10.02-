n=int(input()) #몇 개를 입력 할건지 입력 받기 #반복문에서 사용할 변수 i 정의
i=0
while(n>=i): #n이 i보다 크거나 같을때 까지
    for i in range(1, n + 1,1): #i가 1부터 n까지 1씩 증가
        a, b = input().split() #a와 b 입력받기 split으로 받아서 정수형이 아닌 문자열
        print("Case #%d: %d + %d = %d"%(i,int(a),int(b),int(a)+int(b))) #출력