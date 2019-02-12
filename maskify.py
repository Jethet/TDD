def maskify(txt):
    if len(txt) == 0:
        return txt
    if len(txt) < 4:
        return txt
    if len(txt) >= 4:
        new_txt1 = txt[0:-4]
        new_txt2 = txt[-4::]
        return ('#' * len(new_txt1)) + new_txt2


print(maskify("4556364607935616")) # "############5616"
print(maskify("64607935616")) # "#######5616"
print(maskify("1")) # "1"
print(maskify("")) # ""
