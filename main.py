from tkinter import messagebox
import tkinter as tk
from random import choice
ta=[]
tb=[]
class Jeu:
    def __init__(self, root, player1_color, player2_color, player1_name, player2_name):
        #ta,tb=[],[]
        self.ta=[]
        self.tb=[]
        self.root = root
        self.root.title("Jeu")
        self.canvas = tk.Canvas(root, width=600, height=600, bg='white')
        self.canvas.pack()
        self.player1_name=player1_name
        self.player2_name=player2_name
        self.player2_color=player2_color
        self.player1_color=player1_color
        self.current_player_label=tk.Label(root, text=f"Au tour de {player1_name}", width=20, height=2,
                                 bg="#F44336", font=("Helvetica", 12), fg=player1_color if player1_name=="A" else player2_color)
        self.current_player_label.pack()
        self.button_return = tk.Button(root, text="Retour au menu", command=self.Menu, width=20, height=2,
                                  bg="#FFC107", fg="white", font=("Helvetica", 12))
        # Création du carré
        self.canvas.create_rectangle(50, 50, 550, 550)

        # Création des diagonales
        self.canvas.create_line(50, 50, 550, 550, fill='black', width=2)  # Diagonale 1
        self.canvas.create_line(550, 50, 50, 550, fill='black', width=2)  # Diagonale 2

        # Création des médianes
        self.canvas.create_line(50, 300, 550, 300, fill='black', width=2)  # Médiane horizontale
        self.canvas.create_line(300, 50, 300, 550, fill='black', width=2)  # Médiane verticale

        # Positionnement initial des pièces
        self.positionner_pieces()
        # Définition des lignes gagnantes
        A1,A2,A3=(50,50),(50,300),(50,550)
        B1,B2,B3=(300,50),(300,300),(300,550)
        C1,C2,C3=(550,50),(550,300),(550,550)
        self.lignes_possibles=[
        [A1,A2,A3],[A1,A3,A2],[A2,A1,A3],
        [A2,A3,A1],[A3,A1,A2],[A3,A2,A1],
        [B1,B2,B3],[B1,B3,B2],[B2,B1,B3],
        [B2,B3,B1],[B3,B1,B2],[B3,B2,B1],
        [C1,C2,C3],[C1,C3,C2],[C2,C1,C3],
        [C2,C3,C1],[C3,C1,C2],[C3,C2,C1],
        [A1,B1,C1],[A1,C1,B1],[B1,C1,A1],
        [B1,A1,C1],[C1,A1,B1],[C1,B1,A1],
        [A2,B2,C2],[A2,C2,B2],[B2,C2,A2],
        [B2,A2,C2],[C2,A2,B2],[C2,B2,A2],
        [A3,B3,C3],[A3,C3,B3],[B3,C3,A3],
        [B3,A3,C3],[C3,A3,B3],[C3,B3,A3],
        [A1,B2,C3],[A1,C3,B2],[B2,A1,C3],
        [B2,C3,A1],[C3,A1,B2],[C3,B2,A1],
        [C1,B2,A3],[C1,A3,B2],[B2,C1,A3],
        [B2,A3,C1],[A3,C1,B2],[A3,B2,C1]
        ]
        self.reinitialiser_jeu()
        # Initialisation des pièces et du joueur actuel
        self.pieces = {'A1': 'boule', 'A2': 'boule', 'A3': 'boule',
                       'B1': 'cylindre', 'B2': 'cylindre', 'B3': 'cylindre'}
        self.joueur_actuel = 'A'
        self.selection = None

        # Gestion des clics
        self.canvas.bind('<Button-1>', self.gerer_clic)
        self.button_return.pack(pady=10)

    def positionner_pieces(self):
        # Positionner les pièces le long des côtés gauche et droit du carré
        for i, (forme_a, forme_b) in enumerate([('boule', 'cylindre')] * 3):
            x_gauche, y_gauche = 25, 150 + i * 150
            x_droite, y_droite = 575, 150 + i * 150
            self.canvas.create_oval(x_gauche - 15, y_gauche - 15, x_gauche + 15, y_gauche + 15, fill='red', tags=('piece', 'A'))  # Pièce A
            self.canvas.create_rectangle(x_droite - 15, y_droite - 15, x_droite + 15, y_droite + 15, fill='blue', tags=('piece', 'B'))# Pièce B

    def gerer_clic(self, event):
        x, y = event.x, event.y

        # Vérifier si une pièce est déjà sélectionnée
        if self.selection:
            # Trouver le point de contact le plus proche des diagonales et médianes
            point_contact = self.trouver_point_contact_proche(x, y)

            # Vérifier s'il y a une autre pièce à cet emplacement
            pieces = self.canvas.find_overlapping(point_contact[0] - 15, point_contact[1] - 15,
                                               point_contact[0] + 15, point_contact[1] + 15)
            if any('piece' in self.canvas.gettags(piece) for piece in pieces):
                # Si une pièce est déjà présente, ne rien faire
                return

            # Déplacer la pièce sélectionnée vers le point de contact
            self.canvas.coords(self.selection, point_contact[0] - 15, point_contact[1] - 15, point_contact[0] + 15, point_contact[1] + 15)
            # supprimer les points du tableau ou il n'ya pas de piece
            if self.joueur_actuel=="A":
            	for x,y in self.ta:
            		piec = self.canvas.find_overlapping(x-15, y-15, x+15, y+15)
            		if not any('piece' in self.canvas.gettags(piece) for piece in piec):
            			self.ta.remove((x,y)) 
            	self.ta.append((point_contact[0],point_contact[1]))
            else:
            	for x, y in self.tb:
            		piec = self.canvas.find_overlapping(x-15, y-15, x+15, y+15)
            		if not any('piece' in self.canvas.gettags(piece) for piece in piec):
            			self.tb.remove((x,y))
            	self.tb.append((point_contact[0],point_contact[1]))
                      	
            # Vérifier s'il y a une ligne alignée
            if self.verifier_ligne_alignee() == True :
                messagebox.showinfo("",f"Le joueur {self.joueur_actuel} a gagné!")
                self.ta=[]
                self.tb=[]
                self.reinitialiser_jeu()
                
                
            else:
                # Changer de joueur
                self.joueur_actuel = 'B' if self.joueur_actuel == 'A' else 'A'
                self.current_player_label.config(text=f"Autour de {self.player1_name if self.joueur_actuel == 'A' else self.player2_name}")
            # Réinitialiser la sélection
            self.selection = None
            # Effacer la surbrillance des points de contact
            self.canvas.delete('surbrillance')
        else:
        # Vérifier si le clic est sur une pièce du joueur en cours
            pieces_du_joueur = self.canvas.find_withtag(self.joueur_actuel)
            for piece_id in pieces_du_joueur:
                if self.point_dans_piece(x, y, piece_id):
                    # Sélectionner la pièce
                    self.selection = piece_id
                # Mettre en surbrillance les positions libres
                    self.mettre_en_surbrillance_positions_libres()
                    break
