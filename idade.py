# Solicita que o usuário digite o ano de nascimento
ano = int(input("Digite o ano de nascimento: "))
# Calcula a idade subtraindo o ano de nascimento do ano atual (2024, neste caso)
idade = 2024 - ano

# Exibe a idade calculada ao usuário
print("A sua idade é:", idade)

# Verifica a faixa etária do usuário com base na idade calculada
# Verifica a faixa etária e imprime a mensagem correspondente
if idade >= 65:
    print("És um sénior")
    # Caso contrário, se a idade for maior ou igual a 18 e menor que 65, exibe 'adulto'
elif idade >= 18:
    print("És um adulto")
else:
    print("És uma criança")

# Se a idade for menor que 18, exibe a mensagem de 'criança'

''' git diff: Mostra as diferenças entre arquivos alterados mas ainda não "stageados" ou entre commits.
git commit: Salva as mudanças do staged area no repositório local com uma mensagem explicando as alterações.
git merge: Combina alterações de uma branch com outra.
git log: Exibe o histórico de commits.
Outros comandos úteis:

git add: Adiciona alterações ao staged area para serem commitadas.
git checkout: Muda de branch ou restaura arquivos.
git branch: Gerencia branches (criar, listar, deletar).
git push: Envia commits do repositório local para o remoto.
git pull: Atualiza o repositório local com mudanças do repositório remoto.
git clone: Clona um repositório remoto para o local.
Esses comandos são essenciais para o fluxo de trabalho no Git.'''
