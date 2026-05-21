# 지역변수 vs 전역변수
# 지역변수는 함수 내부에서 선언된 변수로 함수 내부에서만 사용 가능합니다.
# 전역변수는 함수 외부에서 선언된 변수로 함수 내/외부에서만 사용 가능합니다.

'''
cannot access local variable 'num' where it is not associated with a value
'''

# num = 10

# def fun():
#     # num = 20                 # 지역변수
#     global num
#     num = num + 1              # 데이터 수정 num(전역변수) = 10 + 1
#     print(f'num: {num}')     # 10, 전역변수 num > 20, 전역변수 num

# print(f'num: {num}')         # 10, 전역변수 num

# fun()

'''
global 키워드는 함수 내에서 전역변수의 값을 '수정'하고자 할때 반드시 명시하자!
'''

# quiz) 웹사이트의 누적방문 횟수 프로그램
# 웹사이트 방문 여부를 입력받아 웹사이트의 누적 방문 횟수를 출력해봅시다.

# flag = True
# totalVisitor = 0

# def countVisitor():
#     global totalVisitor
#     totalVisitor += 1

# while flag:
#     selectedMenuNum = int(input('1.웹사이트 방문   2.종료'))

#     if selectedMenuNum == 1:
#         countVisitor()
#         print(f'누적 방문 횟수: {totalVisitor}')

#     else:
#         flag = False
#         print('Good bye~')


# 매개변수(************************************)
# 매개: 둘 사이에서 양편의 '관계를 맺어' 줌

# 함수를 사용하기 위해 먼저 함수를 정의하고 필요할 때 호출하죠.
# 이 때 함수를 정의하는 쪽을 함수 정의부(선언부), 함수를 호출하는 쪽을 호출부하고 합니다.

# 함수를 호출할 때 데이터를 넘겨줄 수 있는데 이 데이터를 '인수'라고 합니다.
# 함수 정의부는 인수를 받으면 '매개변수'라는 변수에 저장합니다. 그리고 매개변수는 지역변수의 일종입니다.

# def greet(name, age):
#     # name = '홍길동' or '박찬호' or '박세리'
#     print(f'{name}님 안녕하세요. 나이는 {age}입니다.')

# greet('홍길동', 25)
# greet('박찬호', 20)
# greet('박세리', 30)

# def forecastWeather(temp, humi, rain):
#     print('날씨 예보입니다.')
#     print(f'최고 온도: {temp}도')
#     print(f'평균 습도: {humi}%')
#     print(f'비율 확율: {rain}%')

# forecastWeather(35, 70 ,80)

# 인수의 개수를 모르는 경우
# 우리 학급 학생들의 시험점수 총합과 평균을 구하는 함수를 만들자!
# 우리 학습 학생수는 총 3명이다.

# 3명
# def printScoresForStudent(subject, *scores):          # 리스트(list) > 튜플(tuple)
    
#     print(f'scores type: {type(scores)}')    # tuple
#     print(f'scores length: {len(scores)}')    # 4

#     totalScore = 0
#     for score in scores:
#         totalScore += score

#     print(f'{subject} 과목 총합: {totalScore}')
#     print(f'{subject} 과목 평균: {totalScore / len(scores)}')

# # # 90, 80, 100
# printScoresForStudent('국어', 90, 80, 100, 90, 50)

'''
선생님이 몇 명일지 모르는 학생의 점수를 입력한다.
이때 학생 점수의 종합과 평균을 구하는 함수를 만들고 이를 이용하는 프로그램을 만들어보자!
'''

# flag = True
# studentScores = []

# def printScoresForStudent(scores):          # scores = [,,,,,,,]
#     if len (scores) == 0:
#         print('학생수가 0명이라 총점과 평균을 구할 수 없습니다.')
#     else:
#         totalScore = 0
#         for scores in scores:
#             totalScore += 0

#     totalScore = 0
#     for score in scores:
#         totalScore += score

#     average = totalScore / len(scores)      # 0 / 0
#     print(f'총점: {totalScore}')
#     print(f'평점: {average}')

# while flag:
#     selectedMenuNum = int(input('1.학생 점수 입력      2.종료'))
#     if selectedMenuNum == 1:
#         score = int(input('학생 점수 입력: '))
#         studentScores.append(score)
#     else:
#         flag = False

# printScoresForStudent(studentScores)

