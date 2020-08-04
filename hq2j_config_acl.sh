#! /bin/bash
# 获取IP白名单并配置于交换机ACL中
echo -e "\033[36m##############################################\033[0m\n"
echo -e "\033[36m           HQ2J_DC交换机更新ACL配置           \033[0m\n"
echo -e "\033[36m               1.配置ACL                      \033[0m"
echo -e "\033[36m               2.应用ACL到接口                \033[0m"
echo -e "\033[36m               3.解绑ACL                      \033[0m\n"
echo -e "\033[36m##############################################\033[0m"
read -p "please input a number 1-3:" n
case $n in
1)
python get_hq2j_dc_ip_list.py && ansible-playbook config_hq2j_acl.yml
;;
2)
ansible-playbook apply_hq2j_acl.yml
;;
3)
ansible-playbook untied_hq2j_acl.yml
;;
*)
echo "Please input a number: 1-3"
;;
esac
