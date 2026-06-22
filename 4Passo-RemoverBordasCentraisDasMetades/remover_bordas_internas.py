"""
Proposito: Remover a bordinha interna que fica entre as colunas (ENEM 2022 Digital).
Adaptado do codigo original de Alexandre Nassar de Peder
"""
from PIL import Image
import os

# Ajuste de caminhos relativos a partir da raiz do projeto
pasta_imagens = "3Passo-DividirAoMeioPaginasSemBordas/divididas-com-bordas-do-meio"
pasta_saida = "4Passo-RemoverBordasCentraisDasMetades/divididas-sem-bordas-do-meio"

os.makedirs(pasta_saida, exist_ok=True)

if not os.path.exists(pasta_imagens):
    print(f"Erro: A pasta de origem '{pasta_imagens}' nao foi encontrada!")
else:
    print("Iniciando a remocao das bordas centrais das metades...")
    for nome_arquivo in os.listdir(pasta_imagens):
        if nome_arquivo.lower().endswith(".png"):
            caminho_entrada = os.path.join(pasta_imagens, nome_arquivo)
            imagem = Image.open(caminho_entrada)
            
            largura, altura = imagem.size
            
            # Caixa de corte base (imagem inteira)
            caixa_corte = (0, 0, largura, altura)
            
            # Aplica cortes adicionais baseados na metade correspondente
            if nome_arquivo.endswith("_esquerda.png"):
                # Remove 25 pixels da borda direita
                caixa_corte = (caixa_corte[0], caixa_corte[1], 
                              caixa_corte[2] - 25, caixa_corte[3])
            
            elif nome_arquivo.endswith("_direita.png"):
                # Remove 25 pixels da borda esquerda
                caixa_corte = (caixa_corte[0] + 25, caixa_corte[1], 
                              caixa_corte[2], caixa_corte[3])
            
            imagem_cortada = imagem.crop(caixa_corte)
            
            caminho_saida = os.path.join(pasta_saida, nome_arquivo)
            imagem_cortada.save(caminho_saida)
            print(f"[OK] Borda central limpa: {nome_arquivo}")

    print("\nRecorte os das bordas centrais concluido com sucesso!")
