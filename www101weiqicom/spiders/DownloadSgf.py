import re
import subprocess
import scrapy
import os
import configparser
from urllib.parse import urljoin
from . import on_g_qq,getGqq,headers_str_to_dict,parse_cookie


class KdlSpider(scrapy.Spider):
    name = "DownloadSgf"
    allowed_domains = ["www.101weiqi.com", "static2.101weiqi.com"]
    questionlib="https://www.101weiqi.com/questionlib/"
    base_url="https://www.101weiqi.com"
    table = {
        "4路": "size4",
        "5路": "size5",
        "6路": "size6",
        "7路": "size7",
        "8路": "size8",
        "9路": "size9",
        "10路": "size10",
        "11路": "size11",
        "12路": "size12",
        "13路": "size13",
        "吃子题目": "questionchizi",
        "骗招题目": "questionpianzhao",
        "布局题目": "questionbuju",
        "官子题目": "questionguanzi",
        "中盘作战题": "questionzhongpan",
        "模仿题": "clone",
        "实战题": "questionshizhan",
        "棋理题": "questionqili"
    }
    custom_headers = headers_str_to_dict()
    cookie_dict = parse_cookie(custom_headers.get('Cookie', ''))
    config = configparser.ConfigParser()
    config.read('CrawlingTargets.ini', encoding='utf-8')
    CrawlingTargets = config['CrawlingTargets']
    def run_exe_with_args(self, exe_path, args):
        try:
            
            process = subprocess.Popen([exe_path] + args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            
            for line in process.stdout:
                print(line, end='')
            process.wait()
            return process.returncode
        except Exception as e:
            print("Error:", e)
            return -1
    def start_requests(self):
        #for url in self.start_urls:
        yield scrapy.Request(self.questionlib, headers=self.custom_headers, callback=self.parse)
        

    def parse(self, response):

        h4_titles = response.xpath('//h4/text()').getall()
        classification = self.CrawlingTargets['classification']
        StartPage = int(self.CrawlingTargets['StartPage'])
        EndPage = int(self.CrawlingTargets['EndPage'])
        level = self.CrawlingTargets['level']

        for title in h4_titles:
            if title in classification:
                selected_title_xpath = f'//h4[text()="{title}"]'
                next_div = response.xpath(selected_title_xpath + '/following-sibling::div[@class="row"][1]')
                links = next_div.xpath('.//a/@href').getall()
                for link in links:
                    if link.replace('/', '') == level:
                        for i in range(StartPage, EndPage):
                            if i > 1:
                                relative_url = link + f"?page={StartPage}"
                                full_url = urljoin(self.base_url, relative_url)
                            else:
                                relative_url = link
                                full_url = urljoin(self.base_url, relative_url)

                            yield scrapy.Request(full_url, headers=self.custom_headers, meta={'level': level}, callback=self.parse_page)

                    for key,value in self.table.items():
                        #print(key,value,level,link.replace('/', ''))

                        if key == level and value == link.replace('/', ''):
                            for i in range(StartPage, EndPage):
                                if i > 1:
                                    relative_url = link + f"?page={StartPage}"
                                    full_url = urljoin(self.base_url, relative_url)

                                else:
                                    relative_url = link
                                    full_url = urljoin(self.base_url, relative_url)


                                yield scrapy.Request(full_url, headers=self.custom_headers,meta={'level': key}, callback=self.parse_page)
                            break
                break
        

    def parse_page(self, response):
        level = response.meta['level']

        if not 'sgf' in response.meta:
            
            if not os.path.exists(level):
                os.makedirs(level)
                
            for item in response.css('.col-md-2.col-xs-6.col-sm-3 a'):
                href = item.css('::attr(href)').get()
                if href:
                    g_qq = getGqq(urljoin(self.base_url, href), self.cookie_dict, self.custom_headers)
                    on_g_qq(level=level, g_qq=g_qq)
                    #yield scrapy.Request(urljoin(self.base_url, href), headers=self.custom_headers, meta={'level': level,'sgf': True}, callback=self.parse_page)
        # else:
        #     script_content = response.xpath('//script[contains(., "var g_qq = ")]/text()').get()
        #     g_qq_match = re.search(r'var g_qq\s*=\s*(.*?);', script_content)
        #     if g_qq_match:
        #         g_qq_value = g_qq_match.group(1)
        #         getGqq(level, g_qq_value)

            else:
                print("未找到g_qq变量")

        self.run_exe_with_args('sgf2gif.exe', level)
    def save_image(self, response):
        # 获取meta中的图片名称
        image_name = response.meta['image_name']
        level = response.meta['level']
        # 将图片保存到本地
        with open(f'{level}/{image_name}', 'wb') as f:
            f.write(response.body)
            self.log(f'Saved file {image_name}')
