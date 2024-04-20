import sys
import requests
import json
import time
from pyfiglet import Figlet
Old_api_url="http://hnqndaxuexi.dahejs.cn/stw/news/list?pageNumber=2&pageSize=100"
# Study_url="http://hnqndaxuexi.dahejs.cn/stw/news/study/1333257798674313218"
New_api_url="http://hnqndaxuexi.dahejs.cn/stw/banner/list"

def Newlen(Old_api_url):
    r = requests.get(Old_api_url)
    New_dict = json.loads(r.text)
    i = len(New_dict['obj']['news']['list'])
    return i
def Newid(i,Old_api_url):
    r=requests.get(Old_api_url)
    New_dict=json.loads(r.text)
    print("正在学习青年大学习第"+New_dict['obj']['news']['list'][i]['title'])
    Study_url = f"http://hnqndaxuexi.dahejs.cn/stw/news/study/{New_dict['obj']['news']['list'][i]['id']}"
    # print(Study_url)
    return Study_url
def Oleid(New_api_url):
    r=requests.get(New_api_url)
    New_dict=json.loads(r.text)
    # print(New_dict['obj'][0]['newsId'])
    #dict_keys(['id', 'title', 'imgUrl', 'link', 'newsId', 'disabled', 'newsType', 'study'])
    print("正在获取最新一期。。。。。。。。。。")
    print("最新一期是："+New_dict['obj'][0]['title'])
    print("正在学习中")
    Study_url=f"http://hnqndaxuexi.dahejs.cn/stw/news/study/{New_dict['obj'][0]['newsId']}"
    return Study_url
def Study(Study_url):
    headers={
        'accept':'*/*',
        'Origin':'http://hnqndaxuexi.dahejs.cn',
        'Accept-Language':'zh - CN, zh;q = 0.9',
        #'token':'o5_mOuAHQDsQstzpNF_z_CyX2t_k',
        'token':f'{sys.argv[1]}',
        'Proxy-Connection':'keep-alive',
        'Referer':'http://hnqndaxuexi.dahejs.cn/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090a13) XWEB/9105 Flue',
        'Content-Type':'application/x-www-form-urlencoded',
        'cookie':f'{sys.argv[2]}'
    }
    #'Cookie': 'stw=fd1771fb-c302-4dbd-8b29-9e4bac8d0994;yfx_c_g_u_id_10000051=_ck24042010360812773196098368853;yfx_f_l_v_t_10000051=f_t_1713580568269__r_t_1713580568269__v_t_1713580568269__r_c_0'
    data={
    }
    time.sleep(2)
    r=requests.post(url=Study_url,headers=headers,data=data)
    res=json.loads(r.text)
    if '200' in r.text:
        print("正在获取状态")
        if "您" in res['obj']:
            print(res['obj'])
        else:
            print("学习完成")
    else:
        return False
def main(New_api_url,Old_api_url):

    f = Figlet()
    print(f.renderText("Youth college！"))
    while 1:

        print("最新一期请按 ”1“ 自动刷往期请按 ”0“ 退出请按 ”q“")
        h=input(">>")
        if h=='0':
            print("正在获取往期数量")
            print("获取到"+str(Newlen(Old_api_url)))
            for i in range(0,int(Newlen(Old_api_url))):
                Study(Newid(i,Old_api_url))
            print("往期学习完成")
        if h=='1':
            Study(Oleid(New_api_url))
        if h=='q':
            f = Figlet()
            print(f.renderText("Bye!"))
            break
        if h!="":
            print("请重新选择")
main(New_api_url,Old_api_url)









