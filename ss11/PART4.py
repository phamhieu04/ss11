
dict={
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS': 400,
    'TOSHIBA': 600,
    'FUJITSU': 900,
    'ALIENWARE': 1000,
}

# Từ bảng giá, in ra giá của 1 máy ASUS
print("gia may asus la:",dict['ASUS'])

# Từ bàng giá, in ra giá của 1 máy, hãng máy nhập từ bàn phím
ask=input("gia may ban muon tim:").upper()
if ask=="HP":
    print("gia may",ask,"la:",dict['HP'])
if ask=="DELL":
    print("gia may",ask,"la:",dict['DELL'])
if ask=="MACBOOK":
    print("gia may",ask,"la:",dict['MACBOOK'])
if ask=="ASUS":
    print("gia may",ask,"la:",dict['ASUS'])
if ask=="TOSHIBA":
    print("gia may",ask,"la:",dict['TOSHIBA'])
if ask=="FUJITSU":
    print("gia may",ask,"la:",dict['FUJITSU'])
if ask=="ALIENWARE":
    print("gia may",ask,"la:",dict['ALIENWARE'])