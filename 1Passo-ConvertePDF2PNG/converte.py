import os
from pdf2image import convert_from_path

# Caminhos de origem e destino
pdf_path = os.path.join("1Passo-ConvertePDF2PNG", "prova_2022.pdf")
output_dir = os.path.join("1Passo-ConvertePDF2PNG", "imagens")

# Garante que a pasta de destino das imagens exista
os.makedirs(output_dir, exist_ok=True)

print("?? Iniciando a conversao do PDF para PNG (isto pode levar alguns segundos)...")

try:
    # Converte as paginas do PDF em formato de imagem (ajuste o path do poppler se necessario)
    paginas = convert_from_path(pdf_path, dpi=200)
    
    for i, pagina in enumerate(paginas):
        # Garante a nomenclatura correta das paginas (ex: pagina_enem_01.png)
        nome_imagem = f"pagina_enem_{i+1:02d}.png"
        caminho_salvamento = os.path.join(output_dir, nome_imagem)
        pagina.save(caminho_salvamento, "PNG")
        print(f"[OK] Convertida: {nome_imagem}")
        
    print("\n? PDF convertido com sucesso completo!")

except Exception as e:
    print(f"\n? Erro durante a conversao: {e}")
    print("Dica: Se der erro de Poppler, lembre-se de configurar o caminho dos binarios!")
