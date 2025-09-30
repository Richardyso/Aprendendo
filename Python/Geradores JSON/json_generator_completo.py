import json
import re

def normalizar_categoria(nome_categoria):
    """Converte nome da categoria para snake_case"""
    # Remove acentos
    nome = nome_categoria.lower()
    nome = re.sub(r'[àáâãä]', 'a', nome)
    nome = re.sub(r'[èéêë]', 'e', nome)
    nome = re.sub(r'[ìíîï]', 'i', nome)
    nome = re.sub(r'[òóôõö]', 'o', nome)
    nome = re.sub(r'[ùúûü]', 'u', nome)
    nome = re.sub(r'[ç]', 'c', nome)
    # Substitui espaços e caracteres especiais por underscore
    nome = re.sub(r'[^a-z0-9]', '_', nome)
    # Remove underscores duplos
    nome = re.sub(r'_+', '_', nome)
    # Remove underscores no início e fim
    nome = nome.strip('_')
    return nome

def obter_booleano(pergunta):
    """Obtém resposta booleana do usuário"""
    while True:
        resposta = input(f"{pergunta} (s/n): ").lower().strip()
        if resposta in ['s', 'sim', 'y', 'yes']:
            return True
        elif resposta in ['n', 'não', 'nao', 'no']:
            return False
        else:
            print("Por favor, digite 's' para sim ou 'n' para não.")

def obter_preco():
    """Obtém preço formatado do usuário"""
    while True:
        try:
            preco = input("Preço (apenas números, ex: 19.90): R$ ")
            # Tenta converter para float para validar
            float(preco.replace(',', '.'))
            # Retorna formatado
            return f"R$ {preco}"
        except ValueError:
            print("Por favor, digite um preço válido (ex: 19.90)")

def obter_quantidade():
    """Obtém quantidade como número inteiro"""
    while True:
        try:
            quantidade = int(input("Quantidade: "))
            return quantidade
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def main():
    print("=== GERADOR DE CATÁLOGO DE PRODUTOS ===\n")
    
    catalogo = {}
    
    while True:
        # Obter nome da categoria
        nome_categoria = input("Nome da categoria: ").strip()
        if not nome_categoria:
            print("Nome da categoria não pode estar vazio!")
            continue
        
        categoria_key = normalizar_categoria(nome_categoria)
        catalogo[categoria_key] = []
        
        print(f"\n--- Adicionando produtos para a categoria '{categoria_key}' ---")
        
        contador_produto = 1
        
        while True:
            print(f"\n>> Produto {contador_produto} da categoria '{categoria_key}':")
            
            # Gerar ID do produto
            produto_id = f"{categoria_key.upper()}_{contador_produto:02d}"
            
            # Obter dados do produto
            nome = input("Nome do produto: ").strip()
            if not nome:
                print("Nome do produto não pode estar vazio!")
                continue
            
            descricao = input("Descrição: ").strip()
            preco = obter_preco()
            imagem = input("URL da imagem: ").strip()
            quantidade = obter_quantidade()
            disponivel = obter_booleano("Produto disponível?")
            
            # Criar produto
            produto = {
                "id": produto_id,
                "nome": nome,
                "descricao": descricao,
                "preco": preco,
                "imagem": imagem,
                "quantidade": quantidade,
                "disponivel": disponivel
            }
            
            catalogo[categoria_key].append(produto)
            contador_produto += 1
            
            # Perguntar se quer adicionar mais produtos nesta categoria
            if not obter_booleano("Adicionar mais um produto nesta categoria?"):
                break
        
        # Perguntar se quer adicionar mais categorias
        if not obter_booleano("Adicionar mais uma categoria?"):
            break
    
    # Salvar arquivo JSON
    nome_arquivo = input("\nNome do arquivo (sem extensão): ").strip()
    if not nome_arquivo:
        nome_arquivo = "catalogo_produtos"
    
    nome_arquivo += ".json"
    
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(catalogo, arquivo, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Arquivo '{nome_arquivo}' criado com sucesso!")
        print(f"Total de categorias: {len(catalogo)}")
        
        # Mostrar resumo
        for categoria, produtos in catalogo.items():
            print(f"  - {categoria}: {len(produtos)} produto(s)")
            
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo: {e}")

if __name__ == "__main__":
    main()