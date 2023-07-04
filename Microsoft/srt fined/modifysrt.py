import docx
import re
import string

# 读取file2.docx中的单词
doc = docx.Document('script2.docx')
words_iter = (paragraph.text.strip() for paragraph in doc.paragraphs)

def compare_words(word1, word2):
    # 移除word1和word2中的所有空格
    word1 = re.sub(r'\s+', '', word1)
    word2 = re.sub(r'\s+', '', word2)
    #print('word1 = ', word1)
    #print('word2 = ', word2)

    # 判断最后一个字符是否是标点符号
    if word1[-1] in string.punctuation:
        # 去掉单词结尾的标点符号
        word1 = word1.rstrip(string.punctuation)
    # 判断第一个字符是否是标点符号
    if word1[0] in string.punctuation:
        # 去掉单词开头的标点符号
        word1 = word1.lstrip(string.punctuation)

    # 判断最后一个字符是否是标点符号
    if word2[-1] in string.punctuation:
        # 去掉单词结尾的标点符号
        word2 = word2.rstrip(string.punctuation)
    # 判断第一个字符是否是标点符号
    if word2[0] in string.punctuation:
        # 去掉单词开头的标点符号
        word2 = word2.lstrip(string.punctuation)

    #print('1--word1 = ', word1)
    #print('2--word2 = ', word2)

    # 如果word1和word2长度不同，则不是相同的单词
    if len(word1) != len(word2):
        return False

    #print('word1.lower = ', word1.lower())
    #print('word2.lower = ', word2.lower())

    # 如果word1和word2只有大小写和标点符号的区别，则将word2替换为word1
    if word1.lower() == word2.lower():
        return word1
    else:
        return False

# word = next(words_iter)
# for i in range(0, 10):
#     print('word ---> ',word)
#     word = next(words_iter)

with open('file1-1.srt', 'r') as f1, open('file3.srt', 'w') as f3:
    current_line = 1  # 当前行号
    current_time = ''  # 当前时间线
    words2 = next(words_iter) #读取docx的一段
    words2list = words2.split() #分解为单词列表
    while len(words2list) <= 2:
        words2 = next(words_iter) #读取docx的下一段
        words2list = words2.split() #分解为单词列表[]

    n2 = 0

    for line in f1:
        line = line.strip()
        # 数字行
        if line.isdigit():
            current_line = int(line)
            f3.write(line + '\n')
        # 只包含数字和标点的行
        elif all(char.isdigit() or char in '.,:-> ' for char in line):
            current_time = line
            f3.write(line + '\n')
        # 空行
        elif not line:
            f3.write(line + '\n')
        # 其他行
        else:
            words = line.split()
            n1 = len(words)
            for i in range(n1):
                #如果docx的上一段读完

                if n2 >= len(words2list):
                    words2 = next(words_iter) #读取docx的下一段
                    words2list = words2.split() #分解为单词列表
                    while len(words2list) <= 2:
                        words2 = next(words_iter) #读取docx的下一段
                        words2list = words2.split() #分解为单词列表[]
                    n2 = 0

                # 从file2中读取词
                try:
                    while words2 == '':
                        words2 = next(words_iter)
                        print('try2 word ---> ', words2)
                except StopIteration:
                    print('file2中的单词数量不足')
                    exit()
                # 如果词相同，继续读取下一个词
                words2list[n2] = words2list[n2].replace("’", "'")
                result = compare_words(words[i], words2list[n2])
                #print('result = ', result)
                if result != False:
                    words[i] = words2list[n2]
                    n2 = n2 + 1
                    continue
                else:
                    print('当前行号：', current_line)
                    print('当前时间线：', current_time)
                    print('srt --- docx：', words[i], ' --- ', words2list[n2])
                    exit()
                line = ''.join(words)
            f3.write(line + '\n')
    print('词对比完成，没有不同之处')
