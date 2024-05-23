# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from .sgf import on_g_qq

from .cookie import headers_str_to_dict, parse_cookie
from .GetGqq import getGqq,get_data_file_path