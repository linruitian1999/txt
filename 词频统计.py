import jieba  
txt = open("新建文本文档.txt", encoding="utf-8").read()  
#加载停用词表  
stopwords = [line.strip() for line in open("stopwords1893.txt",encoding="utf-8").readlines()]  
jieba.suggest_freq(('火钳刘明'), True)
jieba.suggest_freq(('谢罪警告'), True)
jieba.suggest_freq(('开花就完事了'), True)
jieba.suggest_freq(('开花'), True)
jieba.suggest_freq(('文体两开花'), True)
jieba.suggest_freq(('章口就来'), True)
jieba.suggest_freq(('章口就莱'), True)
jieba.suggest_freq(('两开花'), True)
jieba.suggest_freq(('灵堂麦片'), True)
jieba.suggest_freq(('中美合拍'), True)
jieba.suggest_freq(('国际巨星'), True)
jieba.suggest_freq(('国际影星'), True)
jieba.suggest_freq(('我也喜欢'), True)
jieba.suggest_freq(('战术后仰'), True)
jieba.suggest_freq(('六老师'), True)
jieba.suggest_freq(('章老师'), True)
jieba.suggest_freq(('章金莱'), True)
jieba.suggest_freq(('零糖麦片'), True)
jieba.suggest_freq(('戏说不是胡说'), True)
jieba.suggest_freq(('石敢当'), True)
jieba.suggest_freq(('六学家'), True)
jieba.suggest_freq(('身份证'), True)
jieba.suggest_freq(('两个身份证'), True)
words  = jieba.lcut(txt)  
counts = {}  
for word in words:  
    #不在停用词表中  
    if word not in stopwords:  
        #不统计字数为一的词  
        if len(word) == 1:  
            continue  
        else:  
            counts[word] = counts.get(word,0) + 1  
items = list(counts.items())  
items.sort(key=lambda x:x[1], reverse=True)   
for i in range(100):  
    word, count = items[i]  
    print ("{:<10}{:>7}".format(word, count))
