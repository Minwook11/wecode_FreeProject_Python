# 프로그래머스 코딩 테스트 정렬 파트 - K값 찾기

def solution(array, commands):
    answer = []
    for i in commands :
        temp_array = array[int(i[0] - 1) : int(i[1])]
        print(temp_array)
        temp_array.sort()
        print(temp_array)
        value = temp_array[int(i[2] - 1)]
        print(value)
        answer.append(value)
    
    return answer

target_array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = solution(target_array, commands)

print(answer)

# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)) 1줄 답안;;;;