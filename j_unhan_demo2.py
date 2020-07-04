def solution(arrayA, arrayB):
    answer = []

    # A집합 - 중복제거
    answer.append(len(array_print(arrayA)))
    # B집합 - 중복제거
    answer.append(len(array_print(arrayB)))
    # 합집합
    answer.append(len(array_sum(arrayA, arrayB)))
    # 차집합
    answer.append(len(array_complement(arrayA, arrayB)))
    # 교집합
    answer.append(len(array_intersect(arrayA, arrayB)))

    return answer


def array_print(array): # 중복 제거
    array_new = list()
    for i in array:
        if i not in array_new:
            array_new.append(i)
    print("집합 = ", array_new)
    return array_new
    # return len(array_new)

def array_sum(arrayA, arrayB):
    array_sum = []
    for i in arrayA:
        if i not in array_sum:
            array_sum.append(i)
    for i in arrayB:
        if i not in array_sum:
            array_sum.append(i)
    return array_sum

def array_complement(arrayA, arrayB):
    arrayA = array_print(arrayA)
    arrayB = array_print(arrayB)
    for i in arrayB:
        if i in arrayA:
            arrayA.remove(i)
    return array_print(arrayA)

def array_intersect(arrayA, arrayB):
    array_intersect = list()
    for i in arrayA:
        if i in arrayB:
            array_intersect.append(i)
    return array_print(array_intersect)