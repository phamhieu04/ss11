dict={
    'HP' : 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30,
}

# Hiện ra số lương MACBOOK có trong kho
print("so may macbook la:",dict['MACBOOK'])


# Tính tổng số máy, bao gồm tất cả các loại hãng có trong kho
sum=dict['HP']+dict['ASUS']+dict['MACBOOK']+dict['DELL']
print("tong so may la:",sum)


# thêm 2 loại máy mới vào trong kho, FUJITSU với số lượng 15, ALIENWARE với số lượng 50
dict['FUJITSU']=15
dict['ALIENWARE']=50
print(dict)

# không cần sửa lại code, số lượng máy vẫn ra đúng kết quả
tong=0
for i in dict.values():
    tong=tong+i
print("tong so may la:",tong)
