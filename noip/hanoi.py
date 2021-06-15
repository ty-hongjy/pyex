def move(n, a, b, c):
	global count
    if n == 1:
        print(a, '-->', c)
        count+=1
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

a = input('请输入A柱盘子的个数：')
num = int(a)
print('把',num,'个盘子全部移到C柱子的顺序为：')
move(num, 'A', 'B', 'C')
print(count)

def hanoi(n, a, b, c):
    if n == 1:
        print(a + '--->' + c)
    else:
        hanoi(n-1, a, c, b)
        print(a + '--->' + c)
        hanoi(n-1, b, a, c)


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
