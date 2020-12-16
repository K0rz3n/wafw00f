# waf 检测能力补充

标签（空格分隔）： 工具

---

## 0x00 现状


目前最好的工具就是 wafw00f 了，但是对于国内的一些 waf 来讲还是存在一些局限性，这个就需要我利用代码进行弥补,实际上就是写插件，然后重新编译，实际操作就是将wafw00f fork 到本地仓库，然后将原仓库作为我们本地仓库的远端仓库，然后定期同步本地仓库和远端仓库，就能将其原作者的更新和我们的更新进行合并


暂时不改变原始的项目代码，目的是为了合并的时候不出现冲突，方便我们进行自动化，后期如果有需要可以考虑修改整体的代码逻辑，增强我们的检测能力，例如增加更多的payload


譬如，我在［[https://github.com/skyswind/GIScript.git](https://github.com/skyswind/GIScript.git)］上通过Github.com[网站页面](https://github.com/skyswind/GIScript.)Fork到自己的空间。
然后，在本地通过命令行工具取到本地目录中，如下。
```
git clone https://github.com/supergis/GIScript.git
```
按照如下步骤操作即可：
```
#! /bin/bash

echo "Create local branch..."
git checkout -b newBranch

echo "Commit branch changes..."
git add .
git commit -m "add newBranch support..."

echo "Switch to master branch..."
git checkout master

echo "Merge changes from the new branch to the master branch..."
git merge newBranch

echo "Delete the new branch..."
git branch -D newBranch

echo "Specify remote source..."
git remote add upstream https://github.com/EnableSecurity/wafw00f.git

echo "Get updates from remote sources..."
git fetch upstream

echo "Merged into the local library..."
git merge upstream/master

echo "Submit to the local repository..."
git commit -a -m "merged upstream."

echo "Push and submit to my own github repository."
git push

echo "end..."
```




## 0x01 常见的 waf 以及对应的识别情况


![此处输入图片的描述][1]

[常见waf 拦截页面][2]

### 1.360 磐云(已添加)


#### 特征：

    1.200-> 473
    2.Server: panyun/2.0.5


#### 脚本
panyun360.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Panyun (360 Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'panyun/(.*?)')),
        self.matchStatus(473)
        
    ]
    if all(i for i in schemes):
        return True
    return False
```


### 2.akamai(已补充)


#### 特征

    
    1.Server: GHost
    2.content:<TITLE>Access Denied
    
#### 脚本
akamai.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Akamai (Akamai Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'GHost')),
        self.matchContent(r'<TITLE>Access Denied'),
    ]
    if all(i for i in schemes):
        return True
    return False
```


### 3.阿里云(已补充)


#### 特征
    
    
    1.content:g.alicdn.com/sd/punish/waf_block.html
    

#### 脚本


aliyun.py


```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'aliyun (alibaba Technologies)'


def is_waf(self):
    schemes = [
        
        self.matchContent(r'g\.alicdn\.com/sd/punish/waf_block\.html'),
        self.matchContent(r'您的访问被阻断'),
        self.matchContent(r'detected malicious traffic from your network'),
        self.matchContent(r'/waf\.123\.123'),
        self.matchContent(r'应用防火墙'),
        self.matchContent(r'errors\.aliyun\.com'),


    ]
    if any(i for i in schemes):
        return True
    return False
```



### 4.安恒信息｜明御web 防火墙(已添加)
#### 特征：

    
    1.status:400
    2.content:<title>Error 400 ——
    3.content:<strong>400
    

#### 脚本


mingyu.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'mingyu (anheng Technologies)'


def is_waf(self):
    schemes = [
        self.matchStatus(400),
        self.matchContent(r'<title>Error 400 —— (.*?)'),
        self.matchContent(r'<strong>400'),
    ]
    if all(i for i in schemes):
        return True
    return False
