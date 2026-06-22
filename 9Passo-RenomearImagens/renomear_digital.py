
import os
import shutil

# Caminho de origem das paginas limpas (Passo 2) e destino (Passo 9)
PASSO2_DIR = "2Passo-RemoverBordasPaginasInteiras/sem-bordas-externas"
PASSO9_DIR = "9Passo-RenomearImagens"

# Mapeamento com base na leitura do PDF:
# A Questao 180 esta na Pagina 100, a Questao 179 na Pagina 99...
# Logo, a Questao 91 esta na Pagina 11. As paginas 1 a 10 sao capas/instrucoes (lixo).
ajuste_questao = 80  # Exemplo: pagina_enem_11.png -> 11 + 80 = Questao 91

print("🔄 Iniciando a renomeacao direta das questoes digitais para o Passo 9...")

if not os.path.exists(PASSO2_DIR):
    print(f"Erro: A pasta de origem {PASSO2_DIR} nao foi encontrada.")
else:
    # Cria as pastas de destino conforme o padrão que você usa
    pasta_natureza = os.path.join(PASSO9_DIR, "91-135")
    pasta_matematica = os.path.join(PASSO9_DIR, "136-180")
    os.makedirs(pasta_natureza, exist_ok=True)
    os.makedirs(pasta_matematica, exist_ok=True)

    for i in range(11, 101):  # Paginas de 11 a 100
        nome_antigo = f"pagina_enem_{i:02d}.png"
        caminho_antigo = os.path.join(PASSO2_DIR, nome_antigo)

        if os.path.exists(caminho_antigo):
            num_questao = i + ajuste_questao
            nome_novo = f"questao-{num_questao}.png"

            # Separa nas pastas correspondentes de cada grande area
            if num_questao <= 135:
                caminho_novo = os.path.join(pasta_natureza, nome_novo)
            else:
                caminho_novo = os.path.join(pasta_matematica, nome_novo)

            shutil.copy(caminho_antigo, caminho_novo)
            print(f"[OK] {nome_antigo} -> {nome_novo}")

    print("\n✨ Renomeacao do ENEM Digital concluida com sucesso!")