# Ajouter une nouvelle méthode pour trouver le point de contact le plus proche
    def trouver_point_contact_proche(self, x, y):
        points_contacts = self.points_contacts_diagonales_carré() + self.points_contacts_mediane_carré()
        distance_minimale = float('inf')
        point_proche = None

        for point in points_contacts:
            distance = ((x - point[0]) ** 2 + (y - point[1]) ** 2) ** 0.5
            if distance < distance_minimale:
                distance_minimale = distance
                point_proche = point

        return point_proche

    # Ajouter une nouvelle méthode pour vérifier si un point est dans une pièce
    def point_dans_piece(self, x, y, piece_id):
        coords_piece = self.canvas.coords(piece_id)
        return coords_piece[0] <= x <= coords_piece[2] and coords_piece[1] <= y <= coords_piece[3]

    def mettre_en_surbrillance_positions_libres(self):
        # Mettre en surbrillance les positions libres du plateau en rouge
        for x, y in self.positions_libres():
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red', tags='surbrillance')

    def positions_libres(self):
        # Retourner les positions libres du plateau
        positions = []

        # Ajouter les positions libres le long des diagonales et médianes
        positions.extend(self.points_contacts_diagonales_carré() + self.points_contacts_mediane_carré())

        return positions

    def points_contacts_diagonales_carré(self):
        return [(50, 50), (300, 300), (550, 550), (550, 50), (50, 550)]

    def points_contacts_mediane_carré(self):
        return [(300, 50), (300, 550), (50, 300), (550, 300)]

    def verifier_ligne_alignee(self):
        if (self.joueur_actuel=="A" and self.ta in self.lignes_possibles) or (self.joueur_actuel=="B" and self.tb in self.lignes_possibles):
            return True
        else:
        	return False

    def reinitialiser_jeu(self):
        # Effacer toutes les pièces et les surbrillances
        self.canvas.delete('piece', 'surbrillance')

        # Positionner les nouvelles pièces
        self.positionner_pieces()

        # Réinitialiser le joueur actuel
        self.joueur_actuel = 'A'

        # Réinitialiser la sélection
        self.selection = None

    def Menu(self):
        self.canvas.destroy()
        self.button_return.pack_forget()
        self.current_player_label.pack_forget()
        label_title.pack(pady=20)
        button_start.pack(pady=10)
        button_help.pack(pady=10)
        button_quit.pack(pady=10)

