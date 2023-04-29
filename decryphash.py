import hashlib
import itertools

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
checksum = "{YOUR HASH FOR DECRYPT}"

for tamanho in range(1, 10):
    for comb in itertools.product(caracteres, repeat=tamanho): #Gera todas as combinações possíveis de caracteres de acordo com o tamanho
        senha = ''.join(comb) #Tranforma em uma única string fazendo a senha
        hash_md5 = hashlib.md5() 
        hash_md5.update(senha.encode('utf-8')) #Atualiza o Hash com a senha codificada em UTF-8
        hash_md5_senha = hash_md5.hexdigest() #Gera o valor de hash da senha
        if hash_md5_senha == checksum: #Compara ao Checksum
            print(f"Senha encontrada: {senha}")
            break





                            
