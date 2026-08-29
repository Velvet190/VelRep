notes = {
    "Alice": 15,
    "Bob": 8,
    "Charlie": 17,
    "David": 11
}
i = 0
res = 0

#for note in notes:
#    if notes[note] > 10:
#        print(note, ":", notes[note])

for nom, note in notes.items():
    res += note
    i += 1
print(res/i)