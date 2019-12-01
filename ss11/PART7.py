dict={
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': 'Shield, Bread Loaf',
    'Gold': 100,
    'Level': 2,
}

#  thêm 50 Gold cho nhân vật này
dict['Gold']=+50

# thêm FlintStone vào Backback của nhân vật này
dict['Backpack']='Shield,Bread Loaf,FlintStone'

# trong Pocket chứa 1 danh sách các vật dụng bao gồm MonsterDex và Flashlight
list=['MonsterDex','Flashlight']
dict['Pocket']=list

print(dict)