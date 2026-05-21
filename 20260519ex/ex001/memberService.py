# '''
# 처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
# 메뉴: 1.회원가입    2.로그인    3.특정 회원 정보 출력  4.모든 회원 정보 출력    99.종료
# 사용자가
# '1.회원가입'을 선택하면 회원ID, 회원PW, 회원Email, 회원Phone 정보를 입력받아 회원가입 진행한다.
# '2.로그인'을 선택하면 회원ID, 회원PW를 입력받아 로그인 '성공' 또는 '실패'를 출력한다.
# '3.특정 회원 정보 출력'를 선택하면 회원ID와 회원PW를 입력받아 일치하는 회원 정보를 모두 출력한다.
# '4.모든 회원 정보 출력'를 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
# '99.종료'를 선택하면 프로그램 종료 시킨다.

# 심심하면> 특정 회원의 회원ID와 회원PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해 보자!
# '''

SIGN_UP = 1
SIGN_IN = 2
PRINT_MY_INFO = 3
PRINIT_ALL_MEMBER_INFO = 4
SYSTEM_SHUTDOWN = 99

DEV_MOD = True

members = {}           # Database

if DEV_MOD:

    uIds = ['gildong', 'chanho', 'saeri']
    uPws = ['1234', '5678', '9012']
    uMails = ['gildong@gmail.com', 'chanho@naver.com', 'saeri@daum.net']
    uPhones = ['010-1234-5678', '010-9999-8888', '010-7777-6666']

    for n in range(len(uIds)):          # 3회 반복 ( 0, 1, 2 )
        members[uIds[n]] = {
            'uId': uIds[n],
            'uPw': uPws[n],
            'uMail': uMails[n],
            'uPhone': uPhones[n]
        }

# functionns START
def getSelectedMenuNum():
    selectedMenuNum = int(input('1.회원가입 2.로그인 3.특정 회원 정보 출력 4.모든 회원 정보 출력 99.종료'))
    return selectedMenuNum

def setNewMember(uId,uPw,uMail,uPhone):
    members[uId] = {
                'uId': uId,
                'uPw': uPw,
                'uMail': uMail,
                'uphone': uPhone
            }
def isNotMember(uId):
    if uId in members:
            print(f'{uId}는(은) 이미 사용중 입니다. 다시 확인하세요.')
            return True
    else:
        return False

def printAllMemberInfo(value):
    for key1, value1 in value.items():
                print(f'{key}: {value1}')
# functionns END


flag = True
while flag:

    userSelectedMenuNum = getSelectedMenuNum()

    if userSelectedMenuNum == SIGN_UP:        # 1.회원가입
        uId = input('Input member ID: ')
        if not isNotMember(uId):            # False: 회원이 없는경우(회원가입 진행x)   True: 회원이 있는겨우(회원가입 진행)
            uPw = input('Input member PW: ')
            uMail = input('Input member EMAIL: ')
            while True:
                if '@' not in uMail:
                    print('입력한 이메일 주소가 형식에 맞지 않습니다. ')
                    uMail = input('Input member EMAIL: ')
                else:
                    break

            uPhone = input('Input member PHONE: ')

            setNewMember(uId, uPw, uMail, uPhone)

            print('SING-UP SUCCESS!!')

            if DEV_MOD: print(f'members: {members}')

    elif userSelectedMenuNum == SIGN_IN:
        signInCount = 1
        while True:        # 2.로그인
            uId = input('Input member ID: ')
            uPw = input('Input member PW: ')

            if uId in members:
                uInfo = members[uId]
                if uInfo['uPw'] == uPw:
                    print('SIGN-IN SUCCESS!!')
                else:
                    print('SIGN-IN FAIL!!')
                    signInCount += 1
                    if signInCount > 3:
                        print('3회 이상 틀렸어요!!')
                        break
            else:
                print(f'존재 하지 않은 ID입니다. 다시 확인하세요.')

    elif userSelectedMenuNum == PRINT_MY_INFO:        # 3.나의 정보 출력
        uId = input('Input member ID: ')
        uPw = input('Input member PW: ')

        if uId in members:
            uInfo = members[uId]
            if uInfo['uPw'] == uPw:
                print('SIGN-IN SUCCESS!!')

                print('-' * 30)
                for key, value in uInfo.items():
                    print(f'{key}: {value}')
                print('-' * 30)

            else:
                print('SIGN-IN FAIL!!')
        else:
            print(f'존재 하지 않은 ID입니다. 다시 확인하세요.')

    elif userSelectedMenuNum == PRINIT_ALL_MEMBER_INFO:        # 4.모든 회원 정보 출력
        for key, value in members.items():
            print(f'{key}님의 정보------------')
            printAllMemberInfo(value)
            print('-' * 30)

    elif userSelectedMenuNum == SYSTEM_SHUTDOWN:       # 99.종료
        flag = False
        print('Good bye~')