from bs4 import BeautifulSoup
import re
from urllib import parse

class HtmlParser(object):

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))

        for link in links:
            new_url = link['href']
            new_full_urls = parse.urljoin(url, new_url)
            new_urls.add(new_full_urls)
        return new_urls

    def _get_new_datas(self, url, soup):

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        res_data = {}
        res_data['url'] = url
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.getText()
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.getText()
        return res_data


    def parse(self, page_url, html_count):

        if page_url is None or html_count is None:
            return
        soup = BeautifulSoup(html_count, 'html.parser')
        urls = self._get_new_urls(page_url, soup)
        datas = self._get_new_datas(page_url, soup)
        return urls, datas
