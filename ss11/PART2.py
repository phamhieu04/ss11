while True:
    dict={
        'HP' : 20,
        'DELL': 50,
        'MACBOOK': 12,
        'ASUS': 30,
    }
    dict['TOSHIBA']=10
    dict['DELL']=60
    dict['MACBOOK']=2
    ask=input("so luong may ban muon tim:").upper()
    if ask=="HP":
        print("so luong may",ask,"la:",dict['HP'])
    if ask=="DELL":
        print("so luong may",ask,"la:",dict['DELL'])
    if ask=="MACBOOK":
        print("so luong may",ask,"la:",dict['MACBOOK'])
    if ask=="HP":
        print("so luong may",ask,"la:",dict['ASUS'])
    if ask=="TOSHIBA":
        print("so luong may",ask,"la:",dict['TOSHIBA'])
    if ask=="THOI":
        break
    