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
list_ifname_ip(file)
def capif(file):
  file=open("running-config.cfg",'r')
  nfile=open("running-config-new.cfg",'w')
  for line in file:
    if  "255.255.0.0" in line or "172" in line:
       line= line.replace("255.255.0.0","255.0.0.0")
       line=line.replace("172","10")
       nfile.write(line)
    elif "255.255.255.0" in line or "192" in line:
       line=line.replace("255.255.255.0","255.0.0.0")
       line=line.replace("192","10")
       nfile.write(line) 
    else:
       nfile.write(line)
  return nfile
capif(file)
