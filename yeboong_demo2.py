

def solution(A, B) :
    A_filter = filter_set(A)
    B_filter = filter_set(B)
    sum_set = operater(A_filter, B_filter)[0]
    complement_set = operater(A_filter, B_filter)[1]
    intersect_set = operater(A_filter, B_filter)[2]
    result_list = [len(A_filter), len(B_filter), len(sum_set), len(complement_set), len(intersect_set)]

    print("A집합 : ", A_filter)
    print("B집합 : ", B_filter)
    print("합집합 : ", sum_set)
    print("차집합 : ", complement_set)
    print("교집합 : ", intersect_set)
    print(result_list)

def filter_set(array):
    array_filter = []
    for i in array:
        if i not in array_filter:
            array_filter.append(i)
    return array_filter

def operater(A, B):
    sum_set = A
    intersect_set = []
    complement_set = []
    all_set = []
    for i in B:
        if i not in A:
            sum_set.append(i)
        else:
            intersect_set.append(i)
    
    for i in sum_set:
        if i not in B:
            complement_set.append(i)
    
    sum_set.sort()
    all_set.append(sum_set)
    all_set.append(complement_set)
    all_set.append(intersect_set)

    return all_set

A = [1,2,3,2]
B = [1,3]
solution(A,B)