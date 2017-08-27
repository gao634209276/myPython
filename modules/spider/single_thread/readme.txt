Requests介绍与安装
Requests：HTTP for Humans
完美替代Python的urllib2模块
更多的自动化
更友好的用户体验
更完善的功能
	Windows：pip install requests
	Linux：sudo pip install requests
	少用easy_install 因为只能安装不能卸载
	多用pip方式安装
	撞墙了怎么办？请戳->
	http://www.lfd.uci.edu/~gohlke/pythonlibs/

-------------------------------------------------------
第一个网页爬虫
Requests获取网页源代码
	直接获取源代码
	修改http头获取源代码
Requests与正则表达式
	使用Requests获取网页源代码，再使用正则表达式匹配出感兴趣的内容，这是单线程简单爬虫的基本原理。




向网页提交数据
	Get与Post介绍
	分析目标网站
	Requests的表单提交

	Get是从服务器上获取数据
	Post是向服务器传送数据
	Get通过构造url中的参数来实现功能
	Post将数据放在header提交数据


向网页提交数据— 分析目标网站
	网站地址：https://www.crowdfunder.com/browse/deals
	分析工具：Chrome-审核元素-Network

	核心方法：request.post
	核心步骤：构造表单-提交表单-获取返回信息
实战——极客学院课程爬虫