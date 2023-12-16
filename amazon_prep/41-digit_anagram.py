def solution(a):
    count_dict = {}
    count = 0
    for num in a:
        sorted_digits = "".join(sorted(str(num)))
        if sorted_digits in count_dict:
            count += count_dict[sorted_digits]
            count_dict[sorted_digits] += 1
        else:
            count_dict[sorted_digits] = 1
    return count
    [].ins
# def solution(a):
#     i = 0
#     count = 0
#     while i < (len(a)):
#         first = a[i]
#         for j in range(i+1, len(a)):
#             second = a[j]
#             if is_anagram(first, second) == True:
#                 count +=1
#         i += 1
#     return count
        
        

# def is_anagram(num1, num2):
#     """ Check if two numbers are digit anagrams """
#     str_num1 = str(num1)
#     str_num2 = str(num2)
#     if len(str_num1) != len(str_num2):
#         return False
#     l1 = sorted(list(str_num1))
#     l2 = sorted(list(str_num2))
#     if l1 == l2:
#         return True
#     else:
#         return False
    
    
    
