#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 如果类把某个属性定义为序列，可以使用__getitem__()输出序列属性中的某个元素.
class FruitShop:
	# 获取序列的索引key对应的值，等价于seq[key]
	def __getitem__(self, i):  # 获取水果店的水果
		return self.fruits[i]  # 可迭代对象


# 假设水果店中销售多钟水果，可以通过__getitem__()方法获取水果店中的没种水果
if __name__ == "__main__":
	shop = FruitShop()
	print shop  # __main__.FruitShop instance
	shop.fruits = ["apple", "banana"]
	print shop[1]  # banana
	for item in shop:  # 输出水果店的水果
		print item,