# quiz) SMS와 MMS 구별하기
'''
문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다. 그런데 100자를 
넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다. 단문과 장문을 구별해서 돈을 부
과하는 프로그램을 만들어봅시다.
'''

# def sendUserMessage(str):
#     strLength = len(str)
#     print(f'사용자가 입력한 문자 길이: {strLength}')

#     if strLength <= 100:
#         print(f'SMS 발송 완료!')
#         print(f'50분 부과!')
#     else:
#         print(f'MMS 발송 완료!')
#         print(f'100분 부과!')

# inputData = input('문자 입력')
# sendUserMessage(inputData)

# 인수와 매개변수의 순서가 일치하지 않을 경우
# def printMemberInfo(name, email, major, grade):
#     print(f'Name\t: {name}')
#     print(f'Email\t: {email}')
#     print(f'Major\t: {major}')
#     print(f'Grade\t: {grade}')
#     print('----------------------------')

# # printMemberInfo('Hong Gildong', "gildong@gmil.com", "art", 1)

# # printMemberInfo(email = "gildong@gmil.com",
# #                 name ='Hong Gildong',
# #                 major = "art",
# #                 grade = 1)


# def printMemberInfo(info):
#     print(f'name: {info['name']}')
#     print(f'email: {info['email']}')
#     print(f'major: {info['major']}')
#     print(f'grade: {info['grade']}')

# printMemberInfo({'major': 'art',
#         'grade': '1',
#         'name': 'Hong glidom',
#         'email': 'gildong@gmail.com'
#     })

# printMemberInfo(memberInfo)

# 매개변수의 기본값 설정
# 직원 급여 지급 프로그램을 만들어보자!
# def setSalary(name, pay = 200):
#     print(f'{name}의 급여 {pay}원 지급!!')

# setSalary('박찬호', 400)
# setSalary('박세리', 600)
# setSalary('박용태')

# 데이터 반환(return)
# 데이터 반환이란, 함수는 실행이 끝난 후에 결과물(값)을 호출부로 반환할 수 있습니다.
# 이때 사용하는 키워드가 return입니다.
# 덧셈 연산 함수를 만들어 결과를 출력하는 프로그램을 만들어보자!

# def printResult(value):
#     print(f'result: {value}')

# def addFuntion(n1, n2):
#     sum = n1 + n2         # 30
#     # print(f'결과 값: {sum}')
#     printResult(sum)
#     return sum

# result = addFuntion(10, 20)
# print(f'result: {result}')

# DEV_MOD = True

# def fun1():
#     print('222222222')
#     if DEV_MOD == True:
#         print('111111111')
#         return
#     print('333333333')

# fun1()

# 별탑 만들기
# def increaseStart(limitStarCount):
#     print('*')
#     print('**')
#     print('***')
#     print('****')
#     print('*****')
#     print('******')
#     print('*******')
#     print('********')
#     for n in range(1, 8):
#         print('*' * n)
#         if n == limitStarCount:
#             break

# increaseStart(5)

# 7 ~ 8교시
# Toy 프로젝트 진행
'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1.회원가입    2.로그인    3.특정 회원 정보 출력  4.모든 회원 정보 출력    99.종료
사용자가
'1.회원가입'을 선택하면 회원ID, 회원PW, 회원Email, 회원Phone 정보를 입력받아 회원가입 진행한다.
'2.로그인'을 선택하면 회원ID, 회원PW를 입력받아 로그인 '성공' 또는 '실패'를 출력한다.
'3.특정 회원 정보 출력'를 선택하면 회원ID와 회원PW를 입력받아 일치하는 회원 정보를 모두 출력한다.
'4.모든 회원 정보 출력'를 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'99.종료'를 선택하면 프로그램 종료 시킨다.

