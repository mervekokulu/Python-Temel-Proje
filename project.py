def flatten(x):
    if len(x) == 0:
        return x
    if isinstance(x[0], list):
        return flatten(x[0]) + flatten(x[1:])
    return x[:1] + flatten(x[1:])

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))



def reverse_all(x):
    result = []
    for e in x:
        if isinstance(e, list):
            result.append(deep_reverse(e))
        else:
            result.append(e)
    result.reverse()
    return result

reverse_all([[1, 2], [3, 4], [5, 6, 7]])


def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result += flatten(item)
        else:
            result.append(item)
    return result

user_input = input()

user_list = eval(user_input)
flattened_list = flatten(user_list)
print( flattened_list)





def reverse_list(lst):
    reversed_lst=lst[::-1]
    for i in range(len(reversed_lst)):
        if type(reversed_lst[i])==list:
            reversed_lst[i]=reverse_list(reversed_lst[i])
    return reversed_lst

input_list=input()
parsed_list=eval(input_list)
reversed_list=reverse_list(parsed_list)
print(reversed_list)