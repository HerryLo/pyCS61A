## jieba文本数据分析

我是为了分析我自己的印象笔记文本，但是我没有将自己印象笔记数据上传。你可以在代码中替换自己的文本数据

* 使用 ```BeautifulSoup``` 会html文本内容进行提取

[参考: https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)

```python
soup = BeautifulSoup(
    open("./file/html.html", encoding='utf-8').read(), "html.parser")
html_text = soup.get_text() # 获取文本
```
如果html格式文件，可以不使用```BeautifulSoup```对文本进行解析修改。如果是html格式文件，直接替换掉open的文件地址即可，如果是其他格式文件就直接使用open开启, 例如:

```python
soup = open("./file/html.txt", encoding='utf-8').read()
```

* ```jieba```完成关键词提取

[参考: https://github.com/fxsjy/jieba](https://github.com/fxsjy/jieba)
```python
# 分析关键字 基于 TF-IDF 算法
extract_tags = jieba.analyse.extract_tags(html_text, topK=20, withWeight=True)
# 输出
for item in extract_tags:
    print(item)
```


