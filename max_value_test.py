# 프로그래머스 코딩 테스트 정렬 파트 - 가장 큰 수

from itertools import permutations

def solution (numbers) :
    answer = []
    value = []
    allways = list(permutations(numbers, len(numbers)))

    for i in allways :
        test = ''
        for j in range(len(numbers)) :
            test = test + '{}'.format(i[j])
        value.append(test)
    answer = max(value)
    return answer

numbers1 = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]

answer = solution(numbers1)

print(answer)

# def solution(numbers):
#     numbers = list(map(str,numbers)) 
#     numbers.sort(key=lambda x: x * 3, reverse=True) 
#     if sum(list(map(int,numbers))) == 0:
#     	numbers = list(set(numbers))
#     return "".join(numbers)               

# def solution(numbers): 
#     l = [] 
#     for number in numbers: 
#         original = str(number) 
#         number = list(str(number)) 
#         i = 0 
#         while len(number) <= 4: 
#             number.append(original[i]) i = (i + 1) % len(original) 
#             number = int("".join(number)) 
#             l.append([number, original]) 
#     l = sorted(l, reverse=True) 
#     return str(int("".join([item[1] for item in l])))