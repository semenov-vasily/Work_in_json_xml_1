import json
import xml.etree.ElementTree as ET

def read_xml(file_path, word_max_len=6, top_words_amt=10):
        parser = ET.XMLParser(encoding = 'utf-8')
        tree = ET.parse(file_path, parser)
        root = tree.getroot()
        news_list = root.findall('channel/item/description')
        all_words = []
        list_description = []
        for news in news_list:
                all_words.extend(news.text.split())
        i_description = [s for s in all_words if len(s) > word_max_len]
        list_description.extend(i_description)
        set_description = list(set(list_description))
        words_counted = sorted([[n, list_description.count(n)] for n in set_description], key=lambda x: x[1], reverse=True)
        result = [i[0] for i in words_counted[:top_words_amt]]
        return result

#
if __name__ == '__main__':
    print(read_xml('newsafr.xml'))



def read_json(file_path, word_max_len=6, top_words_amt=10):
    with open('newsafr.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        b = data['rss']["channel"]["items"]
        list_description = []
        for i in b:
            i_description = [s for s in i["description"].split() if len(s) > word_max_len]
            list_description.extend(i_description)
    set_description = set(list_description)
    list_set_description = list(set_description)
    words_counted = sorted([[n, list_description.count(n)] for n in list_set_description], key=lambda x: x[1], reverse=True)
    result = [i[0] for i in words_counted[:top_words_amt]]
    return result

if __name__ == '__main__':
    print(read_json('newsafr.json'))



#         json_data = json.load(f)
#         # print(json_data)
#         dict_news = json_data["rss"]["channel"]["items"]
#         # print(dict_news)
#         text_news = []
#         for new in dict_news:
#                 new_1 = new["description"].split(" ")
#                 # print(new_1)
#                 for n in new_1:
#                         # print(n)
#                         if len(n) > word_max_len:
#                                 text_news.append(n)
#         # print(text_news)
#
# unique_word = set(text_news)
# d = {}
# for i in unique_word:
#         for m in text_news:
#                 if i == m:
#                         d.setdefault(i, 0)
#                                 # print(d)
#                         d[i] += 1
# print(d)
# d = list(dict(sorted(d.items(), key=lambda x: x[1])))
# print(d)
# c = d[::-1]
# print(c)
# res = [a for a in c][:top_words_amt]
# print(res)
# return res
#
# if __name__ == '__main__':
#         print(read_xml('newsafr.json'))
