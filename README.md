# Python实现阿里云域名DDNS支持ipv4和ipv6

感谢两位大神：
https://github.com/dingguotu/ddns-aliyu.git
https://github.com/zeruns/-Python-aliddns_ipv4-ipv6


需要安装的库：
```
pip install aliyun-python-sdk-core-v3
pip install aliyun-python-sdk-domain
pip install aliyun-python-sdk-alidns
pip install requests
```

## 关键词

1. domain  域名
2. sub_domain  二级域名，子域名

## 前置条件

1. Git
2. python 3.*
3. 阿里云账号

## 使用方法
已经在python 3.5

---

通过本命令获取 ddns-aliyun

```bash
git clone https://github.com/SmartIotMaker/Python-aliddns_ipv4-ipv6.git
```

---

接下来到阿里云中创建AccessKey，具体步骤是：
登录阿里云 -> 进入控制台 -> 点击accesskeys ![accesskeys](img/accesskeys.png)

-> 创建AccessKey ![AccessKey](img/create-access-key.png)

---

如果域名是在腾讯云或其他非阿里云处购买的，还需要进入相对应的服务商控制台，修改域名的DNS地址为：

```bash
ns1.alidns.com
ns2.alidns.com
```

---

复制 `conf.sample.json` 文件，并重命名为 `conf.json`，根据您的DNSPod设置修改 `conf.json` 文件，填入以下内容：

```bash
{
    "access_key": <access_key>,
    "access_secret": <access_secret>,
    "domains": [
        {
            "name": <first_domain>,
            "sub_domains": [<first_sub_domain_name>, <second_sub_domain_name>,...]
        },
        {
            "name": <second_domain>,
            "sub_domains": [<first_sub_domain_name>, <second_sub_domain_name>,...]
        }
    ]
}
```

`domains`部分，想绑定几个就写几个，不需要多写，`sub_domains`通常写 `@` 和 `*` 就够了，二级子域名直接用 `*` 代替，然后在自己的代理服务器（IIS，nginx，Apache等）上面去进行绑定。domain 和 sub_domain 可以不需要事先手动绑定，本程序会自动识别

---



