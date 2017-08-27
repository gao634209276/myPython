正则表达式符号与方法
密码：hadkfalifexxIxxfasdjifja134xxlovexx23345sdfxxyouxx8dfse
解密：I love you
解密方法：找规律	xx需要的内容xx

常用符号：点号，星号，问号与括号
常用方法：findall，search，sub
正则表达式符号与方法 — 常用符号
	.  :  匹配任意字符，换行符\n除外
	* ：匹配前一个字符0次或无限次
	? ：匹配前一个字符0次或1次
	.*：贪心算法
	.*?：非贪心算法
	（）：括号内的数据作为结果返回

效果展示
	findall： 匹配所有符合规律的内容，返回包含结果的列表
	Search：匹配并提取第一个符合规律的内容，返回一个正则表达式对象（object)
	Sub：替换符合规律的内容，返回替换后的值

常用技巧
	import re
	from re import *
	from re import findall,search,sub,S
	不需要complie
	使用\d+匹配纯数字
正则表达式的应用举例
	使用findall与search从大量文本中匹配感兴趣的内容
	使用sub实现换页功能
匹配多段内容
	灵活使用findall与search
	先抓大再抓小

正则表达式的应用举例 — 实现翻页
	实验网址：http://www.jikexueyuan.com/course/android/?pageNum=2
	核心代码
			new_link = re.sub(‘pageNum=\d+’,’pageNum=%d’%i, old_url)

实战——制作文本爬虫
	目标网站：http://www.jikexueyuan.com/
	目标内容：课程图片
	实现原理：
	1.保存网页源代码
	2.Python读文件加载源代码
	3.正则表达式提取图片网址
	4.下载图片












