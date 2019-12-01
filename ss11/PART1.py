# Khai báo 1 dictionary để biểu diễn thông tin trên
dict={
    'HP' : 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30,
}
print(dict)


# Hiện ra số lương MACBOOK có trong kho
print("so may macbook la:",dict['MACBOOK'])


# Lặp lại câu 2 với hãng máy tính nhập bởi người dùng
ask=input("so luong may ban muon tim:").upper()
if ask=="HP":
    print("so luong may",ask,"la:",dict['HP'])
if ask=="DELL":
    print("so luong may",ask,"la:",dict['DELL'])
if ask=="MACBOOK":
    print("so luong may",ask,"la:",dict['MACBOOK'])
if ask=="ASUS":
    print("so luong may",ask,"la:",dict['ASUS'])