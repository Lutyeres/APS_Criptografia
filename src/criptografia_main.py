def criptografar (frase):
    resultado = ''
    for i in frase:
        char = i
        resultado += chr(ord(char) + 5)
    return resultado

def descriptar (frase):
    resultado = ''
    for i in frase:
        char = i
        resultado += chr(ord(char) - 5)
    return resultado

escolha = input('Digite C para criptografar ou D para Descriptografar: ')

if escolha.upper() == 'C':
    mensagem = input('Escreva a mensagem que você quer criptografar: ')
    mensagemCrip = criptografar(mensagem)
    
    with open('mensagem_criptografada.txt', 'w', encoding = 'utf-8') as arquivo_criptografado:
        arquivo_criptografado.write(mensagemCrip)
        print('A mensagem foi criptografada no arquivo mensagem_criptografada.txt')

elif escolha.upper() == 'D':
    with open('mensagem_criptografada.txt', 'r', encoding = 'utf-8') as arquivo_criptografado:
        mensagemCrip = arquivo_criptografado.read()
        mensagemDescrip = descriptar(mensagemCrip)
    with open('mensagem_descriptografada.txt', 'w', encoding = 'utf-8') as arquivo_descriptografado:
        arquivo_descriptografado.write(mensagemDescrip)
        print('A mensagem foi descriptografada no arquivo mensagem_descriptografada.txt')

else:
    print('Opção invalida, por favor escolha uma opção existente!')
    
