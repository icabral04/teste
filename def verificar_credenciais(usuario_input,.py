def verificar_credenciais(usuario_input, senha_input):
    usuario_correto = "Igor"
    senha_correta = "senha secreta"
    
    if usuario_input == usuario_correto and senha_input == senha_correta:
        return "Acesso concedido! Bem-vindo, Igor!"
    else:
        return "Erro: nome de usuário ou senha incorretos."

def solicitar_credenciais():
    tentativas = 3
    while tentativas > 0:
        # Solicita o nome de usuário e a senha do usuário
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        
        # Verifica as credenciais e exibe a mensagem apropriada
        mensagem = verificar_credenciais(usuario, senha)
        print(mensagem)
        
        # Se a mensagem for de sucesso, sai do loop
        if mensagem == "Acesso concedido! Bem-vindo, Igor!":
            return True
        else:
            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}")
    
    return False

def adicionar_produto_ao_carrinho(carrinho):
    while True:
        nome_produto = input("Nome do produto: ")
        quantidade = input("Quantidade: ")
        endereco_entrega = input("Endereço de entrega: ")
        
        if nome_produto and quantidade.isdigit() and endereco_entrega:
            carrinho.append({
                "produto": nome_produto,
                "quantidade": int(quantidade),
                "endereco": endereco_entrega
            })
            break
        else:
            print("Entrada inválida. Por favor, preencha todos os campos corretamente.")

def exibir_resumo_carrinho(carrinho):
    print("\nResumo do Pedido:")
    for item in carrinho:
        print(f"Produto: {item['produto']}\nQuantidade: {item['quantidade']}\nEndereço de Entrega: {item['endereco']}\n")
    print("Sua solicitação de compra foi realizada com sucesso!")

def formulario_compra():
    carrinho = []
    while True:
        adicionar_produto_ao_carrinho(carrinho)
        continuar = input("Deseja adicionar mais um produto? (s/n): ").lower()
        if continuar != 's':
            break
    exibir_resumo_carrinho(carrinho)

# Chama a função para iniciar o processo de solicitação de credenciais
if solicitar_credenciais():
    # Após o acesso ser concedido, permite que o usuário preencha o formulário de compra
    formulario_compra()
else:
    print("Número máximo de tentativas excedido. Acesso bloqueado.")
