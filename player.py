from ficha import Ficha

class Player:
    def __init__(self, name, color, origin):
        self.name = name
        self.color = color
        self.origin = origin
        self.fichas = [Ficha(self) for _ in range(4)]
        self.finished_fichas = 0

    def ingresar_ficha(self):
        ingresar = False
        for ficha in self.fichas:
            if ficha.ingame == False:
                ingresar = True
                break
        return ingresar
    
    def ultima_ficha(self):
        ultima_ficha = False
        for ficha in self.fichas:
            if ficha.ingame==True:
                ultima_ficha = ficha
                break
        if ultima_ficha == False:
            return ultima_ficha
        else:
            for ficha in self.fichas:
                if ficha.progress < ultima_ficha.progress and ficha.ingame == True:
                    ultima_ficha = ficha
            return ultima_ficha
    
    def ganador(self):
        ganador = False
        puntaje_total = 0
        for ficha in self.fichas:
            if ficha.winner == True:
                puntaje_total += ficha.valor
        
        if (puntaje_total >= 4):
            ganador = True
        return ganador
    
    def suma_valor_ingame(self):
        suma_valor = 0
        for ficha in self.fichas:
            if ficha.ingame == True:
                suma_valor += ficha.valor
        return suma_valor


