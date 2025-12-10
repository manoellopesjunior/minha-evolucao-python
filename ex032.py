from datetime import date  # importando biblioteca para saber ano atual
a = int(input('Me diga um ano qualquer e direi se é bissexto ou não digite 0 para saber ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano {a} é bissexto')
else:
    print(f'O ano {a} não é bissexto')
