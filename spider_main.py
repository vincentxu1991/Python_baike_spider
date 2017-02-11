import url_manager
import html_download
import html_output
import html_parser

class SpiderMain():

    #在构造函数中初始化所需要的对象
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownLoad()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()

    def craw(self, root_url):
        count = 1
        #将root_url添加进url管理器(添加单个)
        self.urls.add_new_url(root_url)
        #此时,url管理器中已经存在待爬取的url,启动爬虫循环
        while self.urls.has_new_url():
            try:
                #获取即将开始的url链接
                new_url = self.urls.get_new_url()
                print("craw %d :%s" % (count, new_url))
                #开始爬起,并将结果储存在html_count变量中
                html_count = self.downloader.download(new_url)
                print("html_count :",html_count)
                #调用解析器解析页面数据,得到新的url列表,及该页面的数据
                new_urls,new_data = self.parser.parse(new_url,html_count)
                print("new_urls :", new_urls)
                print("new_data :",new_data)
                #将解析出的url添加进url管理器(添加批量)
                self.urls.add_new_urls(new_urls)
                #对数据的收集
                self.output.collect_data(new_data)

                if count == 3:
                    break
                count=count +1

            except:
                print("craw failed")
        self.output.output_html()




if __name__ =='__main__':
    #设定入口URL
    root_url = "http://baike.baidu.com/view/21087.htm"
    #启动爬虫
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)