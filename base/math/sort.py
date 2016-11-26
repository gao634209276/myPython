# coding=utf-8
"""
快排几个概念:活动指针,i,j指针,基准值base
初始基准base为arr[0],所以arr[0]相当于空位,所以i指针指向arr[0],
第一次与基准比较,先选择j指针值arr[j],这里有两种情况:
1.如果base < arr[j],将j指针向左移动,
2.如果 arr[j]< single_thread,应当讲arr[j]的值放在基准前,
这里由于i指针位置相当于空位,所以也就是填补arr[i],并将i指针右移动.
这时的j指针的位置相当于空位,而i指针是没有比较的位置,所以为了继续比较,
应该把活动指针更改为i,这个过程称作交叉移动,即活动指针在i/j指针之间发生变换
改进版本:
为了便于编程,需要在排序中保持活动指针一直为j,这里对发生交叉移动的情况做一下修改:
在出现交叉移动的条件后,仍然先将arr[j]填补i指针位置,同时i指针右移动,
然后在把i指针值arr[i]再填补到arr[j]位置,
此时也就是说i指针依旧是个空位,而j指针位置存放了新值,所以活动指针依旧选择j
"""


# 快排的实现
def quick_sort(arr, i, j):  # 快排总调用函数
    if i < j:
        base = kpgc(arr, i, j)
        quick_sort(arr, i, base)
        quick_sort(arr, base + 1, j)


def kpgc(arr, i, j):  # 快排排序过程
    base = arr[i]
    while i < j:
        while i < j and arr[j] >= base:  # 没有发生交叉移动,j指针前移,循环
            j -= 1
        # 要发生交叉移动,为了保持活动指针不跳,讲i指针值赋值给j指针位置,然后取出
        while i < j and arr[j] < base:
            arr[i] = arr[j]
            i += 1
            arr[j] = arr[i]
    arr[i] = base
    return i


'''
在arr中选择最小的数放在arr[0],并将arr[0]放在原来最小值的位置
然后再从arr[1]开始再选择最小位置放在arr[1],并将arr[1]的值放在原来第二小的位置
如此循环一直到子列长度为1为止
'''


# 选择排序的实现
def select(arr):  # 选择排序
    for i in range(0, len(arr)):  # 每一趟排序
        k = i  # 截止目前的最小值的标记位
        for j in range(i + 1, len(arr)):  # 每一趟选择最小的这个数
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]  # 交换位置


'''
二路归并排序
将arr按照索引从中间位置切分,一直切分到子列长度为1,
然后第一趟排序:
'''


# 二路归并排序
def gb(arr):  # 第一次归并排序，以及持续调用rg（）函数进行后续的归并排序
    arr_t = [[arr[0]]]  # 把传进去的数组的元素变为数组的形式，因为后续需要使用到
    k = 0
    m = ""
    if len(arr) % 2 == 0:  # 如果原数组长度为偶数，那么l的值为均分
        l = len(arr) / 2
    else:  # ……为奇数，那么l值为一半后再加一位
        l = len(arr) / 2 + 1
    for t in range(0, l):
        m = "h" + m
    arr_rg = list(m)  # m=="hhh"     ["h","h","h"]    #生成一个存储数据的列表arr_rg，此列表长度为l
    for i in range(1, len(arr)):
        arr_t = arr_t + [[arr[i]]]  # 生成一个列表，该列表将原列表的元素变为列表，即两层列表，
        # 因为我们要调用后面的rg函数，该函数数据类型为列表
    if len(arr_t) % 2 == 0:  # 进行第一次归并排序，首先进行元素个数为偶数的情况
        for i in range(0, len(arr_t), 2):  # 从第0为元素开始，每次增加2
            arr_rg[k] = dg(arr_t[i], arr_t[i + 1])  # 第i位与i+1位进行排列
            k += 1
    else:  # 若元素个数为奇数
        for i in range(0, len(arr_t) - 2, 2):  # 循环部分先进行偶数位数部分的排序，跟%2==0情况一样
            arr_rg[k] = dg(arr_t[i], arr_t[i + 1])
            k += 1
        arr_rg[k] = arr_t[len(arr_t) - 1]  # 偶数部分排完后，单出一位奇数位，直接将奇数位移到新存储数组arr_rg最后一位即可。
    n = 0
    while 1:  # 第一趟归并完成后，还需要进行后续的归并，那么后续的归并就一直调用arr_rg函数，直到长度为1停止
        if len(arr_rg) == 1:  # 长度为1的时候，不需要归并了，此时停止
            break
        else:
            arr_rg = rg(arr_rg)  # 否者调用arr_rg函数。调用的参数第一次是上述第一次归并的结果，
            # 第二次以及以后的参数是每一次的上一次arr_rg函数的执行结果
    return arr_rg


