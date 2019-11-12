def segitigaKata(x):
    x = x.replace(' ', '')
    q = len(x)-1
    p = 0
    kosong = []
    for i in range(q):
        q = q - p
        if q < 0:
            break
        kosong.append(q)
        p = 1 + 1 + i
    if 0 in kosong:
        y = 0
        z = 0
        a = int((len(x))/2-1)
        for i in range(a):
            y += i + 1
            b = x[z:y]
            print(b)
            z = y
            if z >= len(x):
                break
        y = len(b)
        z = 0
        c = 0
        d = 0
        for i in range(a):
            y = y + c - d
            b = x[z:y]
            print(b)
            z = y
            c = len(b)
            d = 1
            if z >= len(x):
                break
    else:
        print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')


segitigaKata('Purwadhika')
segitigaKata('Purwadhika Startup and Coding School @BSD')
segitigaKata('kode')
segitigaKata('kode python')
segitigaKata('lintang')