
import os
from pypdf import PdfReader

pdf_path = "1Passo-ConvertePDF2PNG/prova_2022.pdf"

if not os.path.exists(pdf_path):
    print(f"Erro: O arquivo {pdf_path} nao foi encontrado!")
else:
    print("🔄 Analisando o PDF da prova de 2022 para mapear as questoes...\n")
    reader = PdfReader(pdf_path)
    
    mapa_questoes = {}
    
    # Varre cada pagina do PDF (comecando da 1)
    for num_pag, pagina in enumerate(reader.pages, start=1):
        texto = pagina.extract_text()
        if not texto:
            continue
            
        # Procura por padroes de QUESTÃO de 91 a 180
        for q in range(91, 181):
            termo = f"QUESTÃO {q}"
            if termo in texto or termo.lower() in texto.lower():
                if q not in mapa_questoes:
                    mapa_questoes[q] = []
                mapa_questoes[q].append(num_pag)

    # Exibe o resultado de forma organizada
    if not mapa_questoes:
        print("Aviso: Nenhuma questao foi encontrada por texto direto no PDF.")
        print("Isso pode significar que as paginas do PDF sao apenas imagens escaneadas.")
    else:
        print("🗺️ MAPA DE QUESTÕES ENCONTRADO:")
        for q in sorted(mapa_questoes.keys()):
            paginas_str = ", ".join(map(str, mapa_questoes[q]))
            print(f"Questao {q} -> Encontrada na(s) pagina(s) do PDF: {paginas_str}")
