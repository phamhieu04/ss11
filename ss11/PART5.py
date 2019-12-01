dict={
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS': 400,
    'TOSHIBA': 600,
    'FUJITSU': 900,
    'ALIENWARE': 1000,
}

# Có một đơn hàng đặt mua máy ASUS với số lượng là 5, tính tổng giá trị đơn hàng
print("tong tien la:",dict['ASUS']*5)


# Lặp lại bài trước với hãng máy và số lượng nhập từ người dùng
while True:
    dict={
        'HP': 600,
        'DELL': 650,
        'MACBOOK': 12000,
        'ASUS': 400,
        'TOSHIBA': 600,
        'FUJITSU': 900,
        'ALIENWARE': 1000,
    }
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
    if ask=="THOI":
        break