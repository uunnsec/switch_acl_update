# switch_acl_update
公司根据各业务情况，明确网络层互相访问关系，在核心交换机配置ACL控制进入流量，提升公司业务安全性。

- 一开始使用python借助c2的ip列表，配置交换机ACL，该方式借助交换机nxapi接口进行操作，存在问题是一些老旧交换机不支持nxapi，因此存在bak4python代码。

- 之后借助ansible工具进行配置交换机ACL

- 内部防火墙也需要自动化更新访问控制列表，实现代码参考firewall_iplist_update
