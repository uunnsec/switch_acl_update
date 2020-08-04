#!/usr/bin/env python
# coding=utf-8

import json,urllib2,requests

data = {
    "hq2y_dc": [
        "proj_ore_f1",
        "vpn4tech_vpc",
        "zq_office",
        "qingcloud_partner",
        "hq2y_dc",
    ],
    "hq2j_dc": [
        "proj_ore_f1",
        "vpn4tech_vpc",
        "vpn_vpc",
        "zq_office",
        "qingcloud_partner",
        "hq2j_dc",
        "hq2y_dc",
    ],
    "hq2j_gpu": [
        "vpn4tech_vpc",
        "zq_office",
        "proj_ha_f1",
        "hq2j_dc",
        "hq2y_dc",
        "vpn_vpc",
    ],
}

#  亦庄和酒仙桥主备交换机ip地址
dev_ips = [
        "1.1.1.1",  #  酒仙桥交换机ip
        "2.2.2.2",  #  酒仙桥交换机ip
        "3.3.3.3",  #  亦庄交换机ip
        "4.4.4.4",  #  亦庄交换机ip
]

dev_ip ="1.1.1.1"

def upd_wlist():
    if dev_ip == dev_ips[0] or dev_ip == dev_ips[1]:
        ip_list1 = []

        for x in data["hq2j_dc"]:
            path1 = "?secretkey=**********&name=" + x
            url1 = "https://c2.test.com/wlist" + path1
            req1 = urllib2.Request(url1)
            response1 = urllib2.urlopen(req1)
            ips1 = response1.read()
            get_ip_list1 = ips1.split('\n')  # 用\n分割str字符串，并保存到列表
            ip_list1 = ip_list1 + get_ip_list1
            ip_list1 = sorted(set(ip_list1),key=ip_list1.index)

        with open('hq2j_dc.txt', 'r') as f1:
            ip_list_old1 = f1.read()
            ip_list_old1 = ip_list_old1.strip()
            ip_list_old1 = ip_list_old1.split('\n')

        diff1 = [item for item in ip_list_old1 if not item in ip_list1]

        print diff1

        for y in diff1:
            url = "http://%s/ins" % dev_ip
            switchuser = "XXXXX"
            switchpassword = "********"
            myheaders = {'Content-Type': 'application/json'}
            payload = {
                "ins_api": {
                    "version": "1.0",
                    "type": "cli_conf",
                    "chunk": "0",
                    "sid": "1",
                    "input": "ip access-list hq2j ;no permit ip %s any " % y,
                    "output_format": "json"
                }
            }

            req = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword))
            req_json = req.json()

            print req_json

        diff2 = [item for item in ip_list1 if not item in ip_list_old1]

        print diff2

        for z in diff2:
            url = "http://%s/ins" % dev_ip
            switchuser = "XXXXX"
            switchpassword = "********"
            myheaders = {'Content-Type': 'application/json'}
            payload = {
                "ins_api": {
                    "version": "1.0",
                    "type": "cli_conf",
                    "chunk": "0",
                    "sid": "1",
                    "input": "ip access-list hq2j ;permit ip %s any " % z,
                    "output_format": "json"
                }
            }

            req = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword))
            req_json = req.json()

            print req_json

        with open('hq2j_dc.txt', 'w') as f:
            for a in ip_list1:
                f.write(str(a))
                f.write('\n')
            f.close()

        ip_list2 = []
        for i in data["hq2j_gpu"]:
            path2 = "?secretkey=**********&name=" + i
            url2 = "https://c2.test.com/wlist" + path2
            req2 = urllib2.Request(url2)
            response1 = urllib2.urlopen(req2)
            ips2 = response1.read()
            get_ip_list2 = ips2.split('\n')  # 用\n分割str字符串，并保存到列表
            ip_list2 = ip_list2 + get_ip_list2
            ip_list2 = sorted(set(ip_list2), key=ip_list2.index)

        with open('hq2j_gpu.txt', 'r') as f2:
            ip_list_old2 = f2.read()
            ip_list_old2 = ip_list_old2.strip()
            ip_list_old2 = ip_list_old2.split('\n')

        diff3 = [item for item in ip_list_old2 if not item in ip_list2]

        print diff3

        for j in diff3:
            url = "http://%s/ins" % dev_ip
            switchuser = "XXXXX"
            switchpassword = "********"
            myheaders = {'Content-Type': 'application/json'}
            payload = {
                "ins_api": {
                    "version": "1.0",
                    "type": "cli_conf",
                    "chunk": "0",
                    "sid": "1",
                    "input": "ip access-list hq2j ;no permit ip %s any " % j,
                    "output_format": "json"
                }
            }

            req = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword))
            req_json = req.json()

            print req_json

        diff4 = [item for item in ip_list2 if not item in ip_list_old2]

        print diff4

        for k in diff4:
            url = "http://%s/ins" % dev_ip
            switchuser = "XXXXX"
            switchpassword = "********"
            myheaders = {'Content-Type': 'application/json'}
            payload = {
                "ins_api": {
                    "version": "1.0",
                    "type": "cli_conf",
                    "chunk": "0",
                    "sid": "1",
                    "input": "ip access-list hq2j ;permit ip %s any " % k,
                    "output_format": "json"
                }
            }

            req = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword))
            req_json = req.json()

            print req_json

        with open('hq2j_gpu.txt', 'w') as f:
            for a in ip_list2:
                f.write(str(a))
                f.write('\n')
            f.close()

    elif dev_ip == dev_ips[2] or dev_ip == dev_ips[3]:
        ip_list = []

        for x in data["hq2y_dc"]:
            path1 = "?secretkey=**********&name=" + x
            url1 = "https://c2.test.com/wlist" + path1
            req1 = urllib2.Request(url1)
            response1 = urllib2.urlopen(req1)
            ips1 = response1.read()
            get_ip_list1 = ips1.split('\n')  # 用\n分割str字符串，并保存到列表
            ip_list = ip_list + get_ip_list1
            ip_list = sorted(set(ip_list), key=ip_list.index)

        with open('hq2y_dc.txt', 'r') as f:
            ip_list_old = f.read()
            ip_list_old = ip_list_old.strip()
            ip_list_old = ip_list_old.split('\n')

        diff1 = [item for item in ip_list_old if not item in ip_list]

        print diff1

        for y in diff1:
            url = "http://%s/ins" % dev_ip
            switchuser = "XXXXX"
            switchpassword = "********"
            myheaders = {'Content-Type': 'application/json'}
            payload = {
                "ins_api": {
                    "version": "1.0",
                    "type": "cli_conf",
                    "chunk": "0",
                    "sid": "1",
                    "input": "ip access-list hq2y ;no permit ip %s any " %y,
                    "output_format": "json"
                }
            }

            req = requests.post(url, data=json.dumps(payload), headers=myheaders,auth=(switchuser, switchpassword))
            req_json = req.json()

            print req_json

        diff2 = [item for item in ip_list if not item in ip_list_old]

        print diff2

        for z in diff2:
            url = "http://%s/ins" % dev_ip
            switchuser = "XXXXX"
            switchpassword = "********"
            myheaders = {'Content-Type': 'application/json'}
            payload = {
                "ins_api": {
                    "version": "1.0",
                    "type": "cli_conf",
                    "chunk": "0",
                    "sid": "1",
                    "input": "ip access-list hq2y ;permit ip %s any " %z,
                    "output_format": "json"
                }
            }

            req = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword))
            req_json = req.json()

            print req_json

        with open('hq2y_dc.txt', 'w') as f:
            for a in ip_list:
                f.write(str(a))
                f.write('\n')
            f.close()


    else:
        print "无此交换机"


if __name__ == '__main__':

    update_wlist = upd_wlist()