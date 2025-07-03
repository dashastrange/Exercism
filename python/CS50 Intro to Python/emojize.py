import emoji

emoji_code = input()

if " " not in emoji_code or "_" in emoji_code:
    print(emoji.emojize(emoji_code, language='alias'))
else:
    print(emoji.emojize(emoji_code))