```




### 5.安全狗(可识别)
### 6.安赛多源联动waf(未找到用例)
### 7.安全帮云waf(未找到用例)
### 8.百度云加速(可识别)
### 9.毕安云盾(未找到用例)
### 10.长亭雷池(已补充)


#### 特征：

    content：<!-- event_id: b2b0befdc02e43c3a7075f8cf1e622e -->


#### 脚本
leichi.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'leichi (chaitin Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<!-- event_id:(.*?)-->'),
        
    ]
    if any(i for i in schemes):
        return True
    return False
```
### 11.迪普web防火墙(未找到用例)
### 12.东软 neteye(未找到用例)
### 13.华数网络云waf(未找到用例)
### 14.华为云(可识别)
### 15.浩克web 防火墙(未找到用例)
### 16.交大捷普(未找到用例)
### 17.金山云(未找到用例)
### 18.蓝盾waf(可识别)
### 19.浪潮云waf(未找到用例)
### 20.六壬网安 waf(未找到用例)
### 21.绿盟科技waf(未找到用例)
### 22.能信安waf(未找到用例)
### 23.奇安信waf(可识别)
### 24.启明星辰waf(未找到用例)
### 25.青云waf(未找到用例)
### 26.任子行waf(已添加)


##### 特征：


    1.content:<title>Request Denied
    2.content:RZX IT by
    3.content:Web Page Blocked!


#### 脚本：
rzx.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'RZX (RZX Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<title>Request Denied'),
        self.matchContent(r'RZX IT by'),
        self.matchContent(r'Web Page Blocked!'),
    ]
    if all(i for i in schemes):
        return True
    return False
```
### 27.瑞数waf(未找到用例)
### 28.山石网科(未找到用例)
### 29.深信服(未找到用例)
### 30.盛邦 raywaf(已添加)


#### 特征：
    1.DrivedBy: WAF-Engine/6.0.0
#### 脚本：
shengbang.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'raywaf (shengbang Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('DrivedBy', 'WAF-Engine/(.*?)')),
        
    ]
    if any(i for i in schemes):
        return True
    return False
```
### 31.上海云盾(已添加)


#### 特征

    1.status:461
    2.Server: WAF/2.4-12.1
    3.<div class="err-tips-en">Blocked by Cloud WAF
    

#### 脚本：
shyundun.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'shyundun (shanghaiyundun Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'WAF/(.*?)')),
        self.matchContent(r'<div class="err-tips-en">Blocked by Cloud WAF'),
        self.matchStatus(461)
    ]
    if all(i for i in schemes):
        return True
    return False
```


### 32.腾讯云(已补充)


#### 特征：
    <title>501 Not Implemented
##### 脚本
tencentcloud.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'TencentCloud (Tencent Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<title>501 Not Implemented'),
        self.matchStatus(501)

    ]
    if all(i for i in schemes):
        return True
    return False
```
### 33.天融信waf(未找到用例)
### 34.天下数据(未找到用例)
### 35.网宿科技(已添加)


#### 特征：
    Server: waf/4.24.1-6.el6
    <img src="https://blocksrc.haplat.net/waf_forbidden_file/waf-interTip.jpg" />
#### 脚本
wangsu.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'wangsu (wangsu Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'WAF/(.*?)')),
        self.matchContent(r'<img src="https://blocksrc\.haplat\.net/waf_forbidden_file'),
        
    ]
    if all(i for i in schemes):
        return True
    return False
```
### 36.网易易盾(未找到用例)
### 37.watchdog(未找到用例)
### 38.孝道科技(未找到用例)
### 39.香港电讯(未找到用例)
### 40.新华三(未找到用例)
### 41.铱讯科技(已补充)
#### 特征：

    <TITLE>访问禁止
    检测到可疑访问


#### 脚本
yxlink_new.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'yxlink (yxlink Technologies)'


def is_waf(self):
    schemes = [
       
        self.matchContent(r'<TITLE>访问禁止'),
        self.matchContent(r'检测到可疑访问'),
    ]
    if all(i for i in schemes):
        return True
    return False
```
### 42.云奕科技(已添加)


#### 特征：

    1.X-Protected-By: YunYiSec
    2.Server: YiDun/5.8.7
    3.<h1>An Error Was Encountered</h1>
    4.<p>The URI you submitted has disallowed characters.</p>


