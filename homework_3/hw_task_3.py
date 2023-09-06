# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text = ''
with open('ekkleciast.txt', 'r') as file:
    for line in file:
        text += line

# удаляем незначащие символы:
unnecess_sym = ['.', ',', ':', ';', '—', '!', '?', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
for sym in text:
    if sym in unnecess_sym:
        text = text.replace(sym, '')

words_count = {}
for word in text.lower().split():
    if len(word) > 3:   # ищем слова длиннее 3 букв
        words_count.setdefault(word, 0)
        words_count[word] += 1

for i in sorted(list(words_count.values()), reverse=True)[:10]:
    for k, v in words_count.items():
        if v == i:
            print(k, v)
