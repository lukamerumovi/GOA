# def number_of_duplicate_digits(n):
#     return 9*10**(n-1)-9**n


# def sum_triangular_numbers(n):
#     return n*(n+1)*(n+2)/6 if n>0 else 0


# def array_diff(a, b):
#     return [x for x in a if x not in set(b)]


# def delete_nth(order,max_e):
#     ans = []
#     for o in order:
#         if ans.count(o) < max_e: ans.append(o)
#     return ans



# def shortest_steps_to_num(num):
#     steps = 0
    
#     while num != 1:
#         if num % 2:
#             num -= 1
#         else:
#             num //= 2
        
#         steps += 1
    
#     return steps