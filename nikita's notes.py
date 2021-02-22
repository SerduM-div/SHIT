prokladka = str('привет')
for i in range(5):
    generated = generate(model, tok, prokladka, num_beams=10)
    prokladka = ' '.join(generated[0].split()[:7])
    print(generated[0])

    
    prokladka = str('привет')
for i in range(5):
    generated = generate(model, tok, prokladka, num_beams=10)
    prokladka = ' '.join(generated[0].split()[:15])
    print('1',prokladka)
    fulltext += ' '.join(generated[0].split())
    print('2',fulltext)
print('3',fulltext)



generated[0] = str('привет')
for i in range(5):
    generated = generate(model, tok, generated[0], num_beams=10)
    generated[0] = ' '.join(generated[0].split()[:7])
    print(generated[0])
