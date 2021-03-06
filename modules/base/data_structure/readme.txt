Python数据结构初识
Python数据结构概述
什么是数据结构？
	我们知道，一个程序里面必然会有数据存在，同样的一个或几个数据要组织起来，可以有不同的组织方式，也就是不同的存储方式。
	不同的组织方式就是不同的结构，我们把这些数据组织在一起的结构称之为数据的结构，也叫做数据结构。
		比如，有一字符串是"abc",我们将其重新组织一下，比如通过list()函数将"abc"变成["a","b","c"]，
		那么这个时候数据就发生了重组，重组之后数据的结构就变了，变成了["a","b","c"]，
	我们把这种形式的数据的结构叫做列表，也就是说列表是数据结构中的一种类型之一。
	数据结构除了列表之外，还有元组、字典、队列、栈、树等等。Python中数据的组织方式叫做Python的数据结构。
数据结构实例
	Python中的数据结构有非常多类型。其中，Python中系统自己定义好的，
	不需要我们自己去定义的数据结构叫做Python的内置数据结构，比如列表、元组等，而有些数据组织方式，
	Python系统里面没有直接定义，需要我们自己去定义实现这些数据的组织方式，
	这些数据组织方式称为Python的扩展数据结构，比如栈、队列等。
	下面我们通过实例来认识一下Python的数据结构。
数据结构与算法的关系
	为什么要将数据结构跟算法放在一起讲呢？
		数据结构就是数据的组织方式，就是数据存储的方式，也就是说，数据结构是静态的。
		算法是指运算方法，通俗的说，算法就是思维。
		我们编写的程序，是动态的，我们需要将数据进行计算，那么我们如何运算呢？
		运算方法有很多，不同的运算方法叫做不同的算法。比如1+7+9的计算方法。
		也就是说算法是动态的，是指运算的思维方法。
	当然我们的算法不是凭空出来的，他必须建立在数据的基础上，
	所以数据结构是算法的基础，但相同的数据结构运用不同的算法拥有不同的效率。

Python常见数据结构-栈
	首先，栈是一种数据结构。这种数据结构在Python中不是内置数据结构，属于扩展数据结构。
Python常见数据结构-队列
Python常见数据结构-树
	树是一种非线性的数据结构，树具有非常高的层次性。
	利用树来存储数据，能够使用公有元素进行存储，能够很大的程度上节约存储空间。
	树的定义是首先有且只有一个根节点，其次他有N个不相交子集，每个子集为一颗子树。

	二叉树一种特殊的树，二叉树要么为空树，要么为左、右两个不相交的子树组成。
	二叉树是有序树，即使只有一个字树，也需要区分该子树是左子树还是右子树。
	二叉树每个节点的度不能大于2,可以取0,1,2。
	二叉树的存储方式有两种，一种是顺序存储，一种是链式存储。
	顺序存储中采用一维数组的存储方式，链式存储中，采用链表的存储方式，通常分为三部分，数据域，左孩子链域和右孩子链域。
Python常见数据结构-链表
	首先，链表是一种数据结构。
	链表是一种非连续，非顺序的存储方式。
	链表由一系列结点组成，每个结点包括两部分，一部分是数据域，另一部分是指向下一结点的指针域。
	链表可以分为单向链表，单向循环链表，双向链表，双向循环链表。
Python常见数据结构-bitmap
	首先，bitmap也是一种数据结构。bit指的是位，map指的是图，bitmap也叫做位图。
	这种数据结构的存储简单来说就是把原来的数，转化为二进制来存储，每个位占一个存储单元。
	我们操作bitmap中的数据，也就是相当于操作一个位。
	bitmap数据结构的优点是可以实现很好的排序，这一点下面我们会讲到。
Python常见数据结构-图
	图是一种数据结构。
	图可以简单的理解为是一个关系网络，该网络中有N多结点，每个结点上存储着一个数据，
	数据之间的关联我们可以用线把关联的结点连起来的方式表示。
	其中，有的数据关系是由方向的，
	比如数据A-->数据B，其关系只能从A到B，不能从B到A，
	如果数据之间的关系是有方向的，这个数据关系用弧线表示。
	有的数据关系是没有方向的，A--B表示既可以A到B关联，也可以B到A关联，这种没有方向的关系用线段表示。