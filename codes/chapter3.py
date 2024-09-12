# 3.1 姓名
names = ["ZYJ",'DZB','XYJ']
print(names[0].title())
print(names[1].title())
print(names[2].title())

# 3.2 问候语
names = ["ZYJ",'DZB','XYJ']
message = f"Hello, my friend {names[0].title()}"
print(message)

# 3.4 嘉宾名单
guests = []
guests.append("ZYJ")
guests.insert(0,"DHY")
guests.append("SJH")


message_1 = f"I'd like to invite you to my party, my friend {guests[0].title()}"
print(message_1)
message_2 = f"I'd like to invite you to my party, my friend {guests[1].title()}"
print(message_2)
message_3 = f"I'd like to invite you to my party, my friend {guests[2].title()}"
print(message_3)
# 3.5 修改嘉宾名单
print("ZYJ can't attend today's party,Tina will come")
guests.remove("ZYJ")
guests.append("Tina")
message_1 = f"I'd like to invite you to my party, my friend {guests[0].title()}"
print(message_1)
message_2 = f"I'd like to invite you to my party, my friend {guests[1].title()}"
print(message_2)
message_3 = f"I'd like to invite you to my party, my friend {guests[2].title()}"
print(message_3)

# 3.6 添加嘉宾
guests.insert(0,"Tom")
guests.insert(-1,"Jerry")
guests.insert(2,"Mia")

# 3.7 缩短名单
print("Sorry,I can only invite two guests now")
friend = guests.pop(0)
print(f"Sorry {friend.title()}, you can't attend today's party")
friend = guests.pop(0)
print(f"Sorry {friend.title()}, you can't attend today's party")
friend = guests.pop(0)
print(f"Sorry {friend.title()}, you can't attend today's party")

print(names)

del names[1]
del names[0]
del names[0]

print(names)

# 3.8 放眼世界
destinations = ["Beijing","Tokoy","Paris","New York","An Qing"]
print(destinations)

print(sorted(destinations))
print(destinations)

print(sorted(destinations,reverse=True))
print(destinations)

destinations.reverse()
print(destinations)

destinations.sort()
print(destinations)




