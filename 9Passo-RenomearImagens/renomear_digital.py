import os
import shutil

# Caminho da pasta do Passo 8 (de onde vamos ler as imagens organizadas)
CAMINHO_PASSO8 = "../8Passo-OrganizarIntervalosQuestoes"

# Pasta final dentro do Passo 9 onde as questões renomeadas vão ficar
PASTA_SAIDA = "./questoes_finais"
os.makedirs(PASTA_SAIDA, exist_ok=True)

def renomear_e_copiar(nome_subpasta, prefixo_questao, inicio_real):
    """Lê os arquivos de uma pasta do Passo 8, ordena e renomeia sequencialmente."""
    pasta_origem = os.path.join(CAMINHO_PASSO8, nome_subpasta)
    
    if not os.path.exists(pasta_origem):
        print(f"Aviso: Pasta {nome_subpasta} não encontrada no Passo 8.")
        return

    # Lista e ordena os arquivos
    arquivos = sorted([f for f in os.listdir(pasta_origem) if f.endswith('.png')])
    
    numero_atual = inicio_real
    for arquivo in arquivos:
        if "ingles" in prefixo_questao or "espanhol" in prefixo_questao:
            nome_final = f"questao_{numero_atual:02d}_{prefixo_questao}.png"
        else:
            nome_final = f"questao_{numero_atual:02d}.png"
            
        origem = os.path.join(pasta_origem, arquivo)
        destino = os.path.join(PASTA_SAIDA, nome_final)
        
        shutil.copy2(origem, destino)
        print(f"Renomeado: {nome_subpasta}/{arquivo} -> {nome_final}")
        numero_atual += 1

# --- MAPEAMENTO FINAL DAS QUESTÕES ---
print("Iniciando o Passo 9 - Renomeando imagens finais...\n")

renomear_e_copiar("1-5-ingles", "ingles", 1)
renomear_e_copiar("1-5-espanhol", "espanhol", 1)
renomear_e_copiar("6-34", "regular", 6)
renomear_e_copiar("35-36", "regular", 35)
renomear_e_copiar("37-76", "regular", 37)
renomear_e_copiar("77-79", "regular", 77)
renomear_e_copiar("80-90", "regular", 80)

print(f"\nSucesso! Todas as questões prontas na pasta: {PASTA_SAIDA}")
