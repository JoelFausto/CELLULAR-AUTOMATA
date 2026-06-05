# sir_model.py
import numpy as np

class AutomatoSIR:
    def __init__(self, tamanho, beta, p_remover):
        self.N = tamanho
        self.beta = beta
        self.p_remover = p_remover
        self.S, self.I, self.R = 0, 1, 2
        
        # Inicializa matriz zerada (Suscetíveis)
        self.grade = np.zeros((self.N, self.N), dtype=int)
        
    def injetar_foco_inicial(self):
        centro = self.N // 2
        self.grade[centro-1:centro+2, centro-1:centro+2] = self.I

    def _contar_vizinhos_infectados(self, x, y):
        contagem = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if self.grade[(x + dx) % self.N, (y + dy) % self.N] == self.I:
                    contagem += 1
        return contagem

    def atualizar(self):
        nova_grade = self.grade.copy()
        for x in range(self.N):
            for y in range(self.N):
                estado = self.grade[x, y]
                
                if estado == self.S:
                    vizinhos = self._contar_vizinhos_infectados(x, y)
                    if vizinhos > 0:
                        prob_contagio = 1 - (1 - self.beta) ** vizinhos
                        if np.random.rand() < prob_contagio:
                            nova_grade[x, y] = self.I
                            
                elif estado == self.I:
                    if np.random.rand() < self.p_remover:
                        nova_grade[x, y] = self.R
                        
        self.grade = nova_grade

    def obter_contagens(self):
        return {
            'S': np.sum(self.grade == self.S),
            'I': np.sum(self.grade == self.I),
            'R': np.sum(self.grade == self.R)
        }