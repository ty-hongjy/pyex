'''
Description: multi methods to step hanoi tower problem
Autor: hongjy
Date: 2023-03-23 15:50:23
LastEditors: hongjy
LastEditTime: 2025-07-15 15:05:35
'''
#this is version include step and golden disk number
def hanoi_with_step(n, a, b, c):
    global step
    step = 0
    def move(n, a, b, c):
        global count,step
        if n == 1:
            step+=1
            bin_step = bin(step)
            gold_num = len(bin_step) - bin_step.rfind('1') - 1
            print("step:",step,",gold disk num:",gold_num,",",a, '-->', c)
        else:
            move(n-1, a, c, b)
            move(1, a, b, c)
            move(n-1, b, a, c)

    # a = input('please input count of golden disk on A rod:')
    # num = int(a)
    print(f'the sequence that {n} disks move to C rod:')
    move(n, 'A', 'B', 'C')

#this is very simple version
def hanoi(n, a, b, c):
    if n == 1:
        print(a + '--->' + c)
    else:
        hanoi(n-1, a, c, b)
        print(a + '--->' + c)
        hanoi(n-1, b, a, c)

#include step and golden disk number
def hanoi_no_recursion(n):
    tower_belong = [0] * n
    if n % 2 == 0:
        tower_name = ['A', 'B', 'C']
    else:
        tower_name = ['A', 'C', 'B']
    for step in range(1, 2 ** n):
        bin_step = bin(step)
        gold_num = len(bin_step) - bin_step.rfind('1') - 1

        print(f"第 {step:2} 步：移动 {str(gold_num)} 号金片，从 {tower_name[tower_belong[gold_num]]} 塔到", end=' ')
        if gold_num % 2 == 0:
            tower_belong[gold_num] = (tower_belong[gold_num] + 1) % 3
        else:
            tower_belong[gold_num] = (tower_belong[gold_num] + 2) % 3
        print(tower_name[tower_belong[gold_num]], '塔')

if __name__ == '__main__':
    # n = int(input('请输入汉诺塔的层数：'))
    n = int(input('please input count of golden disk on A rod:'))
    # hanoi(n, 'A', 'B', 'C')
    # hanoi_no_recursion(n)
    hanoi_with_step(n,'A','B','C')