sugar = int(input())
bag = 0
while sugar >= 0 :
    if sugar % 5 ==0 : # 5의 배수인 경우
        bag += (sugar // 5) # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3 # 5의 배수가 아닌 경우 3kg 봉지를 사용했다고 표현하기
    bag +=1 # 5의 배수가 될때까지 설탕 -3, 봉지 +1
else :
    print(-1)