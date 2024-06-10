def verificar_credenciais(usuario_input, senha_input):
    usuario_correto = "Igor"
    senha_correta = "senha secreta"
    
    if usuario_input == usuario_correto and senha_input == senha_correta:
        return "Acesso concedido! Bem-vindo, Igor!"
    else:
        return "Erro: nome de usuário ou senha incorretos."

def solicitar_credenciais():
    while True:
        # Solicita o nome de usuário e a senha do usuário
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        
        # Verifica as credenciais e exibe a mensagem apropriada
        mensagem = verificar_credenciais(usuario, senha)
        print(mensagem)
        
        # Se a mensagem for de sucesso, sai do loop
        if mensagem == "Acesso concedido! Bem-vindo, Igor!":
            break

def formulario_compra():
    print("Formulário de Compra")
    nome_produto = input("Nome do produto: ")
    quantidade = input("Quantidade: ")
    endereco_entrega = input("Endereço de entrega: ")
    
    print("\nResumo da Compra:")
    print(f"Produto: {nome_produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Endereço de Entrega: {endereco_entrega}")
    print("Sua solicitação de compra foi realizada com sucesso!")

# Chama a função para iniciar o processo de solicitação de credenciais
solicitar_credenciais()

# Após o acesso ser concedido, permite que o usuário preencha o formulário de compra
formulario_compra()



