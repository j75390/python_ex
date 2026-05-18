# 회전하는 각도(angle)와 전진하는 길이(length)를 입력 받아 정육각형을 그려 봅시다.
# 정육각형의 내각은 60도입니다.

import turtle

t = turtle.Turtle()      # 그림 그리기 준비 완료!
t.shape('turtle')        # 아이콘 설정

angle = int(input('회전 각도를 입력하세요.'))             #72
length = int(input('전진 길이를 입력하세요'))              #100

t.left(angle)            # 왼쪽으로 angle(60)도 회전
t.forward(length)        # 100픽셀 실전 그리기

t.left(angle)            # 왼쪽으로 angle(60)도 회전
t.forward(length)        # 100픽셀 실전 그리기

t.left(angle)            # 왼쪽으로 angle(60)도 회전
t.forward(length)        # 100픽셀 실전 그리기

t.left(angle)            # 왼쪽으로 angle(60)도 회전
t.forward(length)        # 100픽셀 실전 그리기

t.left(angle)            # 왼쪽으로 angle(60)도 회전
t.forward(length)        # 100픽셀 실전 그리기

t.left(angle)            # 왼쪽으로 angle(60)도 회전
t.forward(length)        # 100픽셀 실전 그리기