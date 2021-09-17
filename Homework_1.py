import re


def parse(query: str) -> dict:
    if '?' in query:
        query = query.split('?')
        words = re.split('[=&]', query[1])
        if words[-1] == '':
            words.pop()
        return {words[i]: words[i + 1] for i in range(0, len(words), 2)}
    else:
        return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

