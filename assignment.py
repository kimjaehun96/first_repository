# 연습문제(리스트 내장함수)
A=['Life', 'is', 'too', 'short']
print(' '.join(A))

# 연습문제
b = "Life is too short, you need python"
if 'wife' in b:
    print('wife')
elif 'python' in b and 'you' not in b:
    print('python')
elif 'shirt' not in b:
    print('shirt')
elif 'need' in b:
    print('need')
else:
    print('none')


# 연습문제(while 문 별 찍기)
a= 1
while a < 5:
    print("*" * a)
    a += 1

# 연습문제(모음 찾기)
a = "mutzangesazachurum"
result = 0
for i in a:
    if i in "aeiou":
        result += 1
print(result)



# 과제1-1

a =1
sum = 0
while a <= 1000:
    if a % 3==0:
            sum += a
    a +=1
print(sum)

# 과제1-2

a = 10

while a > 0:
    print("*" * a)
    a -= 1

# 과제1-3


A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
while len(A) >= 1:
    good = A.pop()
    if good >= 50:
        sum += good
print(sum)

# 과제2-1
A=range(1,101)
for a in A:
    print(a)

# 과제2-2
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum=0
for a in range(len(A)):
    sum += A[a]
print(sum/len(A))


# 과제2-3
numbers = [1, 2, 3, 4, 5]
result = [num  for num in numbers if num % 2 ==1]
print(result)