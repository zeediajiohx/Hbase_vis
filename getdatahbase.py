import happybase


def get_c1():

    allpopu=0
    cnpopu=0
    connection = happybase.Connection('192.168.56.101')
    table = connection.table('populations')
    for k, v in table.scan(row_start='2019',columns=['popu']):
        for i in v.values():
            allpopu+=int(i.decode())
        cnpopu = int(v['popu:中国'.encode()].decode())
    return ([(allpopu,)],[(cnpopu,)])


def get_c2():
    data = []
    connection = happybase.Connection('192.168.56.101')
    table = connection.table('populations')
    for k, v in table.scan(row_start='2019',columns=['popu']):
        for key in v.keys():
            data.append((key.decode().split(":")[1],int(v[key].decode())))
    return data

def get_l1():
    data = []
    connection = happybase.Connection('192.168.56.101')
    table = connection.table('populations')
    for k, v in table.scan(row_start='1959',columns=['popu','cont']):
        yazhou=0
        ouzhou=0
        feizhou=0
        meizhou=0
        allpopu=0
        for key in v.keys():
            if key.decode().split(":")[0] == 'popu':
                allpopu+=int(v[key].decode())
            elif key.decode().split(":")[0] == 'cont':
                nkey = 'popu:' + key.decode().split(":")[1]
                if v[key].decode()=='亚洲':
                    yazhou+=int(v[nkey.encode()])
                elif v[key].decode()=='欧洲':
                    ouzhou+=int(v[nkey.encode()])
                elif v[key].decode()=='非洲':
                    feizhou+=int(v[nkey.encode()])
                elif v[key].decode()=='美洲':
                    meizhou+=int(v[nkey.encode()])
        data.append((int(k.decode()),allpopu,yazhou,ouzhou,feizhou,meizhou))
    return data

def get_l2():
    data = []
    connection = happybase.Connection('192.168.56.101')
    table = connection.table('populations')
    for k, v in table.scan(row_start='2019',columns=['popu','rank']):
        for key in v.keys():
            if key.decode().split(":")[0]=='rank':
                if int(v[key].decode())<=5:
                    nkey='popu:'+key.decode().split(":")[1]
                    data.append((int(v[nkey.encode()].decode()),key.decode().split(":")[1]))
    data.sort(reverse=True)
    return data

def get_r1():
    data = []
    connection = happybase.Connection('192.168.56.101')
    table = connection.table('populations')
    for k, v in table.scan(row_start='2019',columns=['popu','cont']):
        yazhou=0
        ouzhou=0
        feizhou=0
        meizhou=0
        dayangzhou=0
        for key in v.keys():
            if key.decode().split(":")[0] == 'cont':
                nkey = 'popu:' + key.decode().split(":")[1]
                if v[key].decode()=='亚洲':
                    yazhou+=int(v[nkey.encode()])
                elif v[key].decode()=='欧洲':
                    ouzhou+=int(v[nkey.encode()])
                elif v[key].decode()=='非洲':
                    feizhou+=int(v[nkey.encode()])
                elif v[key].decode()=='美洲':
                    meizhou+=int(v[nkey.encode()])
                elif v[key].decode()=='大洋洲':
                    dayangzhou+=int(v[nkey.encode()])
        data=[('亚洲',yazhou),('大洋洲',dayangzhou),('欧洲',ouzhou),('美洲',meizhou),('非洲',feizhou)]

    return data


print(get_l1())
