#!/usr/bin/python
# -*- coding: future_fstrings -*-thing='world'print(f'hello {thing}')
from urllib import request
import re, json, os, logging
import aliddns
import logger


global LocalIP
global Access_Key_Id
global Access_Key_Secret

Headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Content-type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
    }

def ddns(domain):
    for sub_domain in domain['sub_domains']:
        print(f"domain={domain['name']} sub_domain={sub_domain}")
        isexitflag,recordip,recordid = aliddns.isexitdomain(domain['name'], sub_domain)
        print("1\n")
        if isexitflag == False:
            # logging.info(f"Begin add [{sub_domain}.{domain['name']}].")
            aliddns.add(domain['name'], sub_domain, "A", LocalIP)
        elif recordip.strip() != LocalIP.strip():
            # logging.info(f"Begin update [{sub_domain}.{domain['name']}].")
            aliddns.update(recordip, sub_domain, "A", LocalIP)
        else:
            logging.info("Need upgrade.")

def get_ip():
    global LocalIP

    ipDict = dict()
    ip38(ipDict)
    ip138(ipDict)
    ipcn(ipDict)
    ip42(ipDict)
    jsonip(ipDict)
    httpbin(ipDict)
    ipify(ipDict)

    LocalIP = sorted(ipDict.items(), key=lambda d:d[1], reverse = True)[0][0]
    print(f'LocalIP is {LocalIP}')

# ip38
def ip38(ipDict):
    try:
        ip38Req = request.Request(url=f'http://ip38.com/', headers=Headers, method='GET')
        ip38Res = request.urlopen(ip38Req).read().decode('utf-8')
        ip38 = re.findall(re.compile(r'<a href=/ip.php\?ip=(.*?)>'), ip38Res)[0]
        ipDict[ip38] = ipDict.setdefault(ip38, 0) + 1
    except Exception as e:
        logging.error(e)
        pass

# ip138
def ip138(ipDict):
    try:
        ip138Req = request.Request(url=f'https://2021.ip138.com/', headers=Headers, method='GET')
        ip138Res = request.urlopen(ip138Req).read().decode('utf-8')
        ip138 = re.findall(re.compile(r'\[<a.*?>(.*?)</a>\]'), ip138Res)[0]
        ipDict[ip138] = ipDict.setdefault(ip138, 0) + 1
    except Exception as e:
        logging.error(e)
        pass

# ipcn
def ipcn(ipDict):
    try:
        ipcnReq = request.Request(url=f'https://ip.cn/api/index?ip=&type=0', headers=Headers, method='GET')
        ipcn = json.loads(request.urlopen(ipcnReq).read().decode('utf-8'))['ip']
        ipDict[ipcn] = ipDict.setdefault(ipcn, 0) + 1
    except Exception as e:
        logging.error(e)
        pass

# ip.42
def ip42(ipDict):
    try:
        ip42 = request.urlopen('http://ip.42.pl/raw').read().decode('utf-8')
        ipDict[ip42] = ipDict.setdefault(ip42, 0) + 1
    except Exception as e:
        logging.error(e)
        pass

# jsonip
def jsonip(ipDict):
    try:
        jsonip = json.loads(request.urlopen('http://jsonip.com').read().decode('utf-8'))['ip']
        ipDict[jsonip] = ipDict.setdefault(jsonip, 0) + 1
    except Exception as e:
        logging.error(e)
        pass

# httpbin
def httpbin(ipDict):
    try:
        httpbin = json.loads(request.urlopen('http://httpbin.org/ip').read().decode('utf-8'))['origin']
        ipDict[httpbin] = ipDict.setdefault(httpbin, 0) + 1
    except Exception as e:
        logging.error(e)
        pass    

# ipify
def ipify(ipDict):
    try:
        ipify = json.loads(request.urlopen('https://api.ipify.org/?format=json').read().decode('utf-8'))['ip']
        ipDict[ipify] = ipDict.setdefault(ipify, 0) + 1
    except Exception as e:
        logging.error(e)
        pass    

# ip-api
def ipapi(ipDict):
    try:
        ipapi = json.loads(request.urlopen('http://ip-api.com/json').read().decode('utf-8'))['query']
        ipDict[ipapi] = ipDict.setdefault(ipapi, 0) + 1
    except Exception as e:
        logging.error(e)
        pass    


if __name__ == '__main__':

    logger.setup_logging()
    conf = json.load(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "conf.json"), "r"))
    Access_Key_Id = conf['access_key']
    Access_Key_Secret = conf['access_secret']
    Domains = conf['domains']
    
    try:
        get_ip()
        aliddns.initAliddnsApi(Access_Key_Id, Access_Key_Secret)
        for domain in Domains:
            ddns(domain)
    except Exception as e:
        logging.error(e)
        pass
