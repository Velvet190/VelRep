notes = {
    "Alice": 15,
    "Bob": 8,
    "Charlie": 17,
    "David": 11
}

def analyser_notes(notes):
    res = 0
    i = 0
    max = 0
    min = 20
    for note in notes.values():
        res += note
        if max < note:
            max = note
        if min > note:
            min = note
        i += 1
    moyenne = res/i
    return(moyenne, max, min)

moyenne, meilleure, pire = analyser_notes(notes)

print(moyenne)
print(meilleure)
print(pire)