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
                                                #구글 파이썬 get 메소드 매개변수 keyword 검색 후 위에서부터 십수개의 블로그, 사이트 등 참조
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

#프로젝트 3 함수 구현 참고 문헌 https://sf2020.tistory.com/191
#https://butter-shower.tistory.com/205
#https://likethefirst.tistory.com/entry/Python-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%ED%95%A8%EC%B6%95-List-Comprehension
#https://leedakyeong.tistory.com/entry/python-for%EB%AC%B8-if%EB%AC%B8-%ED%95%9C-%EC%A4%84%EB%A1%9C-%EC%BD%94%EB%94%A9%ED%95%98%EA%B8%B0
#https://www.zinnunkebi.com/python-in-notin-op/

def filter_by_name(spots, name):
    return [spot for spot in spots if name in spot.get('name')]           

def filter_by_city(spots, city):
    return [spot for spot in spots if city in spot.get('city')]


def filter_by_district(spots, district):
    return [spot for spot in spots if district in spot.get('district')]


def filter_by_ptype(spots, ptype):
    return [spot for spot in spots if ptype in spot.get('ptype')]

                                            #location 튜플 생성 과정에서 filter_by_location 함수 내에서 생성 후 구현하려 헀지만
                                            #각 변수들을 읽지 못하는 문제가 발생 --> location을 밖으로 빼네어 구현하려 했지만,
                                            #min_lat <= spot.get('latitude') <= max_lat and min_lon <= spot.get('longitude') <= max_lon
def filter_by_location(spots, location):    #구현 시 정보를 못 받음 --> 조언을 통해 location[i] 형식으로 만들면 해결됨을 이해하고 이로 수정함
    return [spot for spot in spots if location[0] <= spot.get('latitude') <= location[1] and location[2] <= spot.get('longitude') <= location[3]]


def sort_by_keyword(spots, keyword):        #https://sennieworld.tistory.com/46 블로그 참조 후 해당 함수 작성
    return sorted(spots, key=lambda spot: spot.get(keyword))

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")   #read_file 오타 수정
    spots = str_list_to_class_list(str_list)                           #test 실행을 위해 ./input/free_parking_spot_seoul.csv --> ./input/free_parking_spot.csv 로 변경
    # print_spots(spots)                                               #version#4 test를 위해 다시 ./input/free_parking_spot_seoul.csv로 복구

    # version#3
    # spots = filter_by_city(spots, '인천')   #다른 예제들도 정상적으로 작동하는지 실험 확인하기 위해 filter_by_~~~(spots, '~~') 여러가지 실행
    # print_spots(spots)
    
    # version#4
    spots = sort_by_keyword(spots, 'ptype')   #version#4도 마찬가지로 다른 예제들의 정상작동을 확인하기 위해
    print_spots(spots)                        #spots = sort_by_keyword(spots, '~~~')를 바꿔가며 실행