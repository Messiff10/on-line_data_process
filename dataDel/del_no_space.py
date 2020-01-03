import codecs
import os
import re
import sys

from utils.reExpression import replace_quotes_1, replace_brackets_1, replace_brackets_2 \
    , replace_brackets_3, replace_brackets_4, replace_brackets_5, replace_brackets_6, replace_brackets_7 \
    , replace_brackets_8, replace_brackets_9, replace_clock_time, replace_brackets_1, replace_quotes_2, \
    replace_quotes_3, replace_brackets_10, replace_brackets_11, replace_quotes_4, replace_line_time

regex = re.compile(
    '[\±+_·&‰%¢$£¥₱€#@†*‡★؟\‚\:;/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞°↑^←‚\:;?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_·+±\\﴾*★٭\‚‹:;؛∆≠=≈!∞°،↑)}\]’’>›»’↓→\±+_\·&‰٪%¢£¥₱€#@†*‡★\©®™℅]')  # ar
regex2 = re.compile('\s+')
regex3 = re.compile(r'("\w+")')
# data_folder = '/Users/ff/Desktop/测评数据/去空格'
# names = []

# string="hh hh ?? ?! ????AAA    ?  ?  A ??"
# ss=re.findall(regex,string)
# for s in ss:
#     string=string.replace(re.sub('\s+',string),'')
# print(string)

# 无后缀
# for dir_path, subpaths, files in os.walk(data_folder):
#     for name in files:  # 文件夹下的所有文件
#         if not name.endswith('.DS_Store'):
#             file_path = os.path.join(dir_path, name)
#             names.append(name)
# 有后缀
# for dir_path, subpaths, files in os.walk(data_folder):
#     for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
#         file_path = os.path.join(dir_path, name)
#         names.append(name)
# for name in names:
#     file_path = os.path.join(data_folder, name)
#     print(file_path)
# 有后缀
# if os.path.exists(file_path.replace('.txt', '.despace')):
#     print("remove:", file_path.replace('.txt', '.despace'))
#     os.remove(file_path.replace('.txt', '.despace'))
file_path = sys.argv[1]
with open(file_path, 'r', encoding='utf-8') as f_in:
    # 有后缀
    # with open(file_path.replace('.txt', '.despace'), 'w', encoding='utf-8') as f_out:
    # 无后缀
    with open(file_path.replace('.txt', '.despace'), 'w', encoding='utf-8') as f_out:
        for lines in f_in:
            line = lines.strip()
            line = replace_brackets_1(line)
            line = replace_brackets_9(line)
            line = replace_brackets_8(line)
            line = replace_brackets_7(line)
            line = replace_brackets_6(line)
            line = replace_brackets_5(line)
            line = replace_brackets_4(line)
            line = replace_brackets_3(line)
            line = replace_brackets_2(line)
            line = replace_brackets_10(line)
            line = replace_brackets_11(line)
            line = replace_quotes_2(line)
            line = replace_quotes_3(line)
            line = replace_clock_time(line)
            line = replace_quotes_1(line)
            line = replace_quotes_4(line)
            # line = replace_line_time(line)
            # print(line)

            # line.replace()
            # words=re.find(regex,line)
            words = re.findall(regex, line)
            for w in words:
                # line=line.replace(' ','')
                # 先去空格
                line = re.sub('\s+', ' ', line)
                line = line.replace(' ' + w, w)
                line = re.sub('\s+-\s+', '-', line)
                # line = re.sub(regex2, ' ', line)
                # line = line.replace(w+' ' , w)
                # line = re.sub('\"\s+(\w)+\s+\"',r'\1',line)
                # line = line.replace(w, w+' ')
                # line = line.replace(w+' ' , w)
                # line = line.replace('  ', '')
                # 加空格
                # line = line.replace(w, ' ' + w + ' ')  # 加空格
                # line = re.sub('\s+', ' ', line)
            # print(lines.strip()+'\t'+line)
            f_out.write(line.strip())
            f_out.write('\n')
print("Finsh line")
# print(line)
