import itertools
import os


# 从文件中读取所有单词的word_map，结果格式为{ desired_word: { keys: freq } }
import random
import re



sequence_new = []
s="a" # A mira q bueno bb lo que sea es
regex=re.compile('\s+')
def getWordMap():
    word_map_dir = "/Users/ff/Desktop/测评数据/训练数据最后生成测试/word_map/es_US_map_sort.txt"
    # word_map_name = os.path.join(word_map_dir, ".txt")
    wordmap = {}
    with open(word_map_dir, 'r', encoding="utf-8") as input_file:
        current_word = ""
        current_map = {}
        for line in input_file:
            items = line.split("\t")
            desired_word = items[0].strip()
            keys = items[1].strip()
            freq = items[2].strip()

            if keys == "":  # 推荐正确，直接空格上屏
                continue

            if current_word == desired_word:
                current_map[keys] = freq
            else:
                if current_word != "":
                    wordmap[current_word] = current_map

                current_word = desired_word
                current_map = {}
                current_map[keys] = freq

        wordmap[current_word] = current_map
        # for word in wordmap.keys():
        #     print(word,wordmap[word])
    return wordmap
def random_pick_freq(sequence, freqs):
    # print(sequence,freqs)
    # sequence_new = [z for x, y in zip(sequence, freqs) for z in [x] * int(y)]
    if sequence not in sequence_new:
        for x, y in zip(sequence, freqs):
            # print(sequence,freqs)
            # print([x] * int(y))
            for z in[x] * int(y):
                # print(z)
                sequence_new.append(z)
            # print(z)
    # for a in sequence_new:
    #     print(a)
# def choiceone():
    while True:
        yield random.choice(sequence_new)

if __name__ == '__main__':
    wordmap_all=getWordMap()
    words = regex.split(s)
    for w in words:
        if w in wordmap_all.keys():
            wordmap = random_pick_freq(wordmap_all[w.lower()].keys(), wordmap_all[w.lower()].values())
            noise_word = ''.join(itertools.islice(wordmap, 10))
            # print("---------------", wordmap)
            # print("--------------",noise_word)
            output_line = " ".join(noise_word) + '\t' + w + '\n'
            print(output_line)
        else:
            pass
            # print(w.lower())


