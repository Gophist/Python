# Python支持一种被称为匿名的、或lambda函数。它仅由单条语句组成，该语句的结果就是返回值。
# 它是通过lambda关键字定义的，这个关键字没有别的含义，仅仅是说“我们正在声明的是一个匿名函数”。

def short_function(x):
    return x * 2


equiv_anon = lambda x: x * 2
# print(equiv_anon(1))

# 它们在数据分析工作中非常方便，因为你会发现很多数据转换函数都以函数作为参数的。
# 直接传入lambda函数比编写完整函数声明要少输入很多字（也更清晰），甚至比将lambda函数赋值给一个变量还要少输入很多字。
# 看看下面这个简单得有些傻的例子：

def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 2, 5, 6]
result = apply_to_list(ints, lambda x: x * 2)
print(result)


# 再来看另外一个例子。假设有一组字符串，你想要根据各字符串不同字母的数量对其进行排序：

strings = ['foo', 'card', 'bar', 'aaaa', 'abab']



