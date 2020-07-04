A = [2, 3, 4, 3, 5]
B = [1, 6, 7]

def solution(A, B) :
    A_filter = []
    B_filter = []  
    sum_set = []
    complement_set = []
    intersect_set = []
    result_list = []
    for i in A:
        if i not in A_filter:
            A_filter.append(i)
            sum_set.append(i)
    
    for i in B:
        if i not in B_filter:
            B_filter.append(i)

    for i in B_filter:
        if i not in A_filter:
            sum_set.append(i)
        else:
            intersect_set.append(i)
    
    for i in sum_set:
        if i not in B_filter:
            complement_set.append(i) 

    sum_set.sort()
    result_list = [len(A_filter), len(B_filter), len(sum_set), len(complement_set), len(intersect_set)]

    print("A집합 : ", A_filter)
    print("B집합 : ", B_filter)
    print("합집합 : ", sum_set)
    print("차집합 : ", complement_set)
    print("교집합 : ", intersect_set)
    print(result_list)

solution(A,B)