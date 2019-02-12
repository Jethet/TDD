def get_middle(word):
    if len(word) % 2 == 1:
        mid = round(len(word)/2)
        return word[mid]

    else: #len(word) % 2 == 0:
        mid = round(len(word)/2)
        return word[mid-1] + word[mid]

print(get_middle("test")) #➞ "es"
print(get_middle("testing")) #➞ "t"
print(get_middle("incredibility"))
print(get_middle("focus"))
print(get_middle("lav4box"))
