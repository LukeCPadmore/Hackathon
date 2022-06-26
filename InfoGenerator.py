text = ""
f = open("VideoInfo.txt","r")
for line in f:
    final = ""
    for i in range(0,len(line)):
        if line[i]=="\'" or line[i] == "\"" or line[i] == "\\":
            final += "\\"
        final += line[i]
    text += "\\n" + final[0:len(final) - 1]
print(text)
