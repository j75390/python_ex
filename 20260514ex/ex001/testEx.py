# PC방 자리 관리 프로그램 

# PC방 사장이고
# 손님이 자리에 앉으면 "사용중" 으로 바뀌고, 비어있으면 예약할 수 있다.

# seats = {
#     1: "빈자리",
#     2: "사용중",
#     3: "빈자리",
#     4: "사용중",
#     5: "빈자리"
# }
# 프로그램 요구사항
# 1.현재 자리 상태를 전부 출력하기
# 2. 사용자에게 원하는 자리 번호 입력받기
# 3.예약할 자리 번호 :
# 4.빈자리라면 "예약 완료" 출력 해당 자리 상태를 "사용중" 으로 변경 이미 사용중이라면 이미 사용중인 자리입니다 출력
# 5.예약 후 전체 자리 상태 다시 출력하기


# seats = {
#     1: "빈자리",
#     2: "사용중",
#     3: "빈자리",
#     4: "사용중",
#     5: "빈자리"
# }

# print("현재 좌석 상태:")
# for num, status in seats.items():
#     print(f"{num}번 자리: {status}")

# number = int(input("예약할 자리를 선택하세요: "))

# if seats[number] == "빈자리":
#     seats[number] = "사용중"
#     print("예약 완료!")
# else:
#     print("이미 사용중인 자리입니다.")

# print("예약 후 좌석 상태:")
# for num, status in seats.items():
#     print(f"{num}번 자리: {status}")


# - 배달 주문 통계 프로그램 
# 배달 앱에서 하루 주문 데이터를 분석하려고 한다.
# 주어진 주문 목록
# orders = [
#     "치킨",
#     "피자",
#     "치킨",
#     "햄버거",
#     "피자",
#     "치킨"
# ]
# 프로그램 요구사

# 1. 각 음식이 몇 번 주문됐는지 딕셔너리에 저장하기
# 2. 가장 많이 주문된 음식 찾기
# 3. 총 주문 개수 출력하기
# 4. 사용자가 음식 이름 입력하면
# 몇 번 주문됐는지 출력하기

# orders = [
#     "치킨",
#     "피자",
#     "치킨",
#     "햄버거",
#     "피자",
#     "치킨"
# ]

# order_count = {}
# for food in orders:
#     if food in order_count:
#         order_count[food] += 1
#     else:
#         order_count[food] = 1

# print("주문 통계:", order_count)

# most_ordered = max(order_count, key=order_count.get)
# print("가장 많이 주문된 음식:", most_ordered)

# print("총 주문 개수:", sum(order_count.values()))

# food_name = input("조회할 음식 이름을 입력하세요: ")
# print(f"{food_name} 주문 횟수:", order_count.get(food_name, 0))


# -시험 결과 분석 프로그램 
# 학원에서 시험 결과를 분석하려고 한다.
# 주어진 데이터
# scores = {
#     "민수": 88,
#     "지훈": 72,
#     "수아": 95,
#     "유진": 64,
#     "서연": 100
# }
# 프로그램 요구사항
# 1.전체 학생 점수 출력하기
# 2.평균 점수 계산하기
# 3.최고 점수 학생 찾기
# 4.60점 이상은 합격, 미만은 불합격 출력하기
# 5.90점 이상 학생 수 출력하기
# 6.점수 높은 순으로 학생 출력 도전하기

# scores = {
#     "민수": 88,
#     "지훈": 72,
#     "수아": 95,
#     "유진": 64,
#     "서연": 100
# }


# print("전체 학생 점수:")
# for name, score in scores.items():
#     print(f"{name}: {score}")

# average_score = sum(scores.values()) / len(scores)
# print("\n평균 점수:", average_score)

# top_student = max(scores, key=scores.get)
# print("최고 점수 학생:", top_student, scores[top_student])

# print("\n합격 여부:")
# for name, score in scores.items():
#     result = "합격" if score >= 60 else "불합격"
#     print(f"{name}: {result}")

# high_score_count = sum(1 for score in scores.values() if score >= 90)
# print("\n90점 이상 학생 수:", high_score_count)

# print("\n점수 높은 순 정렬:")
# sorted_students = sorted(scores.items(), key=lambda x: x[1], reverse=True)
# for name, score in sorted_students:
#     print(f"{name}: {score}")