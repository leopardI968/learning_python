# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def multi(a, b):
    return a * b


def my_max(array):
    # return max(array)
    cur_max = array[0]
    for d in array[1:]:
        if d > cur_max:
            cur_max = d
    return cur_max



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # a = 'sdjkfdkjf'
    # b = "asdfdfadsf"
    # print(a, len(a), a.endswith('kjz'))
    # t = True
    # if t and len(a) >= 9:
    #     print('Tryeeeee')
    # for c in a:
    #     print(c)
    arr = [-1, -2, -88, -35, -34, -10, -23, -12, -99, -11]
    arr2 = [5]
    # f = 0
    #
    # for i in arr:
    #     f += i
    #     print(f)
    # print(min(arr))
    odd_sum = not_odd_sum = 0
    for g in arr:
        if g % 2 == 1:
            not_odd_sum += g
        else:
            odd_sum += g

    print(f'odd sum: {odd_sum}, not odd summ {not_odd_sum} ')

    m = my_max(arr2)
    print(f'max of array = {m}')