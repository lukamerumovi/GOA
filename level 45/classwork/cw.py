# def evaluate(equation):
#     a, *numbers = map(int, equation.split(" @ "))
    
#     for b in numbers:
#         if b == 0:
#             return None
        
#         a = (a + b) + (a - b) + (a * b) + (a // b)
    
#     return a



# def isValidWalk(walk):
#     return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')



# def expanded_form(num):
#     num = str(num)
#     st = ''
#     for j, i in enumerate(num):
#         if i != '0':
#             st += ' + {}{}'.format(i, (len(num[j+1:])*'0'))
#     return st.strip(' +')