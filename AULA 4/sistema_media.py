# sistema escola
alunos = []
medias  = []
pergunta  =  input('Deseja acessar?').lower()
while pergunta == 'sim':
    
    for i in range(3):
        senha =  input('SENHA: ')
        if senha  == '123':
               print('SISTEMA DE NOTAS..')
               
               nome =  input('Aluno: ')
               nota1 = float(input('Nota Matematica: '))
               nota2 = float(input('Nota Portugues: '))
               nota3 = float(input('Nota ingles: '))
               media =  (nota1+nota2+nota3) / 3
               print('Média', media, 'Aluno(a):', nome)
               alunos.append(nome)
               medias.append(media)
               pergunta  =  input('Deseja continua?')
               if pergunta != 'sim':
                   print('***' * 8)
                   print('Lista de alunos')
                   print(alunos)
                   print('MÉDIAS')
                   print(medias)
                   print('***' * 8)
                   print('MÉDIA DA SALA: ', sum(medias)/len(medias))
                   print('***' * 8)
                   pergunta  =  input('Deseja continua?')
                   
           
        else:
            print('Senha incorreta')    
    else:
        print('Senha bloqueada')
        break      
    
else:
    print('Até logo ... ')

