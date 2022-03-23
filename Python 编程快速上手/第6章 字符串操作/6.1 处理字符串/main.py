# 双引号
spam = "That is Alice's cat."
print(spam)

# 转义字符
spam = 'Say hi to Bob\'s mother.'
print(spam)

# 换行符 \n
newline = "Hello there!\nHow are you?\nI'm doing fine."
print(newline)

# 原始字符串
# 在字符串前加上r，使它成为原始字符串。
rawline = r'That is Carol\'s Cat'
print(rawline)

# 三重引号多行字符串
triple_quotes = '''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob'''
print(triple_quotes)

# 多行注释
"""这是一条多行注释
这是一条多行注释
这是一条多行注释
"""

# 字符串像列表一样，使用下标和切片。
str = "Hello world!"
print(
    str[0],
    str[4],
    str[-1],
    str[0:5],
    str[:5],
    str[6:]
)

# in 和 not in 操作符也可以用于字符串
print('Hello' in 'Hello world')
print('hello' in 'Hello')
print('HELLO' in 'Hello World')
print('' in 'spam')
print('cats' not in 'cats and dogs')

# 字符串方法 upper() lower() isupper() islower()
spam = 'Hello world!'
print(spam)
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

# 小程序 How are you?
print("How are you?")
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is also good!^_^')


