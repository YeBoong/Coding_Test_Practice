name_list1 = ["봄", "여름", "가을", "겨울"]
name_list2 = ["고기", "소고기", "돼지고기"]
name_list3 = ["고기", "고기", "꽃"]

def solution(name_list):
    answer = False
    for i in range(0, len(name_list) - 1):
        if name_list[i] == name_list[i + 1]:
            answer = True

    name_list_copy = name_list

    for i in name_list:
        for j in name_list_copy:
            if i != j:
                if i in j:
                    answer = True

    return answer

print(solution(name_list1))
print(solution(name_list2))
print(solution(name_list3))