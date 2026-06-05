# main.py
import matplotlib.pyplot as plt
from sir_model import AutomatoSIR
from seic_model import AutomatoSEIC

# Parâmetros de Simulação
TAMANHO_GRADE = 50
PASSOS_TEMPO = 120

# Taxas epidemiológicas comuns
BETA_TRANSMISSAO = 0.25
TAXA_RECUPERACAO_CRONICIDADE = 0.05
TAXA_INCUBACAO = 0.20  # Exclusivo do SEIC (E -> I)

def rodar_projeto():
    # Instanciando e inicializando os dois modelos separados
    modelo_sir = AutomatoSIR(TAMANHO_GRADE, BETA_TRANSMISSAO, TAXA_RECUPERACAO_CRONICIDADE)
    modelo_seic = AutomatoSEIC(TAMANHO_GRADE, BETA_TRANSMISSAO, TAXA_INCUBACAO, TAXA_RECUPERACAO_CRONICIDADE)
    
    modelo_sir.injetar_foco_inicial()
    modelo_seic.injetar_foco_inicial()
    
    # Dicionários para consolidar o histórico de dados
    dados_sir = {'S': [], 'I': [], 'R': []}
    dados_seic = {'S': [], 'E': [], 'I': [], 'C': []}
    
    print("Executando simulação de Autômatos Celulares...")
    
    # Loop temporal discreto (Simulando o relógio do universo AC)
    for t in range(PASSOS_TEMPO):
        # Captura dados do estado atual
        counts_sir = modelo_sir.obter_contagens()
        for chave in dados_sir:
            dados_sir[chave].append(counts_sir[chave])
            
        counts_seic = modelo_seic.obter_contagens()
        for chave in dados_seic:
            dados_seic[chave].append(counts_seic[chave])
            
        # Evolui o estado das células para o próximo passo (Regras locais do livro de Schiff)
        modelo_sir.atualizar()
        modelo_seic.atualizar()

    print("Simulação concluída com sucesso! Plotando resultados gráficos...")

    # --- Plotagem dos Resultados ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), sharey=True)
    eixo_x = range(PASSOS_TEMPO)
    
    # Cores científicas padronizadas
    c_s, c_e, c_i, c_rc = '#2ecc71', '#f1c40f', '#e74c3c', '#7f8c8d'
    
    # Painel Esquerdo: SIR
    ax1.plot(eixo_x, dados_sir['S'], label='Suscetíveis (S)', color=c_s, linewidth=2.5)
    ax1.plot(eixo_x, dados_sir['I'], label='Infectados (I)', color=c_i, linewidth=2.5)
    ax1.plot(eixo_x, dados_sir['R'], label='Removidos (R)', color=c_rc, linewidth=2.5)
    ax1.set_title("Abordagem Clássica: Modelo SIR", fontsize=13, fontweight='bold')
    ax1.set_xlabel("Tempo Discreto (Passos)", fontsize=11)
    ax1.set_ylabel("Quantidade de Células", fontsize=11)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend()
    
    # Painel Direito: SEIC
    ax2.plot(eixo_x, dados_seic['S'], label='Suscetíveis (S)', color=c_s, linewidth=2.5)
    ax2.plot(eixo_x, dados_seic['E'], label='Expostos (E) - Incubação', color=c_e, linewidth=2.5)
    ax2.plot(eixo_x, dados_seic['I'], label='Infectados (I)', color=c_i, linewidth=2.5)
    ax2.plot(eixo_x, dados_seic['C'], label='Crônicos (C)', color=c_rc, linewidth=2.5)
    ax2.set_title("Adaptação p/ Chagas: Modelo SEIC", fontsize=13, fontweight='bold')
    ax2.set_xlabel("Tempo Discreto (Passos)", fontsize=11)
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    rodar_projeto()