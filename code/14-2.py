print("20117894 조혜원\n")

def display_menu():
 print("1. 미터를 마일로 변환하기")
 print("2. 마일을 미터로 변환하기")
 print("3. 종료")
 print()
 
def meters_to_miles(meters):
    print(meters, "미터는 ", (meters / 1609.344), "마일입니다.\n")
 
def miles_to_meters(miles):
    print(miles, "마일은 ", (miles * 1609.344), "미터입니다.\n")



while True:
    display_menu()
    num = int(input("숫자 선택 : "))
    if num == 3:
        print("종료합니다.")
        break
    else:
        distance = float(input("값 입력 : "))
        if num == 1:
            meters_to_miles(distance)
        else:
            miles_to_meters(distance)
