# switch_acl_update
公司根据各业务情况，明确网络层互相访问关系，在核心交换机配置ACL控制进入流量，提升公司业务安全性。

- 一开始使用python借助c2的ip列表，配置交换机ACL，该方式借助交换机nxapi接口进行操作，存在问题是一些老旧交换机不支持nxapi，因此存在bak4python代码。

- 之后借助ansible工具进行配置交换机ACL

- 内部防火墙也需要自动化更新访问控制列表，实现代码参考firewall_iplist_update

### ansible配置使用
- 配置ansible的hosts文件，保存主机认证方式
```
[root@cloud_security_group_api ansible]# ll
total 32
-rw-r--r-- 1 root root 19979 Aug  7  2019 ansible.cfg
drwxr-xr-x 4 root root  4096 Aug  9  2019 group_vars
-rw-r--r-- 1 root root  1301 Aug 22  2019 hosts
drwxr-xr-x 2 root root  4096 Jul 21  2019 roles

组名及主机名都不能重复，否则匹配到就会再其中执行相关操作
[root@cloud_security_group_api ansible]# vi /etc/ansible/hosts 
[hq2y_dc]
yz_nexus1 ip=1.1.1.1 username=test password=test
yz_nexus2 ip=2.2.2.2 username=test password=test

[hq2j_dc]
jxq_nexus1 ip=3.3.3.3 username=test password=test
jxq_nexus2 ip=4.4.4.4 username=test password=test

保存获取到的iplist到yml文件中
[root@cloud_security_group_api ansible]# ll group_vars/hq2j_dc/
total 8
-rw-r--r-- 1 root root   40 Jul 21 15:35 hq2j_dc_access_ip.yml
-rw-r--r-- 1 root root 2763 Jul 21 15:35 hq2j_dc.yml
```

参考地址：

[Ansible介绍](https://getansible.com/)

[cisco1](https://docs.ansible.com/ansible/latest/modules/nxos_acl_module.html?highlight=cisco)

[cisco1](https://docs.ansible.com/ansible/latest/modules/asa_acl_module.html?highlight=cisco）

[cisco1]（https://docs.ansible.com/ansible/latest/modules/nxos_acl_interface_module.html?highlight=cisco）


### ansible tower是收费的，可以破解使用，实现图形界面化的配置ansible
参考地址：

[ansible-tower安装以及破解](https://www.tracymc.cn/archives/1510)
