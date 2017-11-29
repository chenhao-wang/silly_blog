# silly_blog
my blog built with Django
# 解决Django中文上传报错
上传文件一直报错,只要标题和内容里面有中文,就会出现

`UnicodeEncodeError: 'ascii' codec can't encode characters in position`

搜了几圈全是基于python 2的 reload(sys) 和 sys.setdefaultencoding('utf-8')

然而python3改了一圈并没有用... 看文档说python3和django已经自带utf-8了

针对上传包含中文的文件报错问题, 最后才发现是apache2和locale来背锅

首先理解一个概念 locale [what are duty of locale and locale-gen commands?](https://askubuntu.com/questions/442843/what-are-duty-of-locale-and-locale-gen-commands)

locale是干什么的 

`
In computing, a locale is a set of parameters that defines the user's language, country and any special variant preferences that the user wants to see in their user interface. Usually a locale identifier consists of at least a language identifier and a region identifier.
`

locale-gen是干什么的

`Compiled locale files take about 50MB of disk space, and most users only need few locales. In order to save disk space, compiled locale files are not distributed in the locales package, but selected locales are automatically generated when this package is installed by running the locale-gen program.
`

所以就算我在每个.py文件都加上了`# _*_ coding:utf-8 _*_` ,这为了省空间的系统还是傻傻的读不懂啊

为了让ta读懂中文, 终端输入 `sudo locale-gen zh_CN.UTF-8` ,查看方法是`sudo locale-gen` 然后就会看到哪些语言包已经生成了

为了让apache也稳一点, 进入`sudo vi /etc/apache2/envvars` 在末尾加上

`export LANG='zh_CN.UTF-8'`

`export LC_ALL='zh_CN.UTF-8'`

最后在重启apache即可~

进入upload文件夹查看保存的文件,如果发现中文名为乱码,说明系统没有支持中文的显示,下载即可
```
sudo apt-get install language-pack-zh-hans
```
