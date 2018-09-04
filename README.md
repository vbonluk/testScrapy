最近打算接触Scrapy爬虫框架，虽然我之前已经利用BeautifulSoup结合HTMLParser已经mysql数据库来写了一个YouTube搬运到Bilibili的工具，但是最新又有新的需求了，就是每天定时爬取医院HPV9的库存，然后自动预约。于是开始用Scrapy来做一个。

由于我是用Python3.6来写的，我Mac有2.7和3.6两个版本。所以我安装Scrapy的时候只安装在Python3的环境。

	pip3 install Scrapy
	
安装完毕后，我们需要使用Scrapy的startproject命令来生成默认的文件模板。

	scrapy startproject testScrapy
	
![](http://oapglm9vz.bkt.clouddn.com/WX20180904-151236.png)

然后我们打开PyCharm，然后选择file，点击open，选择当前根目录来导入项目。

![](http://oapglm9vz.bkt.clouddn.com/WX20180904-151650.png)

我们可以看到完整的目录。

接下来我们写一个爬虫，在spiders目录下新建一个spider.py爬虫文件，并写入以下内容

	# encoding:UTF-8
	from scrapy.spiders import Spider
	import requests

	class spider(Spider):
    	name = 'hpv9'
    	start_urls = [
        	'http://www.kwh.org.mo/'
    	]

    	def __init__(self):
        	pass
 
上文中，我们可以看到我们新建了一个spider的类，继承自Spider。还定义了变量name和start_urls。
 
name变量用于声明此爬虫文件的唯一名称，Scrapy运行时会根据这个来找到你写的spider.py这个继承Spider的爬虫文件。来运行。
 
star_urls是一个你要抓取的网站列表。
 
下面我们继续完善代码：
 
 	# encoding:UTF-8
	from scrapy.spiders import Spider
	import requests

	class spider(Spider):
    	name = 'hpv9'
    	start_urls = [
        	'http://www.kwh.org.mo/'
    	]

    	def __init__(self):
        	pass

    	def parse(self, response):
        	titles = response.xpath('//b').extract()
        	for title in titles:
            	text = title.strip()
            	print(text)
 
我们可以看到新增了parse函数，这个函数就是这个爬虫解析数据的开始。当Scrapy下载完网页内容后会调这个函数。我们要做的是进行内容的解析以及采集。

下面我们就可以尝试运行这个项目了。当然了我们是通过pycharm来运行项目。但是默认Scrapy默认是通过终端来运行的

cd到spider.py的目录，然后执行

	scrapy crawl hpv9
	
由于scrapy是基于crawl的，所以要加上crawl这个命令。后面的hpv9便是我们上面类里面定义的name，是唯一的，所以scrapy能找到这个spider.py来运行。

但是我们习惯于使用IDE给我们带来的便利，想要用Pycharm来运行怎么运行呢？要知道，scrapy是不支持直接使用IDE运行的。需要配置一下才可以。

### PyCharm 运行Scrapy的配置

我们在scrapy.cfg文件的同级目录下面用Pycharm新建一个名为main.py的文件，并写入以下内容：

	from scrapy import cmdline

	cmdline.execute('scrapy crawl hpv9'.split())
	
然后我们打开Pycharm的菜单栏，选择Run，再选择Edit Configurations

![](http://oapglm9vz.bkt.clouddn.com/WechatIMG263.png)

点击+号，新增python运行配置。

![](http://oapglm9vz.bkt.clouddn.com/WX20180904-154119.png)

然后name写hpv9，再指明scrip的路径为main.py的路径

![](http://oapglm9vz.bkt.clouddn.com/WX20180904-154329.png)

再点击右上角的绿色运行三角形然后就可以运行了，或者快捷键：ctrl + R

![](http://oapglm9vz.bkt.clouddn.com/WX20180904-154624.png)


运行的时候原本来终端的log都会打印在Pycharm的终端里面了。

![](http://oapglm9vz.bkt.clouddn.com/WX20180904-154813.png)

白色字的就是我们爬虫抓到的数据啦！红色的可以忽略。红色的是scrapy打印的。

至此，简明的运行教程以及第一个scrapy爬虫已经可以运行啦。

本文的demo已经上传到GitHub：

<https://github.com/vbonluk/testScrapy>

原创作品，欢迎转载，转载请声明出处：<http://www.真无聊.com>
 
友情链接联系:5914018@qq.com
 
交流QQ群：271568188
