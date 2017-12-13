import nmap

f = open('/Users/zhainaidong/Desktop/Doc/zzz/nmap/Result_ip.txt')
count = 0
for each in f.readlines():

    each = each.strip('\r\n')
    nm = nmap.PortScanner()
    ret = nm.scan(each,arguments='-sn')
    if count%10 = = 0:
        print 'Now printing:%d'%count
    count += 1
    # print ret
    if  ret['nmap']['scanstats']['uphosts'] == '1':
        print 'there is alive host:%s'%each
