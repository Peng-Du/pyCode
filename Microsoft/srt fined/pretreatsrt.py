import pandas as pd

# 读取替代词典
replacedict = {}
df = pd.read_excel('replacedict.xlsx', sheet_name='Sheet1')
for index, row in df.iterrows():
    old_word = str(row[0]).strip()
    new_word = str(row[1]).strip()
    if old_word != '' and new_word != '':
        replacedict[old_word] = new_word

# 读取srt文件并替换词语
with open('file1.srt', 'r', encoding='utf-8') as f:
    content = f.read()

for old_word,new_word in replacedict.items():
    content = content.replace(old_word, new_word)

# 将替换后的内容输出为新的srt文件
with open('file1-1.srt', 'w', encoding='utf-8') as f:
    f.write(content)
