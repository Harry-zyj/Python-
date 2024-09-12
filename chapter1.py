# chapter 1
# 2.3 个性化消息
name_1 = "Eric"
print(f"Hello {name_1},would you like to learn some Python today")

# 2.4 调整名字的大小写
name_2 = "Zhang yejun"
print(name_2.title())   #首字母大写
print(name_2.upper())   #全大写
print(name_2.lower())   #全小写

# 2.5 名言1
print('     Albert Einstein once said,"A person who never made a mistake never tried\nanything new."')

# 2.6 名言2
famous_name = "Albert Einstein"
message = "A person who never made a mistake never tried\nanything new."
print(f'     {famous_name} once said,"{message}"')

# 2.7 删除人名中的空白
name_3 = "\t\tMr.Beast\n"
print(name_3)
print(name_3.lstrip())
print(name_3.rstrip())
print(name_3.strip())

# 2.8 文件扩展名
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

# 2.9 数字8
print(3+5)
print(8-0)
print(2**3)
print(24//3)



