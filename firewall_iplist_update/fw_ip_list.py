#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2,requests

data = {
    "zq_office": [
        "proj_ore_f1",
        "vpn_vpc",
        "vpn4tech_vpc",
    ],
}

def w_list():

    # 从c2获取ip白名单
    for x in data["zq_office"]:
        path = "?secretkey=********&name=" + x
        url = "https://c2.test.com/zone_dc_ip" + path
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        ips = response.read()
        ip_list = ips.split('\n')  # 用\n分割str字符串，并保存到列表
        # ip_list = sorted(set(ip_list), key=ip_list.index)  # list去重并按照原来顺序进行排序

        print ip_list

        # 通过api将ip白名单配置于防火墙策略中
        num = -1
        all_body = ''
        for y in ip_list:
            url = 'http://1.1.1.1:10251/restconf/data/huawei-address-set:address-set/addr-object=public,%s' % x
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
                'Accept': '*/*',
                'accept-encoding': 'gzip, deflate',
                'Authorization': 'Basic ***************',
                'Connection': 'keep-alive',
                'Content-Type': 'application/yang.data+xml',
            }
            num = num + 1
            body = ('<elements> \n'
                    '<elem-id>%s</elem-id> \n'
                    '<address-ipv4>%s</address-ipv4> \n'
                    '</elements> \n'
                    )%(num, y)
            all_body = all_body + body

        all_body = '<addr-object> \n' + all_body + '</addr-object>'
        # proxies = {"http": "http:127.0.0.1:8080"}
        # req = requests.put(url, data=all_body, headers=headers, proxies=proxies)
        req = requests.put(url, data=all_body, headers=headers)
        print req



if __name__ == '__main__':

    fw_ips = w_list()