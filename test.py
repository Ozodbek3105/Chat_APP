a = {1: 10, 2: 20}

kalitlar = []
for key, value in a.items():
    kalitlar.append(key)


for kalit in kalitlar:
    del a[kalit]
