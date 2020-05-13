import requests
from lxml import html


class Cat:
    def __init__(self, name):
        self.name = name

    def nyan(self):
        print(f'{self.name} meows nyan')

    @classmethod
    def get_info(self):
        raw_content = requests.get('http://man7.org/linux/man-pages/man1/cat.1.html')
        html_tree = html.fromstring(raw_content.content.decode())
        info = html_tree.xpath('/html/body/pre[2]')[0].text.strip()
        return info
