# 参考: https://github.com/fxsjy/jieba

from bs4 import BeautifulSoup
import jieba
import math
import jieba.analyse

# 解析html文件, 若不是html文件可以不使用BeautifulSoup
soup = BeautifulSoup(
    open("./file/合并.html", encoding='utf-8').read(), "html.parser")
html_text = soup.get_text() # 获取文本
# 删除词频
delText = ['Map', '对于', '2018', '10', '20']

jieba.load_userdict('./file/dict.txt')  # 自定义词库

# 删除低词频 | 无用词
for item in delText:
    jieba.del_word(item)
# 分析关键字 基于 TF-IDF 算法
extract_tags = jieba.analyse.extract_tags(html_text, topK=20, withWeight=True)
# 输出
for item in extract_tags:
    print(item)

# title = soup.find_all('h1')
# for item in title:
#     print(item)
# print(soup.prettify())
