open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            is_it_true = (open_list[pos] == stack[len(stack) - 1])
            if ((len(stack) > 0) and is_it_true):

                stack.pop()
            else:
                return print("NO")
    if len(stack) == 0:
        return print("YES")
    else:
        return print("NO")

check(input())


# [{}{}]
# {[({})]}