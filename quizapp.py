import tkinter as tk
import random

# Classe do Quiz
class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Quiz')
        self.master.geometry('450x500')

        self.score = 0
        self.question_index = 0

        # Perguntas e respostas
        self.questions_answers = [
            ('Qual é a capital do Brasil?', ['Rio de Janeiro', 'Brasília', 'São Paulo', 'Belo Horizonte'], 'Brasília'),
            ('Qual é o maior planeta do Sistema Solar?', ['Terra', 'Marte', 'Júpiter', 'Vênus'], 'Júpiter'),
            ('Quem pintou a Mona Lisa?', ['Vincent van Gogh', 'Leonardo da Vinci', 'Pablo Picasso', 'Michelangelo'], 'Leonardo da Vinci'),
            ('Quem é o maior campeão do mundo de futebol?', ['França', 'Italia', 'Brasil', 'Alemanha'], 'Brasil')
        ]

        # Label das perguntas
        self.question_label = tk.Label(self.master, text=self.questions_answers[self.question_index][0], font=('Arial', 18), pady=10)
        self.question_label.pack()

        # Criação dos botões
        self.option_buttons = []
        for option in self.questions_answers[self.question_index][1]:
            button = tk.Button(self.master, text=option, font=('Arial', 14), bg='white', command=lambda index=self.questions_answers[self.question_index][1].index(option): self.check_answer(index))
            button.pack(pady=5, ipadx=5, ipady=5, fill='x')
            self.option_buttons.append(button)

        self.result_label = tk.Label(self.master, text='', font=('Arial', 14))
        self.result_label.pack(pady=10)

        # Label da pontuação
        self.score_label = tk.Label(self.master, text='Score: {}'.format(self.score), font=('Arial', 14))
        self.score_label.pack(pady=10)

        # Botão para passar para a proxima pergunta
        self.next_button = tk.Button(self.master, text='Próxima pergunta', font=('Arial', 14), bg='white', command=self.next_question)
        self.next_button.pack(pady=10, ipadx=5, ipady=5)

    # Função para passa para a proxima pergunta
    def next_question(self):
        self.question_index = (self.question_index + 1) % len(self.questions_answers)
        if self.question_index == 0: # verifica se é a última pergunta
            self.show_score()
            return
        self.question_label.config(text=self.questions_answers[self.question_index][0])
        for i, option in enumerate(self.questions_answers[self.question_index][1]):
            self.option_buttons[i].config(text=option)
        self.result_label.config(text='')
        self.next_button.config(state='disabled')

    # Função para mostrar o placar final
    def show_score(self):
        self.question_label.config(text='Seu placar final é: {} de {}'.format(self.score, len(self.questions_answers)))
        for button in self.option_buttons:
            button.destroy() # remove todos os botões de opções
        self.result_label.config(text='')
        self.next_button.config(text='Sair', command=self.master.quit) # altera o texto e comando do botão 'Próxima pergunta'

    # Função para verificação da resposta
    def check_answer(self, index):
        user_answer = self.option_buttons[index]['text']
        correct_answer = self.questions_answers[self.question_index][2]
        if user_answer == correct_answer:
            self.score += 1
            self.result_label.config(text='Correto!', fg='green')
        else:
            self.result_label.config(text='Errado! A resposta correta é {}.'.format(correct_answer), fg='red')
        self.update_score_label()
        self.next_button.config(state='normal')

    # Autualiza a label do placar
    def update_score_label(self):
        self.score_label.config(text='Score: {}'.format(self.score))

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