def help_function():
    # Ajoutez ici la fonctionnalité d'aide
    rules = """
    Les règles du jeu Morpion sont simples :
    1.Le jeu commence avec un carré vide et les 3 pions oranges et bleus sont placés sur le plateau.
    2. Deux joueurs s'affrontent, l'un utilisant les pions oranges et l'autre les pions bleus.
    3. Les joueurs placent à tour de rôle un pion de leur couleur sur le carré, en essayant de former une ligne horizontale, verticale ou diagonale de trois pions de leur couleur.
    4. Le joueur qui parvient à aligner trois pions de sa couleur gagne la partie.
    5.Si un joueur aligne trois pions de sa couleur, il gagne la partie.Le déplacement des pions se fait à volonté et librement jusqu'à ce qu'un joueur gagne.
    """
    messagebox.showinfo("Aide", rules)

def quit_function():
    root.destroy()
def start_game():
    button_start.pack_forget()
    button_help.pack_forget()
    button_quit.pack_forget()
    label_title.pack_forget()
    
    label_player1.grid(row=0, column=0, padx=5, pady=5)
    entry_player1.grid(row=0, column=1, padx=5, pady=5)
    label_player2.grid(row=1, column=0, padx=5, pady=5)
    entry_player2.grid(row=1, column=1, padx=5, pady=5)
    color_label_player1.grid(row=0, column=2, padx=5, pady=5)
    color_menu_player1.grid(row=0, column=3, padx=5, pady=5)
    color_label_player2.grid(row=1, column=2, padx=5, pady=5)
    color_menu_player2.grid(row=1, column=3, padx=5, pady=5)
    btn_valid.grid(row=3, columnspan=4, padx=5, pady=5)
    button_return.pack(pady=10)


def valid():
    player1_name = entry_player1.get()
    player2_name = entry_player2.get()
    if not player1_name or not player2_name:
        messagebox.showerror("Erreur", "Veuillez entrer les noms des deux joueurs.")
        return

    player1_color = color_var_player1.get()
    player2_color = color_var_player2.get()

    starting_player = choice([player1_name, player2_name])
    #messagebox.showinfo("Commencement", f"{starting_player} commence la partie!")
    label_player1.grid_remove()
    label_player2.grid_remove()
    entry_player2.grid_remove()
    entry_player1.grid_remove()
    color_label_player1.grid_remove()
    color_menu_player1.grid_remove()
    color_label_player2.grid_remove()
    color_menu_player2.grid_remove()
    btn_valid.grid_remove()
    # Passer les noms des joueurs lors de la création de l'instance de Jeu
    root.after(5000, Jeu(root, player1_color, player2_color, player1_name, player2_name))
def Menu():
    root.destroy()
    button_return.pack_forget()
    current_player_label.pack_forget()
    label_title.pack(pady=20)
    button_start.pack(pady=10)
    button_help.pack(pady=10)
    button_quit.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('800x800')
    root['bg'] = 'green'
    entry_player1 = tk.Entry(root)
    entry_player2 = tk.Entry(root)
    label_player1 = tk.Label(root, text="Nom du Joueur 1:", width=20, height=2,
                                 bg="white", fg="black", font=("Helvetica", 12))
    label_player2 = tk.Label(root, text="Nom du Joueur 2:", width=20, height=2,
                                 bg="white", fg="black", font=("Helvetica", 12))
    color_options = ['blue', 'orange']
    color_var_player1 = tk.StringVar(root, value=color_options[0])
    color_var_player2 = tk.StringVar(root, value=color_options[1])
    color_label_player1 = tk.Label(root, text="Couleur du Joueur 1:", width=20, height=2,
                                 bg="white", fg="black", font=("Helvetica", 12))
    color_menu_player1 = tk.OptionMenu(root, color_var_player1, *color_options)
    color_label_player2 = tk.Label(root, text="Couleur du Joueur 2:", width=20, height=2,
                                 bg="white", fg="black", font=("Helvetica", 12))
    color_menu_player2 = tk.OptionMenu(root, color_var_player2, *color_options)
    label_title = tk.Label(root, text="Morpion à l'Africaine", font=("Helvetica", 24), bg="#F0F0F0")

    button_start = tk.Button(root, text="Commencer le jeu", command=start_game, width=20, height=2,
                                  bg="#4CAF50", fg="white", font=("Helvetica", 12))
                                  
    button_return = tk.Button(root, text="Retour au menu", command=Menu, width=20, height=2,
                                  bg="#FFC107", fg="white", font=("Helvetica", 12))
    button_help = tk.Button(root, text="Aide", command=help_function, width=20, height=2,
                                 bg="#2196F3", fg="white", font=("Helvetica", 12))    
    button_quit = tk.Button(root, text="Quitter", command=quit_function, width=20, height=2,
                                 bg="#F44336", fg="white", font=("Helvetica", 12))
    btn_valid = tk.Button(root, text="Valider", command=valid, width=20, height=2,
                                 bg="#F44336", fg="blue", font=("Helvetica", 12))
                                 
    label_title.pack(pady=20)
    button_start.pack(pady=10)
    button_help.pack(pady=10)
    button_quit.pack(pady=10)


    root.mainloop()