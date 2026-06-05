# Análise Epidemiológica Espacial da Doença de Chagas: Modelos SIR versus SEIC em Ambientes Discretos

## 📋 Sobre o Projeto

Diferente de modelos epidemiológicos tradicionais baseados em Equações Diferenciais Ordinárias (EDOs) que assumem uma "mistura homogênea" da população, este simulador modela o contágio geograficamente de forma descentralizada. 

No contexto da **Doença de Chagas**, a transmissão não ocorre diretamente de humano para humano, mas sim pela presença local do vetor (o triatomíneo/barbeiro). O modelo utiliza a densidade de infectados na vizinhança de uma célula saudável como um indicador indireto da atividade local do vetor.

### Modelos Implementados:
1. **Modelo SIR Clássico:** Transição direta de Suscetível para Infectado ativo, resultando em uma onda epidêmica veloz e compacta.
2. **Modelo SEIC Customizado:** Introduz o estado **Exposto (E)** para mapear o período latente de incubação do *Trypanosoma cruzi* e o estado **Crônico (C)** para representar a evolução clínica real da doença, revelando um efeito mosaico e um forte achatamento na curva de contágio ativo.

## 📁 Estrutura do Projeto

```
cellular-automata/
├── requirements.txt   # Dependências
├── sir_model.py       # Classe encapsulada com a lógica e varredura espacial do modelo SIR.
├── seic_model.py      # Classe estendida com os estados e regras de atraso (delay) do modelo SEIC.
├── main.py            # Script mestre coordenador da simulação, coleta de dados e renderização gráfica.
└── README.md          # Documentação do projeto
```

## 🛠 Tecnologias Utilizadas

- Python 3 - Linguagem principal
- NumPy - Cálculos científicos e arrays
- Matplotlib - Visualização de gráficos

## 🔧 Como Executar o Projeto

1. Clone este repositório:
```
https://github.com/JoelFausto/CELLULAR-AUTOMATA.git
```
2. Acesse o diretório do projeto:
```
cd CELLULAR-AUTOMATA
```
3. Instale as dependências necessárias:
```
pip install -r requirements.txt
```
4. Execute o script principal:
```
python main_simulacao.py
```

## 📎 Link Artigo

[Análise Epidemiológica Espacial da Doença de Chagas: Modelos SIR versus SEIC em Ambientes Discretos](https://drive.google.com/file/d/147ZOpxSabpGJ4y34yOGLTkG8U9VODT3t/view?usp=sharing)

## 📑 Fontes Teóricas

- SCHIFF, Joel L. Cellular Automata: A Discrete View of the World. Wiley Series in Discrete Mathematics & Optimization. Hoboken: John Wiley & Sons, 2008. (Obra base para as regras locais, sincronização e fronteiras toroidais).
- KEELING, M. J.; ROHANI, P. Modeling Infectious Diseases in Humans and Animals. Princeton: Princeton University Press, 2008. (Abordagem de modelos compartimentais estruturados).
- RASSI, A.; RASSI, A.; MARIN-NETO, J. A. Chagas disease. The Lancet, v. 375, n. 9723, p. 1388-1402, 2010. (Subsídio clínico para a caracterização das fases aguda/incubação e crônica da patologia).



