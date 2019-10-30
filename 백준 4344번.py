"""
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
"""
n=int(input())
for a in range(1,n+1):
    l=input().split()
    sum=0
    p=0
    for i in range(1,len(l)):
        sum=int(l[i])+sum
    s=sum/int(l[0])
    for b in range(1,len(l)):
        if int(l[b])>s:
            p=p+1
    good=p/int(l[0])*100
    print("%.3f%%" %(round(good,3)))