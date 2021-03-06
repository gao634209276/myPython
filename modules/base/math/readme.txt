Python算法概述
什么是算法
	我们上两门课程已经学习过了数据结构，我们知道，数据结构就是数据的存储结构，
	但是，如果我们需要操作这些数据，比如对这些数据进行排序，应该如何去操作，如何去运算呢？
	所以，我们在这里要学习算法，简而言之，算法就是运算方法。
		比如，我们要对一组数据进行排序，我们可以采用冒泡排序的运算方法来排，也可以使用选择排序的运算方法来排，
		实现一个排序的结果，有多种运算方法（算法）。
		再比如，要从一个字符串“according”中搜索“i”这个字符，我们可以按从左往右搜索的方法去搜索，
		也可以使用从右到左的方法去搜索。算法是解决问题的方法，一种策略与思维。
算法举例
	算法是针对问题而出现的，有问题的地方就有算法。
	虽然每个问题的算法都不一样，但是，我们把各种问题的算法总结出来，
	可以得到一些基本的算法思想，这些算法思想是解决很多问题的时候都要用到的思想。
	常见的算法思想有：分治法、贪心法、穷举法、递归法、递推法、回溯法、动态规划法、迭代法、分支界限法。
	除了基本算法思想外，我们这门课程会结合实际问题带领大家学习一些典型的算法，
	比如第二节课到第四节课，我们会给大家结合如何对一组无序数据进行排序方面的问题讲解三种排序算法，
	第五节课我们会给大家结合如何从一个字符串中搜索指定字符的问题讲解一种典型的二分搜索算法。
	让大家学会分析问题，举一反三，从实际中理解算法。
Python常见算法-快排
	首先，快排是一种排序算法，是一种解决排序问题的运算方法。
	比如，我们需要对[7,91,23,1,6,3,79,2]这一组数据按从小到大的顺序进行排序，应该如何排呢？
	对这一组数据进行排序的方法有很多，快排是其中一种方法。
	我们这节课先将如何使用快排算法对数据进行排序。本节课所提到的算法均为快排算法，以下不再做申明。
	是这样的，我们可以首先在这组数据中随意选择一个数字作为基准，
	然后比该基准大的数字在基准数字的左边，比该基准数字大的数字在基准数字的右边，
	这样，第一趟排序过后，把数据分为了两部分，一部分是比基准大的数据，一部分是比基准小的数据，
	然后在分出来的每部分数据中按上述方法再排，一直排到分组中的数据只有一个或者没有数据为止。
	那么下面我们通过动画讲解一下。
Python常见算法-选择排序
Python常见算法-二路归并排序
Python常见算法-搜索算法