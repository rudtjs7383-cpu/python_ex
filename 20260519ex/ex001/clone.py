#배터리 잔량을 표시하고 그에맞는 상태 메세지를 글자로 출력하는 프로그램을 만들자!
#배터리가 20이거나 20이하일때 출력하는메세지와, 21에서 79일때 출력하는메세지, 80일때 출력하는메세지도 입력하자.


# def check_battery (level):
# 
    # 
    # if  level <= 20:
        # return "경고:배터리가 부족합니다. 충전해주세요"
    # elif level < 80:
        # return "안정: 배터리상태가 충분합니다."
    # else:
        # return "정상: 동작중입니다."
# 
# 
# currentbattery = int(input('현재 배터리 상태를 사용자가 입력해주세요 : '))
# result = check_battery(currentbattery)
# print(result)

# 자판기에는 자판기에는 세 가지 음료수가 있습니다. (콜라: 1200원, 사이다: 1000원, 생수: 500원)

#사용자는 먼저 자판기에 돈을 투입합니다.

#음료수를 선택하면, 자판기는 돈이 충분한지 확인한 뒤 음료수를 주고 거스름돈을 계산해 줍니다.
def print_menu():
    """자판기의 메뉴와 가격을 보여주는 함수"""
    print("\n--- 🥤 미니 자판기 메뉴 ---")
    print("1. 콜라   : 1,200원")
    print("2. 사이다 : 1,000원")
    print("3. 생수   :   500원")
    print("---------------------------")

def get_price(choice):
    """선택한 번호에 맞는 음료수 가격을 알려주는 함수"""
    if choice == "1":
        return 1200
    elif choice == "2":
        return 1000
    elif choice == "3":
        return 500
    else:
        return 0

def start_vending_machine():
    """자판기를 작동시키는 메인 함수 (반복 구매 기능 포함)"""
    # 1. 처음 한 번만 돈을 입력받습니다.
    try:
        current_money = int(input("자판기에 넣을 금액을 입력하세요(원): "))
    except ValueError:
        print("🚨 숫자만 입력할 수 있습니다. 이용을 종료합니다.")
        return

    # 2. 남은 돈이 있는 동안 계속 반복하는 반복문(while)을 시작합니다.
    while True:
        print(f"\n💰 현재 잔액: {current_money}원")
        print_menu()
        
        # 음료수 선택 혹은 종료 선택 받기
        choice = input("구매할 음료수의 번호를 선택하세요 (종료하려면 'q' 입력): ").strip().lower()
        
        # 사용자가 종료를 원할 경우
        if choice == 'q':
            print("이용을 종료합니다.")
            break
            
        # 선택한 음료수의 가격 가져오기
        drink_price = get_price(choice)
        
        # 잘못된 번호를 입력했을 때 처리
        if drink_price == 0:
            print("🚨 잘못된 번호입니다. 다시 선택해주세요.")
            continue  # 아래 코드를 건너뛰고 다시 메뉴 선택으로 돌아감
            
        # 잔액이 부족한지 확인
        if current_money < drink_price:
            print("🚨 잔액이 부족합니다! 다른 음료를 고르거나 종료해주세요.")
            continue
            
        # 돈이 충분하다면 음료수를 주고 잔액을 차감합니다.
        current_money -= drink_price
        print("🍹 음료수가 나왔습니다! 덜컹~")
        
        # 만약 잔액이 가장 싼 음료수(생수 500원)보다 적게 남았다면 자동 종료
        if current_money < 500:
            print("\n🚨 잔액이 부족하여 더 이상 음료를 구매할 수 없습니다.")
            break

    # 3. 최종 반환되는 거스름돈 출력
    print(f"💵 최종 거스름돈은 {current_money}원입니다. 안녕히 가세요!")


# 프로그램 실행
if __name__ == "__main__":
    start_vending_machine()






















        
       
       



















































































