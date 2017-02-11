# coding:utf-8
import urllib.request

class HtmlDownLoad(object):
    def download(self, url):

        if url is None:
            return None

        response1 = urllib.request.urlopen(url)
        if response1.getcode() != 200:
            return None

        return response1.read()