심심하면> 특정 회원의 회원ID와 회원PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해 보자!
'''

# signUp = 1
# logIn = 2
# search_one = 3
# search_all = 4
# exit = 99

# members = {}

# while True:
#     print('1. 회원가입')
#     print('2. 로그인')
#     print('3. 특정 회원 정보 출력')
#     print('4. 모든 회원 정보 출력')
#     print('99. 종료')
#     menu = int(input('메뉴를 선택해주세요:'))

#     if menu == signUp:
#         print('======= 회원가입 =========')
#         user_id = input('아이디를 입력하세요: ')
#         if user_id in members:
#             print('이미 존재하는 아이디입니다.')
#         else:
#             passwored = input('비밀번호를 입력하세요: ')
#             user_email = input('이메일을 입력하세요: ')
#             user_phone = input('전화번호를 입력하세요: ')
#             members[user_id] = {
#                 'passwored': passwored,
#                 'email': user_email,
#                 'phone': user_phone,
#             }
#             print('회원가입 완료!')

#     if menu == logIn:
#         print('======== 로그인 =========')
#         user_id = input('아이디를 입력하세요: ')
#         passwored = input('비밀번호를 입력하세요: ')
#         if user_id in members and members[user_id]['passwored'] == passwored:
#             print(f'{user_id}님 로그인 성공!')
#         else:
#             print('아이디 또는 비밀번호가 틀렸습니다. ')

#     if menu == search_one:
#         print('=========특정 회원 정보 출력=========')
#         user_id = input('조회할 아이디를 입력하세요: ')
#         if user_id in members:
#             info = members[user_id]
#             print(f'아이디: {user_id}, 이메일: {info['email']}, 전화번호: {info['phone']}')
#         else:
#             print('존재하지 않는 아이디입니다. ')

#     if menu == search_all:
#         print('=========모든 회원 정보 출력=========')
#         if not members:
#             print('등록된 회원이 없습니다.')
#         else:
#             for uid, info in members.items():
#                 print(f'아이디: {uid}, 이메일: {info['email']}, 전화번호: {info['phone']}')

#     if menu == exit:
#         print('=========종료=========')
#         print(f'다음에도 이용해주세요')
#         break



#  GUI_tkinter 사용 버전

# import tkinter as tk
# from tkinter import messagebox

# members = {}

# def signup():
#     user_id = entry_id.get()
#     password = entry_pw.get()
#     email = entry_email.get()
#     phone = entry_phone.get()

#     if user_id in members:
#         messagebox.showerror("회원가입 실패", "이미 존재하는 아이디입니다.")
#     else:
#         members[user_id] = {
#             "password": password,
#             "email": email,
#             "phone": phone
#         }
#         messagebox.showinfo("회원가입 성공", f"{user_id}님 회원가입 완료!")

# def login():
#     user_id = entry_id.get()
#     password = entry_pw.get()

#     if user_id in members and members[user_id]["password"] == password:
#         messagebox.showinfo("로그인 성공", f"{user_id}님 로그인 성공!")
#     else:
#         messagebox.showerror("로그인 실패", "아이디 또는 비밀번호가 틀렸습니다.")

# def show_user():
#     user_id = entry_id.get()
#     if user_id in members:
#         info = members[user_id]
#         messagebox.showinfo("회원 정보", f"아이디: {user_id}\n이메일: {info['email']}\n전화번호: {info['phone']}")
#     else:
#         messagebox.showwarning("조회 실패", "존재하지 않는 아이디입니다.")

# def show_all():
#     if not members:
#         messagebox.showwarning("회원 없음", "등록된 회원이 없습니다.")
#     else:
#         all_info = ""
#         for uid, info in members.items():
#             all_info += f"아이디: {uid}, 이메일: {info['email']}, 전화번호: {info['phone']}\n"
#         messagebox.showinfo("모든 회원 정보", all_info)

# # Tkinter 윈도우 생성
# root = tk.Tk()
# root.title("회원 관리 프로그램")

# # 입력창
# tk.Label(root, text="아이디").grid(row=0, column=0)
# entry_id = tk.Entry(root)
# entry_id.grid(row=0, column=1)

# tk.Label(root, text="비밀번호").grid(row=1, column=0)
# entry_pw = tk.Entry(root, show="*")
# entry_pw.grid(row=1, column=1)

# tk.Label(root, text="이메일").grid(row=2, column=0)
# entry_email = tk.Entry(root)
# entry_email.grid(row=2, column=1)

# tk.Label(root, text="전화번호").grid(row=3, column=0)
# entry_phone = tk.Entry(root)
# entry_phone.grid(row=3, column=1)

# # 버튼
# tk.Button(root, text="회원가입", command=signup).grid(row=4, column=0)
# tk.Button(root, text="로그인", command=login).grid(row=4, column=1)
# tk.Button(root, text="특정 회원 조회", command=show_user).grid(row=5, column=0)
# tk.Button(root, text="모든 회원 조회", command=show_all).grid(row=5, column=1)

# root.mainloop()