#### 脚本
yidun.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'yidun (yunyi Technologies)'


def is_waf(self):
    schemes = [

        self.matchHeader(('X-Protected-By', 'YunYiSec')),
        self.matchHeader(('Server', 'YiDun/(.*?)')),
        self.matchContent(r'<h1>An Error Was Encountered</h1>'),
        self.matchContent(r'<p>The URI you submitted has disallowed characters.</p>'),
    ]
    if all(i for i in schemes):
        return True
    return False
```


### 43. 创宇盾(已补充)


#### 特征：

    1.<span class="r-tip01"><%= error_403 %>
    2.'hacker';
    3.<center>client: (.*?), server: (.*?), time: (.*?)</center>
    

#### 脚本
chuangyudun.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'chuangyudun (zhidaochuangyu Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<span class="r-tip01"><%= error_403 %>'),
        self.matchContent(r"'hacker';"),
        self.matchContent(r'<center>client: (.*?), server: (.*?), time: (.*?)</center>'),
  
    ]
    if all(i for i in schemes):
        return True
    return False
```


### 44.众易安全(未找到用例)
### 45.aws(可识别)
### 46.梭子鱼waf(可识别)
### 47.cato networks(未找到用例)
### 48.checkpoint(未找到用例)
### 49.cloudflare(可识别)
### 50.fortinet(可识别)
### 51.incapsula(可识别)
### 52.juniper(未找到用例)
### 53.microsoft(可识别)
### 54.palo(可识别)
### 55.R&S waf(未找到用例)
### 56.signal science(未找到用例)


### 57. D 盾(已添加)
#### 特征：

    1.<title>D盾_拦截提示</title>
    2.403
    

#### 脚本
ddun.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ddun (ddun Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<title>D.*?_'),
        self.matchStatus(403)
    ]
    if all(i for i in schemes):
        return True
    return False
```
### 58.云锁(可识别)
### 59.宝塔(已添加)
#### 特征

    <title>宝塔网站防火墙</title>
    <li>您提交的内容包含危险的攻击请求</li>
    <li>这是误报，请联系宝塔 <a href="http://www.bt.cn/bbs" target="_brank">http://www.bt.cn/bbs</a></li>

#### 脚本
baota.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'baota (baota Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<title>宝塔网站防火墙'),
        self.matchContent(r'<li>您提交的内容包含危险的攻击请求'),
        self.matchContent(r'这是误报，请联系宝塔 <a href="http://www\.bt\.cn/bbs" target="_brank">'),
        
    ]
    if any(i for i in schemes):
        return True
    return False
```
### 60.网防 G01(已添加)


#### 特征：

    1.Server: legendsec http proxy
    2.<h1 class="text_404">403</h1>


#### 脚本
wangfang.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'wangfangG01 (gongan Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'legendsec http proxy')),
        self.matchContent(r'<h1 class="text_404">403</h1>'),
        
    ]
    if all(i for i in schemes):
        return True
    return False
```
### 61.护卫神(直接封 ip)


添策略请求失败的默认是存在waf


### 62.西数 WTS(可识别)
### 63.Mod_Security(未找到用例)
### 64.OpenRASP(未找到用例)
### 65.dotDefender(已添加)
### 66.兜底策略(已添加)


#### 特征：

    1.content:Access Denied
    2.status:403

#### 脚本：
minimum.py
```
#!/usr/bin/env python
'''
Copyright (C) 2020, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Minimum (Minimum strategy)'


def is_waf(self):
    schemes = [
        self.matchContent(r'Access Denied'),
        self.matchContent(r'Request Denied'),
        self.matchContent(r'访问禁止'),
        self.matchContent(r'检测到可疑访问'),
        self.matchStatus(403),

    ]
    if any(i for i in schemes):
        return True
    return False
```


  [1]: https://picture-1253331270.cos.ap-beijing.myqcloud.com/waf.jpg
  [2]: https://mp.weixin.qq.com/s/3oZn1mPK-2LuKbIyFlJd4Q