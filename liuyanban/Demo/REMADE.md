用“极验”（ http://www.geetest.com/ ）实现一个限制 spam 的留言板。

具体需求如下：

使用 fingerprint 生成浏览器唯一 ID（ https://github.com/Valve/fingerprintjs ）（暂不考虑用户每次自己设置 ID 绕过验证的情况）

正常留言不显示“极验验证码”和校验

对异常留言，显示“极验验证码”，并进行校验

P.S. 异常留言是指单一 IP 或单一用户进行高频登录、留言操作，比如每 5s～10s 一次。阈值请不要设置过高，以便测试。



界面要求：

显示当前用户用户 ID（fingerprint 生成的唯一 ID 或者加分项中所说的注册用户的 ID）

显示留言板中已有的留言，和留言的输入框


技术栈：

Python3 + Flask + Jinja2

requests 网络请求库

用 pipenv 做虚拟环境和管理第三方依赖

MySQL 存留言，peewee 做 ORM， Redis 做计数器

