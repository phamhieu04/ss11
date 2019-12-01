soluong={
    'HP' : 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30,
}
soluong['TOSHIBA']=10
soluong['DELL']=60
soluong['MACBOOK']=2
soluong['FUJITSU']=15
soluong['ALIENWARE']=50
giatri={
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS': 400,
    'ACER': 350,
    'TOSHIBA': 600,
    'FUJITSU': 900,
    'ALIENWARE': 1000,
}
print("tong gia tri so may HP la:",soluong['HP']*giatri['HP'])
print("tong gia tri so may DELL  la:",soluong['DELL']*giatri['DELL'])
print("tong gia tri so may MACBOOK la:",soluong['MACBOOK']*giatri['MACBOOK'])
print("tong gia tri so may ASUS la:",soluong['ASUS']*giatri['ASUS'])
print("tong gia tri so may TOSHIBA la:",soluong['TOSHIBA']*giatri['TOSHIBA'])
print("tong gia tri so may FUJITSU la:",soluong['FUJITSU']*giatri['FUJITSU'])
print("tong gia tri so may ALIENWARE la:",soluong['ALIENWARE']*giatri['ALIENWARE'])
print("tong gia tri toan bo may trong kho la:",soluong['HP']*giatri['HP']+soluong['DELL']*giatri['DELL']+soluong['MACBOOK']*giatri['MACBOOK']+soluong['ASUS']*giatri['ASUS']+soluong['TOSHIBA']*giatri['TOSHIBA']+soluong['FUJITSU']*giatri['FUJITSU']+soluong['ALIENWARE']*giatri['ALIENWARE'])
for i in soluong.values():
    for k in giatri.values():
        
