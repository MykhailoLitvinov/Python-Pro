import re


def parse(query: str) -> dict:
    if '?' in query:
        query = query.split('?')
        words = re.split('[=&]', query[1])
        if words[-1] == '':
            words.pop()
        for word in words:
            if word.isdigit():
                index = words.index(word)
                words.pop(index)
                words.insert(index, int(word))
        return {words[i]: words[i + 1] for i in range(0, len(words), 2)}
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('https://example.com/path/to/page?name=ferret&color=purple&age=18') == {'name': 'ferret', 'color': 'purple', 'age': 18}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&age=18') != {'name': 'ferret', 'color': 'purple', 'age': '18'}
    assert type(parse('https://example.com/path/to/page?name=ferret&color=purple&age=18')) != int
    assert type(parse('https://example.com/path/to/page?name=ferret&color=purple&age=18')) == dict


def parse_cookie(query: str) -> dict:
    if query:
        words = query.split(';')
        words_1 = words[0].split('=', 1)
        words_2 = words[1].split('=')
        words_1.extend(words_2)
        if '' in words_1:
            words_1.pop()
        return {words_1[i]: words_1[i + 1] for i in range(0, len(words_1), 2)}
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    # assert parse_cookie('name=Dima;age=28;lastName=Kaminskyi') == {'name': 'Dima', 'age': '28', 'lastName': 'Kaminskyi'}


query = 'name=Dima;age=28'
words = query.split(';')
splited_words = []
for _ in words:
    if _.count('=') > 1:
        new_list_1 = _.split('=', 1)
        for _ in new_list_1:
            splited_words.append(_)
    else:
        new_list_2 = _.split('=')
        for _ in new_list_2:
            splited_words.append(_)
    if '' in splited_words:
        splited_words.pop()
my_dict = {splited_words[i]: splited_words[i + 1] for i in range(0, len(splited_words), 2)}
print(my_dict)

def parse_cookie_1(query: str) -> dict:
    if query:
        words = query.split(';')
        split_words = []
        for _ in words:
            if _.count('=') > 1:
                new_list_1 = _.split('=', 1)
                for _ in new_list_1:
                    split_words.append(_)
            else:
                new_list_2 = _.split('=')
                for _ in new_list_2:
                    split_words.append(_)
            if '' in split_words:
                split_words.pop()
        return {split_words[i]: split_words[i + 1] for i in range(0, len(split_words), 2)}
    return {}

if __name__ == '__main__':
    assert parse_cookie_1('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie_1('') == {}
    assert parse_cookie_1('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie_1('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie_1('name=Dima;age=28;lastName=Kaminskyi') == {'name': 'Dima', 'age': '28', 'lastName': 'Kaminskyi'}

# print(parse_cookie_1('name=Dima;age=28;'))

