# Mô tả cây kỹ năng của nhân vật
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

# Hiện ra thông tin skill của nhân vật
for i in range(3):
    print(list[i])

# Hiện ra thông tin skill của nhân vật, chỉ hiện tên kèm số thứ tự ở đằng trước
a=[dict1['Name'],dict2['Name'],dict3['Name']]
print('Skill:')
for i,k in enumerate(a):
    print(i+1,k,sep='.')

