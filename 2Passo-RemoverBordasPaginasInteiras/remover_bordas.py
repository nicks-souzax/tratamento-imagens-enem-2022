"""
Proposito: remover as bordas externas das paginas do ENEM 2022 Digital
Adaptado do codigo original de Alexandre Nassar de Peder
"""

from PIL import Image
import os

# Caminhos relativos corretos a partir da raiz do projeto
pasta_imagens = "1Passo-ConvertePDF2PNG/imagens"
pasta_saida = "2Passo-RemoverBordasPaginasInteiras/sem-bordas-externas"

os.makedirs(pasta_saida, exist_ok=True)

if not os.path.exists(pasta_imagens):
    print(f"Erro: A pasta de origem '{pasta_imagens}' nao foi encontrada!")
else:
    print("Iniciando o corte das bordas externas...")
    for nome_arquivo in os.listdir(pasta_imagens):
        if nome_arquivo.lower().endswith(".png"):
            caminho_entrada = os.path.join(pasta_imagens, nome_arquivo)
            imagem = Image.open(caminho_entrada)

            largura, altura = imagem.size

            # Mantendo a medicao original de contagem de pixels
            caixa_corte = (276, 390, largura - 276, altura - 280)
            imagem_cortada = imagem.crop(caixa_corte)

            caminho_saida = os.path.join(pasta_saida, nome_arquivo)
            imagem_cortada.save(caminho_saida)
            print(f"[OK] Bordas removidas: {nome_arquivo}")

    print("\nRecorte das bordas concluido com sucesso!")
