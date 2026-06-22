"""
Proposito: Cortar as imagens de colunas ao meio (ENEM 2022 Digital).
Adaptado do codigo original de Alexandre Nassar de Peder
"""

from PIL import Image
import os

# Ajuste de caminhos relativos a partir da raiz do projeto
pasta_imagens = "2Passo-RemoverBordasPaginasInteiras/sem-bordas-externas"
pasta_saida = "3Passo-DividirAoMeioPaginasSemBordas/divididas-com-bordas-do-meio"

os.makedirs(pasta_saida, exist_ok=True)

if not os.path.exists(pasta_imagens):
    print(f"Erro: A pasta de origem '{pasta_imagens}' nao foi encontrada!")
else:
    print("Iniciando a divisao das imagens ao meio verticalmente...")
    for nome_arquivo in os.listdir(pasta_imagens):
        if nome_arquivo.lower().endswith('.png'):
            caminho_entrada = os.path.join(pasta_imagens, nome_arquivo)
            imagem = Image.open(caminho_entrada)

            largura, altura = imagem.size
            metade_largura = largura // 2
            
            # Recorte da metade esquerda
            caixa_esquerda = (0, 0, metade_largura, altura)
            imagem_esquerda = imagem.crop(caixa_esquerda)
            
            # Recorte da metade direita
            caixa_direita = (metade_largura, 0, largura, altura)
            imagem_direita = imagem.crop(caixa_direita)
            
            nome_base, extensao = os.path.splitext(nome_arquivo)
            
            caminho_esquerda = os.path.join(pasta_saida, f"{nome_base}_esquerda{extensao}")
            caminho_direita = os.path.join(pasta_saida, f"{nome_base}_direita{extensao}")
            
            imagem_esquerda.save(caminho_esquerda)
            imagem_direita.save(caminho_direita)
            print(f"[OK] Dividida ao meio: {nome_arquivo} (Esquerda/Direita)")

    print("\nDivisao das imagens ao meio concluida com sucesso!")
