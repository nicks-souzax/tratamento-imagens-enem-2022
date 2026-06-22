"""
Proposito: Dividir as questoes pela faixa divisoria (ENEM 2022 Digital).
Adaptado do codigo original de Alexandre Nassar de Peder.
"""

from PIL import Image
import os

# DESATIVAR O LIMITE DE TAMANHO DE IMAGEM DO PILLOW
Image.MAX_IMAGE_PIXELS = None

def encontrar_faixa_divisoria(imagem, cor_alvo=(128, 128, 128), tolerancia=60, altura_faixa=5):
    """
    Encontra posicoes onde ha uma faixa horizontal de separacao.
    Aumentamos a tolerancia para capturar tons de cinza/preto da Prova Digital.
    """
    largura, altura = imagem.size
    pixels = image_load = imagem.load()
    
    posicoes_corte = []
    
    y = 0
    while y < altura - altura_faixa:
        faixa_encontrada = True
        
        for dy in range(altura_faixa):
            # Verifica no centro da coluna
            pixel = pixels[largura // 2, y + dy]
            
            if len(pixel) == 4:  # RGBA
                r, g, b, a = pixel
            else:  # RGB
                r, g, b = pixel[:3]
            
            # Verifica proximidade com a cor alvo (Cinza) ou se e muito escura (Preto)
            if not ((abs(r - cor_alvo[0]) < tolerancia and 
                     abs(g - cor_alvo[1]) < tolerancia and 
                     abs(b - cor_alvo[2]) < tolerancia) or (r < 50 and g < 50 and b < 50)):
                faixa_encontrada = False
                break
        
        if faixa_encontrada:
            posicao_corte = y - 5
            if posicao_corte < 0:
                posicao_corte = 0
                
            posicoes_corte.append(posicao_corte)
            print(f"Faixa divisoria encontrada em y={y}, cortando em y={posicao_corte}")
            y += altura_faixa * 3  # Pula espaco para evitar dupla deteccao
        else:
            y += 1
    
    return posicoes_corte

def dividir_imagem_por_faixas(caminho_imagem, pasta_saida):
    if not os.path.exists(caminho_imagem):
        print(f"Erro: O arquivo de origem '{caminho_imagem}' nao foi encontrado!")
        return

    imagem = Image.open(caminho_imagem)
    largura, altura = imagem.size
    print(f"Imagem carregada: {largura}x{altura} pixels")
    
    posicoes_corte = encontrar_faixa_divisoria(imagem)
    
    if not posicoes_corte:
        print("Aviso: Nenhuma faixa divisoria encontrada com os parametros atuais.")
        print("Dica: Se nao cortar nada, sera necessario inspecionar a cor exata da linha.")
        return
    
    print(f"Encontradas {len(posicoes_corte)} faixas para corte")
    os.makedirs(pasta_saida, exist_ok=True)
    
    posicao_anterior = 0
    for i, posicao_corte in enumerate(posicoes_corte):
        if posicao_corte <= posicao_anterior:
            continue
            
        area_corte = (0, posicao_anterior, largura, posicao_corte)
        secao = imagem.crop(area_corte)
        
        nome_arquivo = f"parte_{i+1:03d}.png"
        caminho_completo = os.path.join(pasta_saida, nome_arquivo)
        secao.save(caminho_completo)
        print(f"Salvo: {caminho_completo} ({secao.width}x{secao.height}px)")
        
        posicao_anterior = posicao_corte + 5
    
    if posicao_anterior < altura:
        area_corte = (0, posicao_anterior, largura, altura)
        secao = imagem.crop(area_corte)
        nome_arquivo = f"parte_{len(posicoes_corte)+1:03d}.png"
        caminho_completo = os.path.join(pasta_saida, nome_arquivo)
        secao.save(caminho_completo)
        print(f"Salvo: {caminho_completo} ({secao.width}x{secao.height}px)")

if __name__ == "__main__":
    caminho_entrada = "6Passo-ConcatenarVerticalmente/colunas_concatenadas_verticalmente.png"
    pasta_destino = "7Passo-DividirPelaFaixaAzul/questoes_colunas"
    
    dividir_imagem_por_faixas(caminho_entrada, pasta_destino)
    print("Processo do Passo 7 concluido!")
