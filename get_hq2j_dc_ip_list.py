#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2,yaml

def zone_ip_list():
    url1 = "https://c2.test.com/zone_dc_ip?secretkey=********&name=hq2j_dc&type=zoneip"
    req1 = urllib2.Request(url1)
    response1 = urllib2.urlopen(req1)
    ip_list1 = response1.read().split('\n')  # 用\n分割str字符串，并保存到列表
    ip_list1 = dict(zip(['hq2j_dc'],[ip_list1]))
    print "该zone授权入方向的IP列表:\n"
    print ip_list1
    with open('/etc/ansible/group_vars/hq2j_dc/hq2j_dc.yml', 'w') as f:
        yaml.dump(ip_list1,f)
        f.close()
    print "\n"
    
    url2 = "https://c2.test.com/zone_dc_ip?secretkey=**********&name=hq2j_dc_access_ip"
    req2 = urllib2.Request(url2)
    response2 = urllib2.urlopen(req2)
    ip_list2 = response2.read().split('\n')  # 用\n分割str字符串，并保存到列表
    ip_list2 = dict(zip(['hq2j_dc_access_ip'],[ip_list2]))
    print "该zone授权任意IP入方向的IP列表:\n"
    print ip_list2
    with open('/etc/ansible/group_vars/hq2j_dc/hq2j_dc_access_ip.yml', 'w') as f:
        yaml.dump(ip_list2,f)
        f.close()
    print "\n"

if __name__ == '__main__':

    get_ip_list = zone_ip_list()