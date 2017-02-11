class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    #向管理器中添加新的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 向管理器中添加批量url
    def add_new_urls(self, urls):
        if urls is None or len(urls) ==0:
            return
        for url in urls:
            self.new_urls.add(url)


    #判断管理器中是否有新的待爬取的url
    def has_new_url(self):
        return len(self.new_urls) !=0

    #从url管理器中获取一个新的url
    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

