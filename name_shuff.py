def name_shuffle(txt):
    txt = txt.split()
    new_text = txt[::-1]
    return ' '.join(new_text)

print(name_shuffle("Rosie O'Donnell")) # "O'Donnell Rosie"
print(name_shuffle("Seymour Butts")) # "Butts Seymour"
