# 국가별 인구수 통계

'''
Description

국가별 인구수 저장되어 있는 csv형식의 파일(엑셀로 열수 있는 콤마로 구분된 파일)(population.csv)에서 국가별 인구수를 가져와서, 화면에 인구수가 가장 많은 국가, 중위에 해당하는 국가를 출력하고 국가별 인구수의 평균을 출력하는 함수get_population()을 작성하시오.


함수 get_population()

함수동작
파일(population.csv)에서 인구수가 가장 많은 국가이름과 인구수를 출력하고
인구수의 median에 해당하는 국가와 인구수를 출력하고
Average 인구수를 소수점 2자리까지 출력하는 함수를 작성하시오

매개변수
없음

반환값
없음
'''

'''
함수 사용예시

get_population()
'''

'''
실행결과

China:1402393160
Costa Rica:5058007
Average:31787881
'''

# Code
def get_population():
    '''get data from population.csv'''
    population_dict = {}
    big_country = ''
    big_population = 0
    population_sum = 0
    with open('population.csv', 'rb') as f:
        population_chart = f.read()

    '''data processing'''
    chart_list = population_chart.split(b'\n')
    for country_data in chart_list[1:-1]:
        #print(country_data)
        rank, country, population, *others = country_data.split(b',')
        #print(country, population)
        population_dict[country] = int(population)
        population_sum += int(population)

        '''printing country and population most people live in'''
        if int(population) > big_population:
            big_country = country.decode('ascii')
            big_population = int(population)
    print('%s' % big_country[1:] + ':' + '%s' % big_population)

    '''printing country and population of median populaion'''
    Sorted_population_list = sorted(population_dict.items(), key=lambda x: x[1])
    if len(Sorted_population_list)%2 == 0:
        print("There's no median country. The median value is in the scope between", Sorted_population_list[int(len(Sorted_population_list) / 2) - 1], 'and', Sorted_population_list[int(len(Sorted_population_list) / 2)] )
    else:
        median_country, median_population = Sorted_population_list[int((len(Sorted_population_list) + 1) / 2 - 1)]
    median_country = median_country.decode('ascii')
    print(median_country[1:] + ':' + '%s' % median_population)

    '''printing Average population'''
    Average_population = population_sum/len(population_dict)
    print('Average:' + '%.2f' % Average_population)
    print(len(Sorted_population_list))

get_population()
