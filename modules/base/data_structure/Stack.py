# coding=utf-8
# 栈的实现

class Stack():
	# 初始化栈主体为list,容量,栈底初始化位置
	def __init__(st, size):
		st.stack = []
		st.size = size
		st.top = -1

	# 入栈,判断栈是否满,然后对主体list最后append该帧,栈底指针+1
	def push(st, content):
		if st.Full():
			print "Stack is Full!"
		else:
			st.stack.append(content)
			st.top += 1

	# 出栈,判读是否空,对栈底指针-1
	def out(st):
		if st.Empty():
			print "Stack is Empty!"
		else:
			st.top -= 1

	def Full(st):
		if st.top == st.size:
			return True
		else:
			return False

	def Empty(st):
		if st.top == -1:
			return True
		else:
			return False
