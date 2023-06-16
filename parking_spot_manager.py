class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    
    # __item 딕셔너리를 __init__ 밖에서 정의할 경우 parking_spot.__init__() missing 1 required positional argument: 'latitude' 오류 발생
    # --> __init__안에서 정의할 시 오류가 없다 라는 조언을 듣고 수정함
    
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = { 'name' : name,
                        'city' : city,
                        'district' : district,
                        'ptype' : ptype,
                        'longitude' :longitude,
                        'latitude' : latitude}

    def get(self, keyword=''):
        return self.__item.get(keyword, None)   #keyword에 해당하는 값을 반환하고, 그렇지 않으면 None을 반환
                                                #구글 파이썬 get 메소드 매개변수 keyword 검색 후 각종 블로그, 사이트 참조
                                                #Chat GPT 참조
        
        
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

def str_list_to_class_list(str_list):
    spots = []
    for line in str_list:
        data = line.split(',')   #쉼표로 구분되어있는 데이터를 나누기 위한 split 함수
        name = data[1]           #data[0]은 순번이므로 자원명부터 데이터를 저장하기 위해
        city = data[2]           #data[1]부터 실행함
        distract = data[3]       #자원명 ~ 주차유형은 문자열 값
        ptype = data[4]
        longitude = float(data[5])   #경도와 위도는 실수 값임으로 float으로 변환
        latitude = float(data[6])

        spot = parking_spot(name, city, distract, ptype, longitude, latitude)
        spots.append(spot)

    return spots

def print_spots(spots):
    print("---print elements({})---".format(len(spots)))   #print("---print elements(",len(spots),")---")로 실행시 ---print elements( 477 )---로 출력됨
    for spot in spots:                                     #https://blockdmask.tistory.com/424 참고 후 ---print elements(477)---로 출력 되도록 수정
        print(spot)


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")   #read_file 오타 수정
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)