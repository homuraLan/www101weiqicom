from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

process = CrawlerProcess(get_project_settings())

process.crawl('DownloadSgf')
process.start()
