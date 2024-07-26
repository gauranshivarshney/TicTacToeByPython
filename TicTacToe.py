from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x800")
root.title("Tic Tac Toe")
root.resizable(0, 0)
root.config(background="lightgrey")

f1 = Frame(root, bg="lightgrey")
f1.grid(padx=180)

f2 = Frame(root, pady=30, bg="lightgrey")
f2.grid()

t_label = Label(f1, text="Tic-Tac-Toe", font=("Arial", 30, 'bold'), fg="blue", bg="lightgrey")
t_label.grid(row=0, column=0, columnspan=3, pady=20)

turn_label = Label(f1, text="Player X's turn", font=("Arial", 20), fg="red", bg="lightgrey")
turn_label.grid(row=2, column=0, columnspan=3, pady=10)

board = {
    1:" ", 2:" ", 3:" ",
    4:" ", 5:" ", 6:" ",
    7:" ", 8:" ", 9:" "
}

turn = "X"
game_end = False

def win(player):
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[6] == player:
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[9] == player:
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[7] == player:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[8] == player:
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[9] == player:
        return True
    elif board[1] == board[5] and board[5] == board[9] and board[9] == player:
        return True
    elif board[3] == board[5] and board[5] == board[7] and board[7] == player:
        return True
    return False

def draw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True

def restart():
    global game_end, turn
    game_end = False
    turn = "X"
    turn_label.config(text="Player X's turn")
    for btt in buttons:
        btt["text"] = " "
    for i in board.keys():
        board[i] = " "

def play(event):
    global turn, game_end
    if game_end:
        return
    b = event.widget
    b_text = str(b)
    clicked = b_text[-1]
    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)
    if b["text"] == " ":
        if turn == "X":
            b["text"] = "X"
            board[clicked] = turn
            if win(turn):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {turn} wins the game")
                game_end = True
                return
            turn = "O"
            turn_label.config(text="Player O's turn")
        else:
            b["text"] = "O"
            board[clicked] = turn
            if win(turn):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {turn} wins the game")
                game_end = True
                return
            turn = "X"
            turn_label.config(text="Player X's turn")
        if draw():
            messagebox.showinfo("Tic-Tac-Toe", "Game Draw")
            game_end = True

b1 = Button(f2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightgrey", fg="yellow")
b1.grid(row=2, column=0)
b1.bind("<Button-1>", play)

b2 = Button(f2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightgrey", fg="yellow")
b2.grid(row=2, column=1)
b2.bind("<Button-1>", play)

b3 = Button(f2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightgrey", fg="yellow")
b3.grid(row=2, column=2)
b3.bind("<Button-1>", play)

b4 = Button(f2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightgrey", fg="yellow")
b4.grid(row=3, column=0)
b4.bind("<Button-1>", play)

b5 = Button(f2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightgrey", fg="yellow")
b5.grid(row=3, column=1)
b5.bind("<Button-1>", play)

b6 = Button(f2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightgrey", fg="yellow")
b6.grid(row=3, column=2)
b6.bind("<Button-1>", play)

b7 = Button(f2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightgrey", fg="yellow")
b7.grid(row=4, column=0)
b7.bind("<Button-1>", play)

b8 = Button(f2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightgrey", fg="yellow")
b8.grid(row=4, column=1)
b8.bind("<Button-1>", play)

b9 = Button(f2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightgrey", fg="yellow")
b9.grid(row=4, column=2)
b9.bind("<Button-1>", play)

r_button = Button(f2, text="Restart", width=12, height=1, font=("Arial", 20, 'bold'), command=restart, bg="lightgrey", fg="red")
r_button.grid(row=5, column=0, columnspan=3, pady=30)

buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

root.mainloop()