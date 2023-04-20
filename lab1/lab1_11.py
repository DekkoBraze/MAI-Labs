# -*- coding: utf-8-*-
s = "В худой котомк поклав ржаное хлебо, Я ухожу туда, где птичья звон. И вижу над собою синий небо, Косматый облак и высокий крон. Я дома здесь. Я здесь пришел не в гости. Снимаю кепк, одетый набекрень. Веселый птичк, помахивая хвостик, Высвистывает мой стихотворень. Зеленый травк ложится под ногами, И сам к бумаге тянется рука. И я шепчу дрожащие губами: «Велик могучим русский языка!»"
s = s.replace(',', '')
s = s.replace('.', '')
s = s.replace('!', '')
s = s.split(' ')
lst = []
g_lst = ["а", "о", "у", "ы", "э", "е", "ё", "и", "ю", "я"]
g_lst_cap = []
for i in g_lst:
    formated_i = i.capitalize()
    g_lst_cap.append(formated_i)
g_lst = g_lst + g_lst_cap
def count_g(word):
    count = 0
    for let in word:
        if let in g_lst:
            count += 1
    return count
for i in s:
    tpl = (i, len(i), count_g(i))
    lst.append(tpl)
for i in lst:
    print(i)