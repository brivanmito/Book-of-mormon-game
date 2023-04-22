import tkinter as tk
from tkinter import messagebox, Toplevel
from tkinter import *
import random
import csv
from csv import writer
# Function to center the windows, because when they are created they are not positioned in the center of the screen.
def center_windows(ventana):
    ventana.update_idletasks()
    widht = ventana.winfo_width()
    heigth = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (widht // 2)
    y = (ventana.winfo_screenheight() // 2) - (heigth // 2)
    ventana.geometry('{}x{}+{}+{}'.format(widht, heigth, x, y))

# Function so that the user can log in with his user name, if he has not entered his user name, he will be asked if he wants to create one.
def create_windows_login(principal_window_game):
    # Properties for the created window
    windows_login = tk.Toplevel(principal_window_game)
    windows_login.configure(bg="#0D3B66")
    windows_login.title("Windows Log in")
    windows_login.geometry("400x430")
    # Create a label with the name of the game
    label1 = tk.Label(windows_login, text="Book \nof \nMormon \nGame", font=("Helvetica", 20), bg="#0D3B66",fg="#D4AF37")
    label1.place(x=50, y=50, width=300, height=200)
    labelusername = tk.Label(windows_login, text="Username: ", font=("Helvetica", 14), bg="#0D3B66", fg="white")
    labelusername.place(x=50, y=300, width=100, height=30)
    usernameentry = tk.Entry(windows_login, font=("Helvetica", 12))
    usernameentry.place(x=180, y=300, width=170, height=30)
    # This button calls the verify_user function to find out if the user is logged in.
    validateuserbutton = tk.Button(windows_login, text="Log in", font=("Helvetica", 12), command=lambda:verify_user(usernameentry.get()))
    validateuserbutton.place(x=150, y=350, width=100, height=30)
    # This function is called by the back button, when you are inside the Log in window, so you can cancel your entry to the game or you can go to the main menu.
    def back_principal_window():
        windows_login.destroy()
        principal_window_game.deiconify()
    # This function allows me to use the read_list function indirectly, I could have called read list directly, but in order to test with Pytest I did it through juan nested function.
    def verify_user(username):
        if validate_user_existence(username):
            global player
            player = username
            # 
            create_windows_quizz(windows_login, principal_window_game)
        else:
            question = messagebox.askquestion("Sorry", "The username don't exist.\n Press YES to create an username\nPress NO to try again")
            if question == "yes":
                create_window_for_create_username(windows_login, principal_window_game)
            

    boton_volver = tk.Button(windows_login, text="Volver a la ventana principal_window_game", command=back_principal_window)
    boton_volver.pack(pady=10)

    center_windows(windows_login)

def create_window_for_create_username(windows_login, principal_window_game):
    """
    This function creates the window for the questionnaires, and I send it two parameters
    that are the:
    principal_window: winow that allows me to start the game or exit
    username window: This window is for user creation, it allows me to go back or exit.
    this allows me to hide the windows since I am not working with classes.
    """
    windows_login.destroy()
    windows_username = tk.Toplevel(principal_window_game)
    windows_username.title("Sign up")
    windows_username.configure(bg="#0D3B66")
    windows_username.geometry("400x430")
    center_windows(windows_username)
    buttonExit = tk.Button(windows_username, text="Exit", font=("Helvetica", 14), command=lambda: (principal_window_game.destroy()))
    buttonExit.place(x=150, y=30)
    buttonHome = tk.Button(windows_username, text="Home", font=("Helvetica", 14), command=lambda: (windows_username.withdraw(), principal_window_game.deiconify()))
    buttonHome.place(x=200, y=30)
    labelusername = tk.Label(windows_username, text="Username: ", font=("Helvetica", 14), bg="#0D3B66", fg="white")
    labelusername.place(x=50, y=100, width=100, height=30)
    usernameentry = tk.Entry(windows_username, font=("Helvetica", 12))
    usernameentry.place(x=180, y=100, width=170, height=30)
    labelname = tk.Label(windows_username, text="Name: ", font=("Helvetica", 14), bg="#0D3B66", fg="white")
    labelname.place(x=50, y=150, width=100, height=30)
    nameentry = tk.Entry(windows_username, font=("Helvetica", 12))
    nameentry.place(x=180, y=150, width=170, height=30)
    labelname = tk.Label(windows_username, text="Last Name: ", font=("Helvetica", 14), bg="#0D3B66", fg="white")
    labelname.place(x=50, y=200, width=100, height=30)
    nameentry = tk.Entry(windows_username, font=("Helvetica", 12))
    nameentry.place(x=180, y=200, width=170, height=30)


def create_windows_quizz(windows_login, principal_window_game):
    global list_of_questions
    list_of_questions = read_list("windows.csv")

    windows_quizz = tk.Toplevel(principal_window_game)
    windows_quizz.title("Quizz")
    windows_quizz.configure(bg="#0D3B66")
    windows_quizz.attributes('-fullscreen', True)
    buttonExit = tk.Button(windows_quizz, text="Exit", font=("Helvetica", 14), command=lambda: (principal_window_game.destroy()))
    buttonExit.pack(padx=10, pady=10)
    buttonExit = tk.Button(windows_quizz, text="Home", font=("Helvetica", 14), command=lambda: (windows_quizz.withdraw(), principal_window_game.deiconify()))
    buttonExit.place(x=590, y=10)
    def back_principal_window():
        windows_quizz.destroy()
        principal_window_game.deiconify()

    if len(list_of_questions) != 0:
        list_of_questions_random = random_position(list_of_questions)
        pregunta_lbl = tk.Label(windows_quizz, text=list_of_questions_random[pregunta_actual][0], width=300, height=2, font=('Helvetica', 14), justify='center', bg="#0D3B66", fg="white")
        pregunta_lbl.pack(padx=10, pady=10)
        botones = []
        options = list_of_questions_random[pregunta_actual][1:5]
        global x
        x = random_position(options)
        for i in range(4):
            boton_back = tk.Button(windows_quizz, text=x[i], bg="#D4AF37", font=('Helvetica', 12), width=100, height=2, command=lambda opcion=i: change_color_on_bottons(list_of_questions_random, pregunta_actual, opcion, botones, siguiente_btn, x))
            boton_back.pack(pady=5)
            botones.append(boton_back)

        siguiente_btn = tk.Button(windows_quizz, text='Siguiente', font=('Helvetica', 12), width=20, height=2, state=tk.DISABLED, command=lambda:cambiar_pregunta(list_of_questions_random, pregunta_lbl, botones, siguiente_btn, number_of_question, windows_quizz, principal_window_game))
        siguiente_btn.pack(pady=10)
        number_of_question = tk.Label(windows_quizz, text=f"1 / {len(list_of_questions)} \nQuestions", bg="#0D3B66", fg="#D4AF37", font=("Helvetica", 12))
        number_of_question.pack(pady=10)
        windows_login.destroy()
    else:
        windows_login.destroy()
        boton_back = tk.Button(windows_quizz, text="Home", font=('Helvetica', 12), width=20, height=2, command=back_principal_window)
        boton_back.pack(padx=50, pady=10)
        boton_back = tk.Button(windows_quizz, text="Exit", font=('Helvetica', 12), width=20, height=2, command=lambda: (principal_window_game.destroy()))
        boton_back.pack(padx=50, pady=10)
        boton_back = tk.Button(windows_quizz, text="Add Questions", font=('Helvetica', 12), width=20, height=2, command=lambda: (windows_quizz.destroy(), create_window_add_questions(principal_window_game)))
        boton_back.pack(padx=50, pady=10)
        label = tk.Label(windows_quizz, text="There are not questions in the questions.csv")
        label.pack(padx=50, pady=50)

    center_windows(windows_quizz)

def create_window_add_questions(principal_window_game):
    windows4 = tk.Toplevel(principal_window_game)
    windows4.title("Quizz")
    windows4.configure(bg="#0D3B66")
    windows4.attributes('-fullscreen', True)
    buttonExit = tk.Button(windows4, text="Exit", font=("Helvetica", 14), command=lambda: (principal_window_game.destroy()))
    buttonExit.pack(padx=10, pady=10)
    buttonExit = tk.Button(windows4, text="Home", font=("Helvetica", 14), command=lambda: (windows4.withdraw(), principal_window_game.deiconify()))
    buttonExit.place(x=590, y=10)
    buttonSeeQuestions = tk.Button(windows4, text="Questions", font=("Helvetica", 14), command=lambda: (windows4.withdraw(), windows4_see_and_editing_questions_in_file(principal_window_game)))
    buttonSeeQuestions.place(x=708, y=10)
    pregunta_lbl = tk.Label(windows4, text="Question", width=300, height=2, font=('Helvetica', 14), justify='center', bg="#0D3B66", fg="white")
    pregunta_lbl.pack(padx=10, pady=10)
    entry_question = tk.Entry(windows4, font=("Helvetica", 12), width=100)
    entry_question.pack(padx=10, pady=10)
    answer_lbl1 = tk.Label(windows4, text="Correct anwer", width=300, height=2, font=('Helvetica', 14), justify='center', bg="#0D3B66", fg="white")
    answer_lbl1.pack(padx=10, pady=10)
    entry_correct_answer = tk.Entry(windows4, font=("Helvetica", 12), width=100, bg="green")
    entry_correct_answer.pack(padx=10, pady=10)
    answer_lbl2 = tk.Label(windows4, text="Aditional answers", width=300, height=2, font=('Helvetica', 14), justify='center', bg="#0D3B66", fg="white")
    answer_lbl2.pack(padx=20, pady=20)
    entry_answer1 = tk.Entry(windows4, font=("Helvetica", 12), width=100)
    entry_answer1.pack(padx=10, pady=10)
    entry_answer2 = tk.Entry(windows4, font=("Helvetica", 12), width=100)
    entry_answer2.pack(padx=10, pady=10)
    entry_answer3 = tk.Entry(windows4, font=("Helvetica", 12), width=100)
    entry_answer3.pack(padx=10, pady=10)
    scripture_label = tk.Label(windows4, text="Scripture: example. (2 Nephi:3-4)", width=300, height=2, font=('Helvetica', 14), justify='center', bg="#0D3B66", fg="white")
    scripture_label.pack(padx=10, pady=10)
    entry_scripture = tk.Entry(windows4, font=("Helvetica", 12), width=100)
    entry_scripture.pack(padx=10, pady=10)
    boton_back = tk.Button(windows4, text="Add Question", font=('Helvetica', 12), width=20, height=2, command=lambda: writing_on_csv_file(entry_question, entry_correct_answer, entry_answer1, entry_answer2, entry_answer3, entry_scripture))
    boton_back.pack(padx=20, pady=20)

def windows4_see_and_editing_questions_in_file(principal_window_game):
    list_of_questions = read_list("windows.csv")
    pregunta_actual = 0
    windows4 = tk.Toplevel(principal_window_game)
    windows4.title("Quizz")
    windows4.configure(bg="#0D3B66")
    windows4.attributes('-fullscreen', True)
    buttonExit = tk.Button(windows4, text="Exit", font=("Helvetica", 14), command=lambda: (principal_window_game.destroy()))
    buttonHome = tk.Button(windows4, text="Home", font=("Helvetica", 14), command=lambda: (windows4.withdraw(), principal_window_game.deiconify()))
    buttonSeeQuestions = tk.Button(windows4, text="Questions", font=("Helvetica", 14), state=DISABLED)
    pregunta_lbl = tk.Label(windows4, text="Question", width=300, height=2, font=('Helvetica', 14), justify='center', bg="#0D3B66", fg="white")
    entry_question = tk.Entry(windows4, font=("Helvetica", 12), width=100)
    answer_lbl1 = tk.Label(windows4, text="Correct anwer", width=300, height=2, font=('Helvetica', 14), justify='center', bg="#0D3B66", fg="white")
    entry_correct_answer = tk.Entry(windows4, font=("Helvetica", 12), width=50, bg="green")
    answer_lbl2 = tk.Label(windows4, text="Aditional answers", width=300, height=2, font=('Helvetica', 14), justify='center', bg="#0D3B66", fg="white")
    entry_answer1 = tk.Entry(windows4, font=("Helvetica", 12), width=50)
    entry_answer2 = tk.Entry(windows4, font=("Helvetica", 12), width=50)
    entry_answer3 = tk.Entry(windows4, font=("Helvetica", 12), width=50)
    number_of_question = tk.Label(windows4, text=f"1 / {len(list_of_questions)} \nQuestions", bg="#0D3B66", fg="#D4AF37", font=("Helvetica", 12))
    scripture_label = tk.Label(windows4, text="Scripture: example. (2 Nephi:3-4)", width=300, height=2, font=('Helvetica', 14), justify='center', bg="#0D3B66", fg="white")
    entry_scripture = tk.Entry(windows4, font=("Helvetica", 12), width=50)
    boton_back = tk.Button(windows4, text="Back Question", font=('Helvetica', 12), width=20, height=2, command=lambda: back_question(list_of_questions, entry_question, entry_correct_answer, entry_answer1, entry_answer2, entry_answer3, entry_scripture, number_of_question))
    boton_next = tk.Button(windows4, text="Next Question", font=('Helvetica', 12), width=20, height=2, command=lambda: next_question(list_of_questions, entry_question, entry_correct_answer, entry_answer1, entry_answer2, entry_answer3, entry_scripture, number_of_question))
    if len(list_of_questions) != 0:
        load_questions(list_of_questions, entry_question, entry_correct_answer, entry_answer1, entry_answer2, entry_answer3, entry_scripture, number_of_question)
    # Placing control on the window
    buttonExit.pack(padx=10, pady=10)
    buttonHome.place(x=590, y=10)
    buttonSeeQuestions.place(x=708, y=10)
    pregunta_lbl.pack(padx=10, pady=10)
    entry_question.pack(padx=10, pady=10)
    answer_lbl1.pack(padx=10, pady=10)
    entry_correct_answer.pack(padx=10, pady=10)
    answer_lbl2.pack(padx=20, pady=20)
    entry_answer1.pack(padx=10, pady=10)
    entry_answer2.pack(padx=10, pady=10)
    entry_answer3.pack(padx=10, pady=10)
    scripture_label.pack(padx=10, pady=10)
    entry_scripture.pack(padx=10, pady=10)
    boton_back.place(x=130, y=400)
    boton_next.place(x=1050, y=400)
    number_of_question.pack(pady=10)

def load_questions(list_of_questions, entry_question, entry_correct_answer, entry_answer1, entry_answer2, entry_answer3, entry_scripture, number_of_question):
    pregunta = list_of_questions[pregunta_actual]
    entry_question.delete(0, tk.END)
    entry_correct_answer.delete(0, tk.END)
    entry_answer1.delete(0, tk.END)
    entry_answer2.delete(0, tk.END)
    entry_answer3.delete(0, tk.END)
    entry_scripture.delete(0, tk.END)
    entry_question.insert(0, pregunta[0])
    entry_correct_answer.insert(0, pregunta[1])
    entry_answer1.insert(0, pregunta[2])
    entry_answer2.insert(0, pregunta[3])
    entry_answer3.insert(0, pregunta[4])
    entry_scripture.insert(0, pregunta[5])
    number_of_question['text'] = f"{pregunta_actual + 1} / {len(list_of_questions)} \nQuestions"

def back_question(list_of_questions, entry_question, entry_correct_answer, entry_answer1, entry_answer2, entry_answer3, entry_scripture, number_of_question):
    global pregunta_actual 
    i = 0
    if pregunta_actual > 0 and pregunta_actual < len(list_of_questions):
        pregunta_actual -= 1
        pregunta = list_of_questions[pregunta_actual]
        entry_question.delete(0, tk.END)
        entry_correct_answer.delete(0, tk.END)
        entry_answer1.delete(0, tk.END)
        entry_answer2.delete(0, tk.END)
        entry_answer3.delete(0, tk.END)
        entry_scripture.delete(0, tk.END)
        entry_question.insert(0, pregunta[i])
        entry_correct_answer.insert(0, pregunta[0])
        entry_answer1.insert(0, pregunta[1])
        entry_answer2.insert(0, pregunta[2])
        entry_answer3.insert(0, pregunta[3])
        entry_scripture.insert(0, pregunta[4])
        number_of_question['text'] = f"{pregunta_actual + 1} / {len(list_of_questions)} \nQuestions"



def next_question(list_of_questions, entry_question, entry_correct_answer, entry_answer1, entry_answer2, entry_answer3, entry_scripture, number_of_question):
    global pregunta_actual 
    i = 0
    pregunta_actual += 1
    if pregunta_actual <= len(list_of_questions) -1:
        pregunta = list_of_questions[pregunta_actual]
        entry_question.delete(0, tk.END)
        entry_correct_answer.delete(0, tk.END)
        entry_answer1.delete(0, tk.END)
        entry_answer2.delete(0, tk.END)
        entry_answer3.delete(0, tk.END)
        entry_scripture.delete(0, tk.END)
        entry_question.insert(0, pregunta[i])
        entry_correct_answer.insert(0, pregunta[0])
        entry_answer1.insert(0, pregunta[1])
        entry_answer2.insert(0, pregunta[2])
        entry_answer3.insert(0, pregunta[3])
        entry_scripture.insert(0, pregunta[4])
        number_of_question['text'] = f"{pregunta_actual + 1} / {len(list_of_questions)} \nQuestions"
    else:
        pregunta_actual = len(list_of_questions) -1

def writing_on_csv_file(entry_question, entry_correct_answer, entry_answer1, entry_answer2, entry_answer3, entry_scripture):
    if entry_question.get() != "" and entry_correct_answer.get() != "" and entry_answer1.get() != "" and entry_answer2.get() != "" and entry_answer3.get() != "" and entry_scripture.get() != "":
        creating_questions(entry_question, entry_correct_answer, entry_answer1, entry_answer2, entry_answer3, entry_scripture)
        messagebox.showinfo("Question added", "Congratulations! You added a new question!")
        entry_question.delete(0, tk.END)
        entry_correct_answer.delete(0, tk.END)
        entry_answer1.delete(0, tk.END)
        entry_answer2.delete(0, tk.END)
        entry_answer3.delete(0, tk.END)
        entry_scripture.delete(0, tk.END)
    else:
        messagebox.showinfo("Question not added", "Make sure you enter all the entries!")

def random_position(options):
    lista_mezclada = random.sample(options, len(options))
    return lista_mezclada
    
def creating_questions(entry_question, entry_correct_answer, entry_answer1, entry_answer2, entry_answer3, entry_scripture):
    with open("windows.csv", "a", newline='') as file:
        writer1 = writer(file)
        question_line = []
        question_line.append(entry_question.get())
        question_line.append(entry_correct_answer.get())
        question_line.append(entry_answer1.get())
        question_line.append(entry_answer2.get())
        question_line.append(entry_answer3.get())
        question_line.append(entry_scripture.get())
        writer1.writerow(question_line)


def change_color_on_bottons(respuestas, pregunta_actual, opcion_seleccionada, botones, siguiente_btn, x):
    
    # respuesta_correcta = int(respuestas[pregunta_actual][-1]) - 1
    respuesta_correcta = respuestas[pregunta_actual][1]
    opcion_seleccionada = x[opcion_seleccionada]
    for i in botones:
        if i['text'] == respuesta_correcta:
            i['bg'] = 'green'
        elif i['text'] == opcion_seleccionada:
            i['bg'] = 'red'
        else:
            i['bg'] = '#D4AF37'
    global score
    if verify_answer(opcion_seleccionada, respuesta_correcta):
        score += 1
    # Disable Buttons, this allows that once selected the user can no longer select another back button.
    enabled_disabled_botoms(botones)
    siguiente_btn['state'] = tk.NORMAL

def verify_answer(opcion_selected, correct_opcion):
    """
    Function that verifies if the selected answer is correct, it receives two parameters:
    - option_selected: It is the option selected by the user.
    - option_correct_option: It is the correct option written in the csv file.
    """
    if opcion_selected == correct_opcion:
        return True
    else:
        return False
# Enable Buttons, this allows that once selected the user can no longer select another back button.
def enabled_disabled_botoms(botons):
    for i in range(len(botons)):
        if botons[i]['state'] == NORMAL:
            botons[i]['state'] = tk.DISABLED
        else:
            botons[i]['state'] = tk.NORMAL

def show_question_on_quizz(preguntas, pregunta_actual, pregunta_lbl, botones, siguiente_btn, number_of_question):
    pregunta_lbl['text'] = preguntas[pregunta_actual][0]
    number_of_question['text'] = f"{pregunta_actual + 1} / {len(list_of_questions)}"
    options = preguntas[pregunta_actual][1:5]
    global x
    x = random_position(options)
    for i in range(4):
        botones[i]['text'] = x[i]
        botones[i]['bg'] = '#D4AF37'
    # for i in range(len(botones)):
    #     botones[i]['state'] = tk.NORMAL
    enabled_disabled_botoms(botones)
    siguiente_btn['state'] = tk.DISABLED

def cambiar_pregunta(preguntas, pregunta_lbl, botones, siguiente_btn, number_of_question, windows_quizz, principal_window_game):
    global pregunta_actual 
    pregunta_actual += 1
    if pregunta_actual < len(preguntas):
        show_question_on_quizz(preguntas, pregunta_actual, pregunta_lbl, botones, siguiente_btn, number_of_question)
    else:
        for i in range(4):
            botones[i].destroy()
            final_result = compute_score()
            siguiente_btn.destroy()
            if final_result >= 80:
                username_label = tk.Label(windows_quizz, text=f"Congratulations {player.upper()} Continue your scripture study", font=('Helvetica', 20), bg="#0D3B66")
                score_lbl = tk.Label(windows_quizz, text=f"{final_result}%", fg="green", font=('Helvetica', 30), bg="#0D3B66")
            else:
                username_label = tk.Label(windows_quizz, text=f"We're sorry, Try Again {player.upper()}", bg="#0D3B66", fg="white", font=('Helvetica', 20))
                score_lbl = tk.Label(windows_quizz, text=f"{final_result}%", fg="red", font=('Helvetica', 30), bg="#0D3B66")
        username_label.pack(pady=10)
        score_lbl.pack(pady=10)
        pregunta_lbl['text'] = 'Fin del cuestionario'
        pregunta_lbl["bg"] = "#0D3B66"
        pregunta_actual = 0
        global score
        score = 0
        finish_boton = tk.Button(windows_quizz, text="Finish", command=lambda: (windows_quizz.destroy(), principal_window_game.deiconify()))
        finish_boton.pack(pady=10)

def compute_score():
    final_result = (score / len(list_of_questions)) * 100
    return int(final_result)

pregunta_actual = 0
score = 0
player = ""
x = []
def main():
    global windows_quizz
    principal_window_game = tk.Tk()
    principal_window_game.configure(bg="#0D3B66")
    principal_window_game.title("Book of Mormon Game")
    principal_window_game.attributes('-fullscreen', True)
    label1 = tk.Label(principal_window_game, text="Book \nof \nMormon \nGame", font=("Helvetica", 30), bg="#0D3B66",fg="#D4AF37")
    # label1.place(x=100, y=50, width=300, height=200)
    label1.place(relx=0.5, rely=0.3, width=300, height=200, anchor='c')



    buttonStart = tk.Button(principal_window_game, text="Start", font=("Helvetica", 18), command=lambda: (principal_window_game.withdraw(), create_windows_login(principal_window_game)))
    buttonStart.place(relx=0.3, rely=0.6, width=150, height=50)
    buttonExit = tk.Button(principal_window_game, text="Questions", font=("Helvetica", 18), command=lambda: (principal_window_game.withdraw(), create_window_add_questions(principal_window_game)))
    buttonExit.place(relx=0.45, rely=0.6, width=150, height=50)
    buttonExit = tk.Button(principal_window_game, text="Exit", font=("Helvetica", 18), command=lambda: (principal_window_game.destroy()))
    buttonExit.place(relx=0.6, rely=0.6, width=150, height=50)


    

    center_windows(principal_window_game)
    principal_window_game.mainloop()


def validate_user_existence(username):
        filename = "players.csv"
        KEY_COLUMN_INDEX_DIC = 0
        players_list = read_dictionary("players.csv", KEY_COLUMN_INDEX_DIC)

        if search_user_in_a_dictionary(username, players_list):
            return True
        else:
            return False

def search_user_in_a_dictionary(key, dictionary_play):
    
    if key in dictionary_play:
        return True
    else:
        return False
    
def read_list(filename):
    """Read the contents of a CSV file into a compound list and return a list
    Parameters
            filename: the name of the csv file to read.
    Return: a compund list
    """
    question_list = []
    try:
        with open(filename, "rt", encoding='utf-8') as csv_file:
            # Use the module to create a reader.
            # Object that will read from the opened file.
            reader = csv.reader(csv_file)
            # The first row of the CSV file contains column headings and not data about the questions
            next(reader)
            # Read each row in the csv file one at time.
            # The reader object returns each row as a list.
            for rowlist in reader:
                # If the current row is not blank,
                # append it to the compound_list.
                if len(rowlist) != 0:
                    # Append one row from the CSV
                    # file to the compound list.
                    question_list.append(rowlist)
    except StopIteration:
        messagebox.showwarning("Warning!", "The windows.csv is empty \nDo you want add questions?", icon="warning")
    except FileNotFoundError:
        messagebox.showwarning("Warning!", "The windows.csv is not on your computer \nCreate a csv file", icon="warning")
        columns = ["Example: Question", "correct answer", "incorrect answer 1", "incorrect answer 2", "incorrect answer 3", "reference", "scripture"]
        with open(filename, mode='w') as file:
            writer = csv.DictWriter(file, delimiter=",", fieldnames=columns)
            writer.writeheader()
    # Return the compound list.
    return question_list

def read_dictionary(filename, key_index):
    """Read the contents of a CSV file into a dictionary and return a the dictionary
    Parameters
            filename: the name of the csv file to read.
            key_index: 
    Return: a dictionary
    """
    with open(filename, "rt", encoding='utf-8') as csv_file:
        # Use the module to create a reader.
        # Object that will read from the opened file.
        reader = csv.reader(csv_file)
        # The first row of the CSV file contains column headings and not data about the questions
        next(reader)
        # Read each row in the csv file one at time.
        # The reader object returns each row as a list.
        dictionary = {}
        for rowlist in reader:
            # If the current row is not blank,
            # append it to the compound_list.
            if len(rowlist) != 0:

                key = rowlist[key_index]
                dictionary[key] = rowlist
    # Return the compound list.
    return dictionary

if __name__ == '__main__':
    main()
