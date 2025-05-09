a = 'hoje-tem-aula-de-python!'
# print(f'o tamanho da minha string é {len(a)} caracteres')

txt1 = 'hj-e-uad-yhn'
txt2 = 'oetmal-epto!'

# print(txt1)
# print(txt2)

i = 0
txt = ''

while i < len(txt1):
    txt += txt1[i] + txt2[i]
    i += 1
print(txt)