"""
Proposito: Organizar os arquivos para o Passo 5 (ENEM 2022 Digital).
Puxa a pasta de colunas divididas do Passo 4 e a pasta de paginas inteiras.
"""
import os
import shutil

# Definicacao dos caminhos relativos
ORIGEM_PASSO4 = "4Passo-RemoverBordasCentraisDasMetades/divididas-sem-bordas-do-meio"
# Nota: Como no Passo 3 optamos por processar todas juntas para analisar o layout digital,
# criamos a pasta inteiras localmente para organizacao se ela ja existir em passos anteriores.
ORIGEM_INTEIRAS = "3Passo-DividirAoMeioPaginasSemBordas/inteiras" 

DESTINO_COLUNAS = "5Passo-OrganizarImagensColunasEInteiras/divididas-sem-bordas-do-meio"
DESTINO_INTEIRAS = "5Passo-OrganizarImagensColunasEInteiras/inteiras"

print("?? Iniciando a organizacao dos arquivos no Passo 5...")

# 1. Puxa a pasta do Passo 4 para o Passo 5
if os.path.exists(ORIGEM_PASSO4):
    if os.path.exists(DESTINO_COLUNAS):
        shutil.rmtree(DESTINO_COLUNAS)
    shutil.copytree(ORIGEM_PASSO4, DESTINO_COLUNAS)
    print("[OK] Pasta 'divididas-sem-bordas-do-meio' copiada com sucesso para o Passo 5.")
else:
    print(f"?? Alerta: A pasta de origem '{ORIGEM_PASSO4}' nao foi encontrada.")

# 2. Puxa a pasta 'inteiras' se ela existir, senao cria a pasta vazia para triagem
if os.path.exists(ORIGEM_INTEIRAS):
    if os.path.exists(DESTINO_INTEIRAS):
        shutil.rmtree(DESTINO_INTEIRAS)
    shutil.copytree(ORIGEM_INTEIRAS, DESTINO_INTEIRAS)
    print("[OK] Pasta 'inteiras' copiada com sucesso para o Passo 5.")
else:
    os.makedirs(DESTINO_INTEIRAS, exist_ok=True)
    print("[OK] Pasta 'inteiras' criada (vazia) no Passo 5 para futura organizacao.")

print("\n? Organizacao do Passo 5 concluida com sucesso!")
