# Programa para verificar a velocidade e calcular a multa
velocidade = float(input("Qual é a velocidade do carro (em km/h)? "))

# Verificar se a velocidade ultrapassa 80 km/h
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 5
    print(f"Você foi multado! Excedeu o limite de velocidade em {excesso:.2f} km/h.")
    print(f"Valor da multa: €{multa:.2f}")
else:
    print("Velocidade dentro do limite permitido. Não há multa.")
    
    
#um comentário para alteração.   
 
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