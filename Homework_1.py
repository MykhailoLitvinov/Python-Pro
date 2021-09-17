import re


def parse(query: str) -> dict:
    if '?' in query:
        query = query.split('?')
        words = re.split('[=&]', query[1])
        if words[-1] == '':
            words.pop()
        return {words[i]: words[i + 1] for i in range(0, len(words), 2)}
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


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
