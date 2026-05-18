# 데이터 입력(input data)
# input()

'''
print('데이터를 입력하세요.')
inputData = input()
print(inputData)
'''
'''
print('정수를 입력하세요.')
inputInteger = input()     # 6
print(inputInteger)        # 6
print(type(inputInteger))  # int
'''
'''
print('실수 입력하세요.')
inputFloat = input()     # 3.14
print(inputFloat)        # 3.14
print(type(inputFloat))  # str
'''

# print('논리형 데이터 입력하세요.', end='')  # 논리형 데이터 입력하세요. (자동개행)
# inputBoolean = input()          # True
# print(inputBoolean)             # True
# print(type(inputBoolean))       # str


# inputBoolean = input('논리형 데이터 입력하세요.\n')
# print(inputBoolean)        # True
# print(type(inputBoolean))  # str

'''
# 자료(data)형을 변환해야 합니다. data type casting
userInputData = input('사용자야~~~~ 정수 입력해라~')    # 10
print(userInputData)                                 # 10
print(type(userInputData))                           # str
userInputData = int(userInputData)                                   # str --> int
print(type(userInputData))                           # str
'''

# str -> boolean
# userInputData = input('true or False 입력하세요')
# print(userInputData)                           # True
# print(type(userInputData))                     # str
# userInputData = bool(userInputData)
# print(type(userInputData))                     # boolean


# str -> float
# userInputData = input('실수 입력하세요.')
# print(userInputData)
# print(type(userInputData))              # str
# userInputData = float(userInputData)
# print(type(userInputData))              # float

# userInputData = 'True'
# userInputData = bool(userInputData)
# print(type(userInputData))

# x = 3              # int   3
# y = float(x)       # int -> float
# print(y)           # 3.0

# x = 3.141592
# y = int(x)
# print(y)             # 3
# print(float(y))      # 3.0

# korScore = input('국어점수:')
# engScore = input('영어점수:')
# mathScore = input('수학점수:')

# print(f'국어 점수 : {korScore}')
# print(f'영어 점수 : {engScore}')
# print(f'수학 점수 : {mathScore}')


# firstNum = int(input("첫 번째 정수 입력: "))
# secondNum = int(input("두 번째 정수 입력: "))

# sum = firstNum + secondNum
# average = sum / 2

# print(f'합:{sum}')
# print(f'평균:{average}')

# firstNum = int(input("첫 번째 정수 입력: "))
# secondNum = int(input("두 번째 정수 입력: "))

# print(f'합: {firstNum + secondNum}')
# print(f'평균: {(firstNum + secondNum) / 2}')

var1 = 10
var2 = 20

print(f'var1: {var1}, var2: {var2}')

temp = var1
var1 = var2
var2 = temp
print(f'varl: {var1}, var2: {var2}')