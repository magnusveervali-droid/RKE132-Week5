#Kirjuta programm, mis käib läbi iga tähe sõnes ja prindib selle välja.

text = "hello"

# for i in text: 
#     print(i)

#prindi sõn tahurpidi (viimasest tähemärgist esimese juurde, iga täht sõnast kuvatakse eraldi rale tagurpidi järjekorras). 

lenght = len(text)
print(lenght)

for letter in range(len(text) -1, -1, -1):
    print(text[letter])