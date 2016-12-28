f = open("index.md", "r")
contents = []

for line in f:
    if '# Article' in line:
        line = line + '{:.no_toc}\n'
    contents.append(line)
f.close()
f = open("index-new.md", "w")
f.writelines(contents)
f.close()