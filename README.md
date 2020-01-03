# on-line_data_process
train_data_pre
## 基本用途
是对CustomUserCorpusTask 生成的用户语料以及爬取的新闻语料的相关处理，为最终生成训练数据提供相关格式的文件
## 文件说明
### add_no_space.py 
新闻语料处理标点符号，给标点与单词间加空格，同时去除表情
##### 参数：
参数1:新闻语料路径

参数2:表情文件路径
### changeCase.py
对新闻加用户语料转换大小写，如果大写形式在词表中，则保留，否则，全部转换成小写形式
##### 参数：
参数1:词表路径

参数2:原始语料路径

参数3:输出路径
### data_utility_nomap.py
将语料转换成无map匹配的格式
i a m h a p p y|#|I am  happy
##### 参数：
参数1:原始语料路径

参数2:表情文件路径
### data_utility_random_letter.py
将语料转换成匹配键码的格式
i a y h a p|#|I am  happy
##### 参数：
参数1:原始语料路径

参数2:map文件路径

参数3:表情文件路径
### mapdel.py
处理word_map文件，将其中空格上屏词汇去除，同时先按照字母升序，之后按照词频降序
##### 参数：
参数1:word_map路径（后缀.txt，生成_sort）
### passemoji.py
去除语料中带表情的语句
##### 参数：
参数1:表情文件路径

参数2:输入文件路径（后缀.txt 生成.noemoji）
### train_words_unigrm_compare_words.py
wordcount词频文件与词表对照结果
##### 参数：
参数1:词表文件路径

参数2:生成wordcount文件路径（后缀.wordcount 生成.true .false）
### wordcount_noemoji.py
新闻加用户不包含emoji的语料统计出的词频
##### 参数：
参数1:语言locale

参数2:原始语料路径（后缀.txt 生成.wordocunt）

参数3:表情文件路径
### del_no_space.py
删除单词和标点符号间的空格
##### 参数：
参数1:原始语料路径（后缀.txt 生成.despace）
### true_rate.py
训练语料中的验证集和测评语料相对于大词表中的命中率
##### 参数：
参数1:locale  
参数2:生成训练数据的文件夹名称  
参数3:一元词表路径  
参数4:测评语料文件夹名称，包含五个文件（语言_data.txt 语言_facebook.txt 语言_im.txt 语言-facebook.txt 语言-twitter.txt 语言-web.txt） 

