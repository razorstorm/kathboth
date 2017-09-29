fh = open("ariseed2.txt", "r")
contents = fh.readlines()

ari_turn = False
outputs = []
for content in contents:
    content = content.lstrip().rstrip()
    if content == "Ari Falkner":
        ari_turn = True
    elif content == "Jason":
        ari_turn = False
    elif ari_turn:
        outputs.append(content)

for output in outputs:
    print output
