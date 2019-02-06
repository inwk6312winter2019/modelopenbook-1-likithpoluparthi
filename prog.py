file=open("running-config.cfg",'r')
d=dict()
def list_ifname_ip(file):  
    for line in file:
        if '!' not in line:
            if 'nameif' in line:
                line=line.strip()
                key=line.split(" ")
            if 'ip address' in line and '.' in line:
                line=line.strip()
                iptemp=line.split(" ")
                tup=(iptemp[2],)
                d.setdefault(key[1],(iptemp[2],iptemp[3]))
    return d
print(list_ifname_ip(file))
