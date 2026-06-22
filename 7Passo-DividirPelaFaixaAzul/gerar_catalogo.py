
import os
from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = None

pasta_imagens = "7Passo-DividirPelaFaixaAzul/questoes_colunas"
arquivo_saida = "7Passo-DividirPelaFaixaAzul/catalogo_inspecao.png"

if not os.path.exists(pasta_imagens):
    print("Erro: Pasta nao encontrada.")
else:
    arquivos = [f for f in os.listdir(pasta_imagens) if f.endswith(".png")]
    arquivos.sort()
    
    print(f"Montando catalogo para {len(arquivos)} imagens...")
    colunas = 5
    linhas = (len(arquivos) + colunas - 1) // colunas
    largura_bloco = 300
    altura_bloco = 600
    
    imagem_catalogo = Image.new("RGB", (colunas * largura_bloco, linhas * altura_bloco), (240, 240, 240))
    draw = ImageDraw.Draw(imagem_catalogo)
    
    for idx, arquivo in enumerate(arquivos):
        caminho = os.path.join(pasta_imagens, arquivo)
        try:
            img = Image.open(caminho)
            img.thumbnail((largura_bloco - 20, altura_bloco - 60))
            l = idx // colunas
            c = idx % colunas
            x = c * largura_bloco + 10
            y = l * altura_bloco + 40
            imagem_catalogo.paste(img, (x, y))
            draw.rectangle([c * largura_bloco, l * altura_bloco, (c + 1) * largura_bloco, (l + 1) * altura_bloco], outline=(200, 200, 200))
        except Exception as e:
            pass

    imagem_catalogo.save(arquivo_saida)
    print(f"Catalogo gerado com sucesso! Abra o arquivo: {arquivo_saida}")
