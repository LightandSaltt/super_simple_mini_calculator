import time

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

def devide(a, b):
    return a / b

def calculator():
    print("계산기를 실행합니다.")
    first_num = int(input("첫번째 숫자를 입력해 주세요. : "))
    calc_symbol = input("계산을 원하는 기호를 입력해 주세요. : ")
    second_num = int(input("두번째 숫자를 입력해 주세요. : "))
    time.sleep(1)
    if calc_symbol == "+":
        add(first_num, second_num)
    elif calc_symbol == "-":
        subtract(first_num, second_num)
    elif calc_symbol == "*":
        multiply(first_num, second_num)
    elif calc_symbol == "/":
        devide(round(first_num, second_num), 3)

select = int(input("1. 계산기 실행하기 / 2. 종료 : "))
if select == 1:
    calculator()
else:
    print("프로그램이 종료됩니다.")