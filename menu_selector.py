import file_manager
import parking_spot_manager   #file_manager와 parking_spot_manager의 모듈을 사용하기위해 import 진행

def start_process(path):
    str_list = file_manager.read_file(path)   #file_manager모듈의 read_file함수를 호출하여 문자열 리스트를 반환받고,다시 이 문자열 리스트를 이용
    spots = parking_spot_manager.str_list_to_class_list(str_list)   #parking_spot객체의 리스트를 반환받음
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:   #parking_spot_manager모듈의 print_spots함수를 호출
            parking_spot_manager.print_spots(spots)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                print("not implemented yet")
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                print("not implemented yet")
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                print("not implemented yet")
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                print("not implemented yet")
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                print("not implemented yet")
                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")   #menu에서 4번 선택시 Exit을 출력하고 break을 통해 반복을 종료함
            break
        else:
            print("invalid input")