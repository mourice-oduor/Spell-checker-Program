# mistakes_list = {'speling':'spelling', 'writen':'written','Morrsi':'Morris'}

# text_first = 'Hi Morrsi, could you please read what I have writen and check the speling'
# text_first = text_first.replace(',', '')
# print(text_first)
# text = text_first.split()
# print(text)

# for each_item_in_text in text:
#     for each_mistake_item in mistakes_list:
#         if each_item_in_text == each_mistake_item:
#             print(each_item_in_text) 

my_dict = {'speling':'spelling', 'writen':'written','Morrsi':'Morris'}

text_first = 'Hi Morrsi, could you please read what I have writen and check the speling'
text_first = text_first.replace(',', '')
text = text_first.split()

final_string = ' '.join(str(my_dict.get(word, word)) for word in text)

print(final_string)
