# def cookie(x):
#     if type(x) == str:
#         return "Who ate the last cookie? It was Zach!"
#     elif type(x) == int or type(x) == float:
#         return "Who ate the last cookie? It was Monica!"
#     elif type(x) != int or type(x) != str or type(x) != float:
#         return "Who ate the last cookie? It was the dog!"


# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# def goose_filter(birds):
#     for i in geese:
#         if i in birds:
#             birds.remove(i)
#     return birds


# def billboard(name, price=30):
#     num = 0
#     for i in range(0, len(name)):
#         num += price
#     return num        


# def get_real_floor(n):
#     if n <= 0:
#         return n
#     elif n < 13:
#         return n -1
#     elif n > 13:
#         return n -2


# def past(h, m, s):
#     return (h * 3600000) + (m * 60000) + (s * 1000)