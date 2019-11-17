import error_raw_data
import constant
# data = json.loads("error_raw_data.txt")
words = {}
for comment in error_raw_data.error_raw_data:
    for stop_word in constant.ori_stopwords:
        if stop_word in comment:
            if stop_word in words:
                words[stop_word] += 1
            else:
                words[stop_word] = 1
print(words)
