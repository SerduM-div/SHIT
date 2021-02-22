generated[0] = str('привет')
for i in range(15):
    generated = generate(model, tok, generated[0], num_beams=10)
    fulltext = ' '.join(generated[0].split())
    generated[0] = ' '.join(generated[0].split()[-15:])
    print('1',fulltext)

print('2',generated[0])


print(fulltext)
