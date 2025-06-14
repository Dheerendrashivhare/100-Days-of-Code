
def first_non_repating_char(string):
    for j in range(len(string)):
        string2 = string
        string2 = string2[:j] + string2[j+1:]
        if string[j] not in string2 :
            return string2[j]

    return None

print(first_non_repating_char("abababab"))