#1.3.4 리스트
a = [1,2,3,4,5] #리스트 생성
print(a) #리스트 내용 출력 -> [1,2,3,4,5]

print(len(a)) #리스트 크기 출력 -> 5

print(a[0]) #리스트의 1번째 인덱스 요소 출력 -> 1

print(a[4]) #리스트의 5번째 인덱스 요소 출력 -> 5

a[4] = 99 #값 대입 
print(a[4]) #99

print(a) #리스트의 요소들 출력 -> [1,2,3,4,99]

print(a[0:2]) #0번째부터 2번째 인덱스 전까지 출력 -> [1,2]
print(a[1:]) #1번째부터 끝까지 출력 -> [2,3,4,99]
print(a[:3]) #처음부터 3번째 인덱스 이전까지 출력 -> [1,2,3]
print(a[:-1]) #처음부터 마지막 인덱스 1개 전까지 출력 -> [1,2,3,4]
print(a[:-2]) #처음부터 마지막 인덱스 2개 전까지 출력 -> [1,2,3]