神器XPath的介绍与配置
	XPath 是一门语言
	XPath可以在XML文档中查找信息
	XPath支持HTML
	XPath通过元素和属性进行导航
	XPath可以用来提取信息
	XPath比正则表达式厉害
	XPath比正则表达式简单

	安装lxml库
	from lxml import etree
	Selector = etree.HTML(网页源代码)
	Selector.xpath(一段神奇的符号)
------------------------------------------------
神器XPath的使用
XPath与HTML结构
	树状结构
	逐层展开
	逐层定位
	寻找独立节点
获取网页元素的Xpath
	手动分析法
	Chrome生成法
应用XPath提取内容
	//定位根节点
	/往下层寻找
	提取文本内容：/text()
	提取属性内容: /@xxxx


------------------------------------------------
神器XPath的特殊用法
以相同的字符开头
	starts-with(@属性名称, 属性字符相同部分)

		<div id="test-1">需要的内容1</div>
		<div id="test-2">需要的内容2</div>
		<div id="testfault">需要的内容3</div>
标签套标签
	string(.)

		<div id=“class3”>美女，
		  <font color=red>你的微信是多少？</font>
		</div>


------------------------------------------------
Python并行化介绍与演示
Python并行化介绍
	多个线程同时处理任务
	高效
	快速
Map的使用
	map 函数一手包办了序列操作、参数传递和结果保存等一系列的操作。
	from multiprocessing.dummy import Pool
	pool = Pool(4)
	results = pool.map(爬取函数, 网址列表)

------------------------------------------------
实战——百度贴吧爬虫