# seic_model.py
import numpy as np

class AutomatoSEIC:
    def __init__(self, tamanho, beta, p_infectar, p_cronificar):
        self.N = tamanho
        self.beta = beta
        self.p_infectar = p_infectar
        self.p_cronificar = p_cronificar
        self.S, self.E, self.I, self.C = 0, 1, 2, 3
        
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
                            nova_grade[x, y] = self.E
                            
                elif estado == self.E:
                    if np.random.rand() < self.p_infectar:
                        nova_grade[x, y] = self.I
                        
                elif estado == self.I:
                    if np.random.rand() < self.p_cronificar:
                        nova_grade[x, y] = self.C
                        
        self.grade = nova_grade

    def obter_contagens(self):
        return {
            'S': np.sum(self.grade == self.S),
            'E': np.sum(self.grade == self.E),
            'I': np.sum(self.grade == self.I),
            'C': np.sum(self.grade == self.C)
        }