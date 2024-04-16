from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton, QRadioButton, QLabel
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        #все строки надо создать при создании объекта, они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []

#Вопросы
question_list.append(Question('Сколько вы потеряли, не разместив у меня свою рекламу?', 'ДОФИГА', 'Ничего', 'Мало', 'Много'))
question_list.append(Question('Сколько ног у медведя?', '4', '31', '3', '5'))
question_list.append(Question('Кто звал Игоря в Уральских пельменях?', 'Андрей Рожков', 'Вечяслав Мясников', 'Дмитрий Брекоткин', 'Александр Попов'))

def show_question():
    #Показать панель вопросов
    btGroup.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    #Сбросить радио кнопки
    #btGroup.setExclusive()
    btn_1.setChecked(False)
    btn_2.setChecked(False)
    btn_3.setChecked(False)
    btn_4.setChecked(False)

def ask(q: Question):
    #Функция записывает значения вопроса и ответов в соотвествующие виджеты
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_result():
    #Показать панель ответов
    btGroup.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_corerct(res):
    #Установим переданный текст в надпись результат
    lb_result.setText(res)
    show_result()

def check_answer():
    #Если выбран какой-то из вариантов ответов, то надо проверить и показать панель ответов
    if answers[0].isChecked():
        #Правильный ответ
        show_corerct('Праильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            #Неправильный ответ
            show_corerct('Неверно')

def next_question():
    #Задает случайный вопрос из списка
    # нужна перемення хранящая номер текущего вопроса
    # Эту переменную можно буде сделать свойством глобального объекта(app / window)
    window.cur_question = window.cur_question + 1 # переход к селдующему вопросу
    if window.cur_question >= len(question_list):
        window.cur_question = 0 # Если список закончился, идем сначала.
    q = question_list[window.cur_question] # Берем вопрос
    ask(q) #спрашиваем

def click_Ok():
    #Определяет надо ли поакзывать другой вопрос или проверять ответ на этот
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        #Следующий вариант ответа
        next_question()
    

app = QApplication([])
window = QWidget()
window.setWindowTitle('Здесь могла быть ваша реклама!!!')
window.setGeometry(20, 20, 400, 200)
screenGeo = window.frameGeometry()

#Автоматическое Центрирование
windowCenter = QDesktopWidget().availableGeometry().center()
screenGeo.moveCenter(windowCenter)
window.move(screenGeo.topLeft())

#Главная направляющая
main_ln = QVBoxLayout()

#Кнопка ответа
btn_OK = QPushButton('Ответить')
ln_btn_OK = QHBoxLayout()

#Текст вопроса
text = QLabel('Когда была основана Москва?')
   
ln_text = QHBoxLayout()

#Группа кнопок и кнопки с ответами
btGroup = QGroupBox('Варианты ответов:')
ln_btGroup = QHBoxLayout()

ln_ans_V = QVBoxLayout()
ln_ans_H = QHBoxLayout()
ln_ans_H2 = QHBoxLayout()

btn_1 = QRadioButton('987')
btn_2 = QRadioButton('1254')
btn_3 = QRadioButton('1147')
btn_4 = QRadioButton('1154')

ln_ans_H.addWidget(btn_1)
ln_ans_H.addWidget(btn_2)
ln_ans_H2.addWidget(btn_3)
ln_ans_H2.addWidget(btn_4)

ln_ans_V.addLayout(ln_ans_H)
ln_ans_V.addLayout(ln_ans_H2)

btGroup.setLayout(ln_ans_V)

#Список с кнопками для ответа
answers = [btn_1, btn_2, btn_3, btn_4]

#Группа ответов
AnsGroupBox = QGroupBox('')
lb_result = QLabel('')
lb_correct = QLabel('')

ln_res = QVBoxLayout()
ln_res.addWidget(lb_result, alignment=Qt.AlignLeft | Qt.AlignTop)
ln_res.addWidget(lb_correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(ln_res)

#Размещение на направляющих
ln_text.addWidget(text, alignment = Qt.AlignHCenter | Qt.AlignVCenter)
ln_btGroup.addWidget(btGroup)
ln_btGroup.addWidget(AnsGroupBox)
AnsGroupBox.hide()
ln_btn_OK.addWidget(btn_OK)

main_ln.addLayout(ln_text)
main_ln.addLayout(ln_btGroup)
main_ln.addLayout(ln_btn_OK)

window.setLayout(main_ln)

window.cur_question = -1
btn_OK.clicked.connect(click_Ok)

window.show()
app.exec_()