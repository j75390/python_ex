# 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
#  [3, 7, 1, 9, 5]

# numbers = [3, 7, 1, 9, 5]
# print(f'numbers: {numbers}')
# print(f'가장 큰 숫자: {max(numbers)}')

# nums = [3, 7, 1, 9, 5]
# maxNum = 0
# for num in nums:
#     if num > maxNum:     # maxNum:9 num:5 > maxNum = 9
#         maxNum = num

# print(f'maxNum: {maxNum}')

# 2. 사용자에게 숫자 입력받아서
# 1부터 입력한 숫자까지 합계 출력하기 ( 5 )

# num = int(input('숫자입력 '))
# total = 0

# for i in range(1, num + 1):
#     total += i

# print(f'합계: {total}')

# 3. 리스트에 있는 숫자 중 짝수만 출력하기
#  [1,2,3,4,5,6]

# numbers = [1,2,3,4,5,6]

# print(f'짝수: ', end=' ')

# for i in numbers:
#     if i % 2 == 0:
#         print(i, end=' ')

# 4. 리스트 숫자를 오름차순 정렬하기
# [5,1,7,3]

# numbers = [5,1,7,3]

# numbers.sort()
# print(f'numbers: {numbers}')


# 5. 리스트 숫자를 내림차순 정렬하기
#  [5,1,7,3]

# numbers = [5,1,7,3]

# numbers.sort(reverse=True)
# print(f'numbers: {numbers}')


# 6. 리스트 안 숫자의 평균 구하기 [10,20,30]

# numbers = [10,20,30]

# average = sum(numbers) / len(numbers)

# print(f'평균값: {average}')

# numbers = [10,20,30]
# total = 0
# average = 0

# for numbers in numbers:
#     total += numbers

# average = total / len('numbers')

# print(f'total: {total}')
# print(f'average: {average}')


# 7. 리스트에서 가장 작은 숫자 찾기
#  (min() 사용 금지)

# import random

# numbers = []

# for i in range(5):
#     numbers.append(random.randint(1, 101))

# print(numbers)

# smallnum = numbers[0]

# for i in numbers:
#     if i < smallnum:
#         smallnum = i

# print(f'가장 작은 숫자: {smallnum}')

# nums = [3, 7, 1, 9, 5]
# minNum = nums[0]
# for num in nums:
#     if num < minNum:
#         minNum = num
# print(f'minNum: {minNum}')    # 1


# 8. 1부터 100까지 숫자 중
# 3의 배수와 5의 배수 출력하기

# print('3의 배수: ', end=' ')

# for i in range(1,101):
#     if i % 3 == 0:
#         print(i, end=' ')

# print()

# print('5의 배수: ', end=' ')

# for i in range(1,101):
#     if i % 5 == 0:
#         print(i, end=' ')

# for num in range(1,101):
#     if num % 3 == 0:
#         print(f'{num}은 3의 배수입니다.')

# for num in range(1,101):
#     if num % 5 == 0:
#         print(f'{num}은 5의 배수입니다.')

# 9. 사용자가 입력한 숫자를 리스트에 저장하다가
# 0 입력하면 종료 후 리스트 출력하기
# [입력: 3 ,입력: 7, 입력: 2 ,입력: 0]

# numbers = []

# while True:

#     number = int(input('숫자를 입력하세요: '))

#     if number == 0:
#         break

#     numbers.append(number)

# print(numbers)


# nums = []

# while True:
#     userInputNumber = int(input('정수 입력: '))

#     if userInputNumber == 0:
#         break

#     nums.append(userInputNumber)

# print(f'nums: {nums}')