def rg(arr_rg):  # 依次对arr_rg进行二路归并
    k = 0
    s = len(arr_rg[0])  # s代表每组多少个元素，len(arr_rg)代表一共有多少组，l代表要比较多少次
    l = len(arr_rg)  # 代表一共有多少组
    if len(arr_rg) % 2 == 0:  # 如果组的个数为偶数
        for i in range(0, len(arr_rg), 2):
            arr_rg[k] = dg(arr_rg[i], arr_rg[i + 1])  # 将两个有序列表arr_rg[i],arr_rg[i+1]用dg函数合并为一个有序列表
            k += 1  # k为 排序后的数组arr_rg的下标
        arr_rg = arr_rg[:l / 2]  # 因为arr_rg由二合一，会产生多余元素，将多余的元素舍去
        return arr_rg
    else:  # 如果组的个数为奇数
        for i in range(0, len(arr_rg) - 2, 2):
            arr_rg[k] = dg(arr_rg[i], arr_rg[i + 1])
            k += 1
        arr_rg = arr_rg[:l / 2] + [arr_rg[len(arr_rg) - 1]]  # 上面用循环排完之后，最后还需要将最后一个奇数位放下来
        return arr_rg


def dg(arr1, arr2):  # 两个有序数列之间排序
    x = len(arr1)  # x为有序列表arr1的长度
    y = len(arr2)  # y为有序列表arr2的长度
    i = 0
    j = 0
    k = 0
    m = ""
    for t in range(0, x + y):
        m = "h" + m
    arr_ok = list(m)  # 生成一个列表，列表的长度为arr1与arr2的长度之和，因为合并之后长度加大
    while k <= x + y:  # 合并规律，k是一个计数器，从0开始，一直到遍历完整个长度为止
        if i == x:  # 临界情况，如果左边的指针已到头，如何办？
            for k in range(j, y):
                arr_ok[k + x] = arr2[k]  # 如果左边指针已到头，将右边的数据移动到最后即可
            return arr_ok
            break
        elif j == y:  # 临界情况，如果右边的指针已到头，如何办？
            for k in range(i, x):
                arr_ok[k + y] = arr1[k]  # 如果右边的指针已到头，把左边剩下的数据移到最后即可
            return arr_ok
            break
        if arr1[i] <= arr2[j]:  # 如果i指向的数据<=j指向的数据，没到头的时候，将小数据移到到arr_ok中i指针往右移即可，
            # 到头时，指针不再移动
            if i == x:
                arr_ok[k] = arr[i]
                k += 1
            else:
                arr_ok[k] = arr1[i]
                i += 1
                k += 1
        else:  # 如果i指针指向的数据>j指针指向的数据的话，与上相反
            if j == y:
                arr_ok[k] = arr[j]
                k += 1
            else:
                arr_ok[k] = arr2[j]
                j += 1
                k += 1
                # return arr_ok


'''
二分查找搜索算法
从中间位置对该值比较,如果大于中间位置值,则从右边继续查找
如果小于,则从左边继续查找
'''


def efss(arr, x):
    i = 0
    j = len(arr) - 1
    for k in range(j / 2 + 1):
        if i > j:
            print -1
        zj = (i + j) / 2  # 中间位置为i+j的和除以2
        if arr[zj] == x:
            return zj
        elif arr[zj] > x:
            j = zj - 1
        else:
            i = zj + 1
