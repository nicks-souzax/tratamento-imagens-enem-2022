import os
import shutil

# Defina os caminhos das pastas do Passo 7 (ajuste os caminhos se necessário)
CAMINHO_PASSO7 = "../7Passo-DividirPelaFaixaAzul"
PASTA_COLUNAS = os.path.join(CAMINHO_PASSO7, "questoes_colunas")
PASTA_PAG15 = os.path.join(CAMINHO_PASSO7, "pagina_15")
PASTA_PAG28 = os.path.join(CAMINHO_PASSO7, "pagina_28")

# Pasta atual (Passo 8) onde os resultados serão salvos
PASTA_DESTINO_RAIZ = "."

def mover_intervalo_imagens(pasta_origem, nome_subpasta_destino, inicio_num, fim_num):
    """Cria uma pasta no Passo 8 e move um intervalo de imagens específicas para ela."""
    nova_pasta = os.path.join(PASTA_DESTINO_RAIZ, nome_subpasta_destino)
    os.makedirs(nova_pasta, exist_ok=True)
    
    for i in range(inicio_num, fim_num + 1):
        nome_arquivo = f"parte_{i:03d}.png"
        origem = os.path.join(pasta_origem, nome_arquivo)
        destino = os.path.join(nova_pasta, nome_arquivo)
        
        if os.path.exists(origem):
            shutil.move(origem, destino)
            print(f"Movido: {nome_arquivo} -> {nome_subpasta_destino}")

def mover_e_renomear_pasta(pasta_origem, nome_subpasta_destino, lixos_para_remover=[]):
    """Move uma pasta inteira do Passo 7 para o Passo 8, remove arquivos inúteis e renomeia."""
    destino_completo = os.path.join(PASTA_DESTINO_RAIZ, nome_subpasta_destino)
    
    if os.path.exists(pasta_origem):
        # Copia/Move a pasta inteira
        shutil.copytree(pasta_origem, destino_completo, dirs_exist_ok=True)
        
        # Remove os arquivos marcados como "lixo"
        for lixo in lixos_para_remover:
            caminho_lixo = os.path.join(destino_completo, lixo)
            if os.path.exists(caminho_lixo):
                os.remove(caminho_lixo)
                print(f"Excluído lixo: {lixo} de {nome_subpasta_destino}")
        print(f"Pasta organizada: {nome_subpasta_destino}")

# --- EXECUÇÃO DO FLUXO DO PASSO 8 ---

print("Iniciando organização do Passo 8...")

# 1. Organizando a pasta "questoes_colunas" por partes
mover_intervalo_imagens(PASTA_COLUNAS, "1-5-ingles", 2, 6)
mover_intervalo_imagens(PASTA_COLUNAS, "1-5-espanhol", 7, 11)
mover_intervalo_imagens(PASTA_COLUNAS, "6-34", 12, 40)
mover_intervalo_imagens(PASTA_COLUNAS, "37-76", 41, 80)

# 2. Puxando as pastas de páginas inteiras, limpando lixos e renomeando
mover_e_renomear_pasta(PASTA_PAG15, "35-36", lixos_para_remover=["parte_001.png"])
mover_e_renomear_pasta(PASTA_PAG28, "77-79", lixos_para_remover=["parte_001.png"])

# 3. Por fim, o que sobrou na "questoes_colunas" vira a pasta 80-90
mover_e_renomear_pasta(PASTA_COLUNAS, "80-90", lixos_para_remover=["parte_001.png"])

print("Organização concluída com sucesso!")
