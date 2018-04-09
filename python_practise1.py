
'''
2.1 列表元素去重并保持原来的顺序
列表内容：L1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
输出结果：['b', 'c', 'd', 'a']
'''

def list_distinct():
	L1 = ['b','c','d','b','c','a','a']
	L2=list(set(L1))
	L3=L2.sort(key=L1.index)
	print(L3)

def list_distinct2():
	L1 = ['b','c','d','b','c','a','a']
	L2 = []
	for x in L1:
		if x not in L2:
			L2.append(x)
	print(L2)

list_distinct()
list_distinct2()


'''
2.2 合并两个列表并保持合并后的列表顺序
L1 = [1, 2, 3, 4]
L2 = [2, 3, 7, 9]
输出结果：[1, 2, 2, 3, 3, 4, 7, 9]
'''

def list_join():
	L1 = [1, 2, 3, 4]
	L2 = [2, 3, 7, 9]
	L3=L1+L2
	L4=L3.sort()
	print(L3)

list_join()



'''
2.3 统计文本中各单词出现的次数
world = "I am very very very love python"
运行结果：
{'python': 1, 'love': 1, 'very': 3, 'am': 1, 'I': 1}
'''
import collections

def count_num():
	world = "I am very very very love python"
	L1=world.split(' ')
	num=collections.Counter(L1)
	print(num)


def count_num2():
	world = "I am very very very love python"
	L1=world.split(' ')
	L2=list(set(L1))
	d1={}

	for x in range(len(L2)):
		d1[L2[x]]=0
		for y in range(len(L1)):
			if L2[x]==L1[y]:
				d1[L2[x]]+=1

	print(d1)
			

count_num()
count_num2()

