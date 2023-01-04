def solution(cacheSize, cities):
    answer = 0
    
    # 캐시에 저장 되는 데이터 리스트
    cache = []
    
    
    for city in cities:
        # 캐시 데이터를 확인 하기 위해 모든 문자열은 소문자로 변경
        l_city = city.lower()
        
        # 캐시에 있는 판별 여부 변수
        find = False
        
        #캐시 리스트에 이미 있다면 해당 데이터를 삭제 후 뒷 부분에 재입력
        for i in range(len(cache)):
            if cache[i] == l_city:
                cache.pop(i)
                cache.append(l_city)
                answer += 1
                find = True
                break
        
        # 캐시 리스트에 없다면 새로운 데이터 추가
        if not find:
            cache.append(l_city)
            answer += 5
            
            # 캐시사이즈 초과라면 추가 된지 가장 오래된 데이터, 즉 0번 인덱스 삭제
            if len(cache) > cacheSize:
                cache.pop(0)

    return answer