"""
Proposito: Concatenar verticalmente as imagens de colunas do Passo 5 (ENEM 2022 Digital).
Adaptado do codigo original de Alexandre Nassar de Peder
"""

from PIL import Image
import os
import re

# Ajuste de caminhos relativos a partir da raiz do projeto
pasta_imagens = "5Passo-OrganizarImagensColunasEInteiras/divididas-sem-bordas-do-meio"
pasta_saida = "6Passo-ConcatenarVerticalmente"

os.makedirs(pasta_saida, exist_ok=True)

# Funcao para extrair o numero da pagina e ordenar corretamente
def get_sort_key(nome_arquivo):
    # Extrai o numero da pagina
    numero = int(re.search(r'pagina_enem_(\d+)_', nome_arquivo).group(1))
    # Define a ordem: esquerda primeiro (0), depois direita (1)
    lado = 0 if 'esquerda' in nome_arquivo else 1
    return (numero, lado)

if not os.path.exists(pasta_imagens):
    print(f"Erro: A pasta de origem '{pasta_imagens}' nao foi encontrada!")
else:
    print("Coletando e ordenando as imagens do Passo 5...")
    arquivos = [f for f in os.listdir(pasta_imagens) if f.endswith('.png')]
    arquivos.sort(key=get_sort_key)

    if not arquivos:
        print("Aviso: Nenhuma imagem encontrada na pasta de origem.")
    else:
        imagens = []
        for arquivo in arquivos:
            caminho = os.path.join(pasta_imagens, arquivo)
            imagens.append(Image.open(caminho))
            print(f"Adicionando a pilha: {arquivo}")

        # Encontrar a largura maxima
        largura_max = max(img.width for img in imagens)

        # Concatenar verticalmente
        print("\nGerando a imagem vertical unificada (isto pode levar alguns segundos)...")
        altura_total = sum(img.height for img in imagens)
        imagem_final = Image.new('RGB', (largura_max, altura_total))

        y = 0
        for img in imagens:
            imagem_final.paste(img, (0, y))
            y += img.height

        # Salvar o resultado final na pasta do Passo 6
        caminho_salvamento = os.path.join(pasta_saida, 'colunas_concatenadas_verticalmente.png')
        imagem_final.save(caminho_salvamento)
        print("\nImagens concatenadas na ordem correta com sucesso!")
        print(f"Arquivo gerado em: {caminho_salvamento}")
