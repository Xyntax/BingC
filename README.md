# BingC
基于Bing搜索引擎的 **IP->域名** 查询，多线程，支持`Bing API`，用于旁站及C段收集。  
  
`python bingC.py IP/MASK [output_path]`  


配置
---
默认为不使用`Bing API`进行查询，也可以出结果但不如`API`准确。  
申请API-Key的过程见后文附录  
  
编辑`config.py`  
```
# 修改为你的主账户密钥
accountKey = 'JaDRZblJ6OheyvTxxxxxxxxxxxxxxxxWx8OThobZoRA' 

# 修改此项为True，开启API搜索
ENABLE_API = True 
```

查询旁站
----
```
λ python bingC.py 139.129.132.156

Running...
139.129.132.156 -> www.cdxy.me | 乐枕的家
139.129.132.156 -> 139.129.132.156 | 乐枕的家
139.129.132.156 -> www.presentxin.com | www.presentxin.com
139.129.132.156 -> www.cdxy.me | CTF – 乐枕的家
Total: 4
```

查询C段
----
```
λ python bingC.py 139.129.132.0/24

Running...
139.129.132.237 -> www.huiu-technology.com | 产品展示 - 珠海汇优科技有限公司
139.129.132.72 -> www.vsqq360.cn | 登录-PK淘宝-惊喜无限
139.129.132.6 -> ld.yanlejy.com | 娄底严乐会计培训学校_娄底学会计_娄底会计培训
139.129.132.81 -> www.jiulide.com | 原浆--酒立得96766_武汉市内免费送货上门
139.129.132.237 -> www.fengdajd.com | 服务咨询- 珠海丰大机电设备安装有限公司
139.129.132.162 -> www.hjzj-vip.com | 惠聚指尖微信管理系统
139.129.132.147 -> seahi.me | 听海 - 听，海在说
139.129.132.237 -> www.zhshunbo.com | 珠海顺博机电设备有限公司珠海空压机,珠海空压机配件耗材 ...

...

```


附：API-KEY申请流程
-------------
注意以下步骤在选择地区时都**不要选择中国**，其余随意  
1. `https://login.live.com`注册并登陆  
2. `https://datamarket.azure.com/dataset/bing/search` 再注册为“开发人员”，并登陆  
3. `https://datamarket.azure.com/account` 点右上部分的`My Account`或者`我的账户`  
4. 在该页面下方找`主账户秘钥`或者`Primary AccountKey`  
5. 复制到`config.py`相应位置，并设置`ENABLE_API = True`即可  