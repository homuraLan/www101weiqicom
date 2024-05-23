#使用说明：
# 方法一：
# 1. 在本文件的同级目录下打开powershell shift+右键 可以看到powershell
# 2. pip install scrapy
# 3. ![环境变量](https://zhuanlan.zhihu.com/p/621645640#:~:text=5%E3%80%81%E6%A3%80%E9%AA%8C%E6%98%AF%E5%90%A6%E6%88%90%E5%8A%9F%EF%BC%9Apip%E5%91%BD%E4%BB%A4%E4%B8%80%E8%88%AC%E6%98%AF%E5%9C%A8scripts%E7%9B%AE%E5%BD%95%E9%87%8C%E9%9D%A2%E7%9A%84%EF%BC%8C%E6%89%80%E4%BB%A5%E6%88%91%E4%BB%AC%E5%83%8F%E4%B9%8B%E5%89%8D%E9%82%A3%E6%A0%B7%E8%BF%9B%E5%85%A5%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E7%BC%96%E8%BE%91%E7%95%8C%E9%9D%A2%EF%BC%8C%E7%9C%8B%E4%B8%8B%E6%9C%89%E6%B2%A1%E6%9C%89%E8%BF%99%E4%B8%AA%E7%9B%AE%E5%BD%95%E2%80%9C.............%5CPython39%5CScripts%E2%80%9D%EF%BC%8C%E6%B2%A1%E6%9C%89%E7%9A%84%E8%AF%9D%EF%BC%8C%E5%B0%B1%E5%9C%A8python39%E4%B8%8B%E9%9D%A2%E5%BB%BA%E7%AB%8B%E4%B8%80%E4%B8%AAScripts%E7%9B%AE%E5%BD%95%EF%BC%88%E6%B3%A8%E6%84%8F%E5%A4%A7%E5%B0%8F%E5%86%99%EF%BC%9B%E8%BF%98%E6%9C%89%E5%B0%B1%E6%98%AF%E6%88%91%E5%AE%89%E8%A3%85%E7%9A%84Python%E6%98%AF3.9%E7%89%88%E6%9C%AC%E7%9A%84%EF%BC%8C%E5%A6%82%E6%9E%9C%E6%98%AF37%E7%89%88%E6%9C%AC%E7%9A%84%E5%B0%B1%E6%98%AFPython37%EF%BC%8C%E7%9B%AE%E5%BD%95%E6%89%80%E5%9C%A8%E8%B7%AF%E5%BE%84%E4%BB%A5%E5%A4%A7%E5%AE%B6%E5%AE%9E%E9%99%85%E5%AE%89%E8%A3%85%E7%9A%84%E8%B7%AF%E5%BE%84%E4%B8%BA%E5%87%86%EF%BC%89)
# 4. 重启powershell
# 5. scrapy crawl DownloadSgf
# 方法二：
# 直接运行carwl.exe
# 如果你有棋谱可以先执行方法一的第一步，然后： .\sgf2gif.exe 你棋谱所在的文件夹

[CrawlingTargets]
# 详见https://www.101weiqi.com/questionlib/
classification=其他分类题目
# 级别 例如：15K
level=吃子题目
#要从第几页开始抓取
StartPage=1
#要抓取多少页
EndPage=2
#抓取延迟，网站有反爬机制，单IP建议不要调太低
delay=0.1

[options]
#播放速度: 
   #输入正整数, 数值越小速度越快, 默认值是50
delay = 50;
#显示手数:
   #输入正整数N, 表示显示最后N手, 可以为0
numbers = 0;
#棋谱分割:
   #按手数分割棋谱, 有两种格式, 均要求间隔大于5
   #(A) 星号+数字N, 表示每N手分割一次. 例: *50
   #(B) 空格分割, 递增的整数序列. 例: 120 170 260
   #也可留空, 表示不分割
splitCount = 0;
#棋子大小:
	#15 ~ 50 (像素)
cw = 23;


