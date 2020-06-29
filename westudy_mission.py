def dic_Print_All(dic) :
    for k in dic.keys() :
        print(dic[k])

def string_Print_All(string) :
    for i in range(len(string)) :
        if i == (len(string) - 1) :
            print(string[i])
        else :
            print(string[i], end ='')

def list_Print_All(list) :
    for j in range(len(list)) :
        if j == (len(list) - 1) :
            print(list[j])
        else :
            print(list[j], end =' ')

def break_Continue(list) :
    for i in range(len(list)) :
        if i == 1 :
            continue
        elif i == 8 :
            print('')
            break
        else :
            print(list[i], end =' ')

def list_Method_Test() :
    print("입력할 수의 개수 : ", end = '')
    index = input()
    temp_list = []

    for i in range(0, int(index)) :
        print("수 입력 : ", end = '')
        temp_list.append(int(input()))

    print("입력 직후 리스트 : ", end = '')
    list_Print_All(temp_list)
    temp_list.sort()
    print("정렬 후 리스트 : ", end = '')
    list_Print_All(temp_list)
    temp_list.pop(0)
    print("값 추출 후 리스트 : ", end = '')
    list_Print_All(temp_list)

test_string = "This is TEST string."

test_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b_c_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

bts_dic = {'Jin' : ['김석진', '1992-12-04', 180, 63, 'O'],
            'Suga' : ['민윤기', '1993-03-09', 173, 59, 'O'],
            'J-hope' : ['정호석', '1994-02-18', 177, 65, 'A'],
            'RM' : ['김남준', '1994-09-12', 181, 67, 'A'],
            'Jimin' : ['박지민', '1995-10-13', 173, 60, 'A'],
            'V' : ['김태형', '1995-12-30', 179, 63, 'AB'],
            'Jungkook' : ['전정국', '1997-09-01', 178, 66, 'A']
        }

dic_Print_All(bts_dic)
string_Print_All(test_string)
list_Print_All(test_list)
break_Continue(b_c_list)
list_Method_Test()