from random import*

# Mô phỏng 1 tình huống trong combat, hiện các skill có thể thực hiện trong combat, và cho người dùng chọn theo thứ tự, kiểm tra xem level của nhân vật có cho phép hay không, nếu không in ra thông báo, nếu có in ra damage tương ứng
# Thực hiện lại bài trước , thêm xác xuất đánh trúng bằng cách tại thời điểm sử dụng skill, sinh 1 số ngẫu nhiên từ 0 đến 1, nếu số sinh ra nhỏ hơn Hi rate của skill, hiện ra damage, nếu số sinh ra lớn hơn Hit rate của skill, thông báo skill đã không trúng mục tiêu

dict1={    
    'Skill': 1,
    'Name': 'Tackle',
    'Minimum level': 1,
    'Damage': 5,
    'Hit rate': 0.3,
}
dict2={
    'Skill': 2,
    'Name': 'Quick attack',
    'Minimum level': 2,
    'Damage': 3,
    'Hit rate': 0.5,
}
dict3={
    'Skill': 3,
    'Name': 'Strong Kick',
    'Minimum level': 4,
    'Damage': 9,
    'Hit rate': 0.2,
}
list=[dict1,dict2,dict3]
a=[dict1['Name'],dict2['Name'],dict3['Name']]
print('Skill:')
for i,k in enumerate(a):
    print(i+1,k,sep='.')

b=randint(1,6)
c=random()
print("ban dang o cap:",b)
ask=input("Chon chieu:")
if ask=="1":
    if c<=dict1['Hit rate']:
        print("sat thuong gay ra:",dict1['Damage'])
    else:
        print("truot")
if ask=="2":
    if c<=dict2['Hit rate']:
        if b<int(ask):
            print("chua du cap de su dung")
        else:
            print("sat thuong gay ra:",dict2['Damage'])
    else:
        print("truot")
if ask=="3":
    if c<=dict3['Hit rate']:
        if b<int(ask):
            print("chua du cap de su dung")
        else:
            print("sat thuong gay ra:",dict3['Damage'])
    else:
        print("truot")