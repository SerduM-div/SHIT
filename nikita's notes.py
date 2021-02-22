prokladka = str('привет')
for i in range(5):
    generated = generate(model, tok, prokladka, num_beams=10)
    prokladka = ' '.join(generated[0].split()[:7])
    print(generated[0])
