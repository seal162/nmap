import ipaddr


f = open('aliveHost.txt')
for each in f.readlines():
    each = each.strip('\r\n')
    if 'there' in each:
        ip = each.split(':')[1]
        print(ip)