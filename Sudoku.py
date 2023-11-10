import random
class Sudoku:
    def __init__(self,nbr_caché=25,taillegrille=9):
        self.nbrcache = nbr_caché
        self.taillegrille = taillegrille
        self.Creation(self.nbrcache,self.taillegrille)
    
    def Creation(self,nbr_caché,taillegrille):
        # Initialiser une matrice vide
        grillesudoku = [[0] * taillegrille for _ in range(taillegrille)]
        print(taillegrille)
        print(grillesudoku)


        return grillesudoku

    def est_valide(self,matrice,taillegrille, ligne, colonne, nombre):
        print('en construction')
