text = "0"

try:
    with open('test.txt','r') as f:
        text = f.read()
    n = int(text[text.rfind('\n')+1:])+1
    text += '\n'
    text += str(n)
except:
    pass

with open('test.txt','w') as f:
    f.write(text)
