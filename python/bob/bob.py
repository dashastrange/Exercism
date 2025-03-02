def response(hey_bob):

    length = len(hey_bob)
    strip_bob = hey_bob.strip()

    if strip_bob.endswith('?') and strip_bob.isupper() == False:
        return str('Sure.')
    elif strip_bob.isupper() and strip_bob.endswith('?'):
        return str("Calm down, I know what I'm doing!")
    elif len(strip_bob) == 0:
        return str('Fine. Be that way!')
    elif strip_bob.isupper() and strip_bob.endswith('?') == False:
        return str('Whoa, chill out!')
    else:
        return str('Whatever.')
