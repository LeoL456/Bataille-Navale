import sqlite3
from tkinter import *
from tkinter import ttk


def get_utilisateurs() -> list:
    """
    Arguments : Aucun.
    Retourne : Liste de tuples contenant les informations des joueurs et leurs scores.
    Description : Se connecte à une base de données SQLite 'general.db', récupère tous les enregistrements de la table 'joueurs' et retourne ces informations sous forme de liste.
    """
    conn = sqlite3.connect("general.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM joueurs")
    utilisateurs = cursor.fetchall()
    conn.close()
    return utilisateurs


def leaderboard():
    """
    Arguments : Aucun.
    Retourne : Rien.
    Description : Crée une fenêtre Tkinter qui affiche un tableau de classement (leaderboard) des joueurs. Permet l'ajout ou la suppression de joueurs via des boutons interactifs.
    """
    global root
    root = Tk()
    root.title("Leaderboard | NSI")
    root.geometry("800x600")

    label1 = Label(root, bg="#88cffa", width=1280, height=854)
    label1.place(x=0, y=0)

    label2 = Label(
        root, text="Leaderboard", fg="black", bg="#88cffa", font=("Parisine", 70, "normal")
    )
    label2.pack(pady=50)

    frame1 = Frame(root, bg="#AAE0FE")
    frame1.pack(pady=0)

    columns = ("Nom", "Score")
    tree = ttk.Treeview(frame1, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack()

    button_frame = Frame(root, bg="#88cffa")
    button_frame.pack()

    back = ttk.Button(
        button_frame,
        text="Fermer",
        command=lambda: root.destroy(),
    )

    back.grid(row=0, column=0, padx=10, pady=10)

    addPlayer = ttk.Button(
        button_frame,
        text="+",
        command=lambda: add_player(),
    )

    addPlayer.grid(row=0, column=1, padx=10, pady=10)

    delPlayer = ttk.Button(
        button_frame,
        text="-",
        command=lambda: delete_player(),
    )

    delPlayer.grid(row=0, column=2, padx=10, pady=10)

    def show_users():
        """
        Fonction d'initialisation du tableau des scores qui appelle la fonction get_utilisateurs().
        """
        utilisateurs = get_utilisateurs()
        for utilisateur in utilisateurs:
            tree.insert("", "end", values=(utilisateur[1], utilisateur[2]))

    show_users()

    root.update_idletasks()
    # screen_width = root.winfo_screenwidth()
    # screen_height = root.winfo_screenheight()
    # x = (screen_width) // 5
    # y = (screen_height) // 5
    # root.geometry("+{}+{}".format(x, y))

    root.mainloop()


def delete_player():
    """
    Arguments : Aucun.
    Retourne : Rien.
    Description : Affiche une fenêtre Tkinter permettant de sélectionner et supprimer un joueur de la base de données 'general.db'.
    Met à jour dynamiquement le tableau des scores après la suppression.
    """
    global del_win
    """
    Fonction de suppression d'un utilisateur de la base de données via une liste de noms.
    """
    from tkinter import messagebox

    def delete():
        selected_name = name_combobox.get()

        if not selected_name:
            messagebox.showerror("Erreur", "Veuillez sélectionner un joueur.")
            return

        match = sqlite3.connect("general.db")
        cursor = match.cursor()
        cursor.execute("SELECT id FROM joueurs WHERE nom=?", (selected_name,))
        player_id = cursor.fetchone()[0]
        match.close()

        del_db = sqlite3.connect("general.db")
        cursor = del_db.cursor()
        cursor.execute("DELETE FROM joueurs WHERE id=?", (player_id,))
        del_db.commit()
        del_db.close()

        messagebox.showinfo("Succès", f"Joueur {selected_name} supprimé avec succès.")

    del_win = Tk()
    del_win.title("Supprimer un Joueur")
    del_win.geometry("300x200")

    selectIn = sqlite3.connect("general.db")
    cursor = selectIn.cursor()
    cursor.execute("SELECT nom FROM joueurs")
    player_names = [row[0] for row in cursor.fetchall()]
    selectIn.close()

    name_label = Label(del_win, text="Sélectionner un joueur :")
    name_label.pack()

    name_combobox = ttk.Combobox(del_win, values=player_names)
    name_combobox.pack()

    delete_btn = Button(
        del_win,
        text="Supprimer",
        command=lambda: [delete(), del_win.destroy(), reload_leaderbord()],
    )
    delete_btn.pack()

    del_win.mainloop()


def add_player():
    """
    Arguments : Aucun.
    Retourne : Rien.
    Description : Ouvre une fenêtre Tkinter avec un formulaire pour ajouter un nouveau joueur à la base de données 'general.db'. Met à jour le tableau des scores après l'ajout.
    """
    global add_win
    """
    Formulaire d'inscription au jeu, ajout d'un joueur.
    """
    from tkinter import messagebox

    def save():
        name = name_entry.get()

        if not name:
            messagebox.showerror("Erreur", "Veuillez entrer un nom.")
            return

        verified = sqlite3.connect("general.db")
        cursor = verified.cursor()
        cursor.execute("SELECT COUNT(*) FROM joueurs WHERE nom=?", (name,))
        count = cursor.fetchone()[0]
        verified.close()

        if count > 0:
            messagebox.showerror("Erreur", "Ce nom d'utilisateur existe déjà.")
            return

        insert = sqlite3.connect("general.db")
        cursor = insert.cursor()
        cursor.execute("INSERT INTO joueurs(nom, score) VALUES (?, 0)", (name,))
        insert.commit()
        insert.close()

        messagebox.showinfo("Succès", "Enregistrement réussi!")

    add_win = Tk()
    add_win.title("Nouveau Joueur")

    form_frame = Frame(add_win, padx=50, pady=50)
    form_frame.pack()

    name_label = Label(form_frame, text="Votre nom :")
    name_label.pack()
    name_entry = Entry(form_frame)
    name_entry.pack()

    add_btn = Button(
        form_frame,
        text="Ajouter",
        command=lambda: [save(), add_win.destroy(), reload_leaderbord()],
    )
    add_btn.pack()

    add_win.mainloop()


def reload_leaderbord():
    """
    Arguments : Aucun.
    Retourne : Rien.
    Description : Rafraîchit l'affichage du tableau des scores en fermant et en rouvrant la fenêtre du leaderboard.
    """
    global root
    root.destroy()
    leaderboard()