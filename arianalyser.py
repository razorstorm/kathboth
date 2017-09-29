fh = open("ari_parsed_text.txt", "r")
contents = fh.readlines()

total_lengths = 0
for content in contents:
    content = content.lstrip().rstrip()
    total_lengths += len(content)

print total_lengths / len(contents)
