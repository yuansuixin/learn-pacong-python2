import re

string = '呵呵<section><span>秦时明月汉时关,万里长征人未还,但使龙城飞将在,不教胡马度阴山</span></section>哈哈'

pattern = re.compile(r'<(\w+)><(\w+)>(.*?)</\2></\1>')

obj = pattern.search(string)

print(obj.group())
print(obj.group(1))
print(obj.group(2))
print(obj.group(3))