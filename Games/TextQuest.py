import random


class Option:
    def __init__(self):
        self._choise_text = None  # Enter to the Option
        self._main_text = None  # Option story
        self._back_object = BackRequest()  #
        self._special_answer = None
        self._options = list()
        self._raise_option = None

    def set_options(self, *options):
        self._options = list(options)
        self._options.append(self._back_object)
        return self

    def __str__(self):
        return self._choise_text

    def show(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self._main_text)
        print(f'{i + 1}. {opt}' for i, opt in enumerate(self._options))

    def get_random_mistake(self):
        return random.choice([
            'Егеге, что тут такое у нас, а? Булщит!',
            'Земля содрогнулась, но не раскололась напополам...',
            'Скелет в углу говорил похожие вещи...',
            'Эхо разнеслось по залу, но никто не понял смысла...',
            'Мудрецы прошлого бы покачали головами...',
            'Как говорится, попытка — не пытка, но это было стильно!',
            'Голоса древних шепчут: "Ну ты даешь..."',
            'Сквозняк донес обрывки фраз... и все они про булщит.',
            'Вселенная замерла в ожидании... и продолжила зевать.',
            'Если бы камни могли смеяться, этот зал был бы самым шумным местом!',
            'Великий Спешл сказал "нет" и удалился в закат. *Наблюдает за тобой*',
            'Задумайся: может, все проще, чем на самом деле?',
            'Ворон на карнизе одобрительно каркнул... но над чем, неизвестно.',
            'В темноте раздался чей-то смешок. Наверное, твой.',
            'Тени на стенах переглянулись, но промолчали.',
            'Кристалл над тобой слегка засветился желтизной',
            'Где-то далеко вздохнул старый зачарователь змей...',
            'Занавеска слегка дрогнула. Но окно возможностей не отворилось.',
            'Этот ответ увековечится в анналах заблуждений!',
            'Легенды сложат о тебе сказание... Но не такое, как хочется.',

            'Стены хранят множество тайн, но этот ответ к ним не относится...',
            'Где-то в параллельной вселенной это, возможно, было бы правильно.',
            'Ты почти взломал матрицу, но что-то пошло не так.',
            'Твои слова отозвались в пустоте... и остались без ответа.',
            'Скрипнула дверь, словно возмущаясь услышанному.',
            'Энциклопедия ошибок пополнилась еще одним примером!',
            'За кулисами кто-то громко шепнул: "Это провал!"',
            'Даже камень в углу слегка покачнулся от недоумения.',
            'Где-то вдали грянул гром. Совпадение? Не думаю.',
            'В этот момент кто-то в мире facepalm’нулся.',
            'Темные силы на мгновение заинтересовались тобой... и разочарованно отвернулись.',
            'Глубоко в лесу филин сказал "ууууу", явно не намекая ни на что.',
            'Тебя бы поняли... но не в этом пространственном измерении...'
        ])

    def try_interpret_as_integer(self, entered: str):
        try:
            entered = int(entered)
            if not (1 <= entered <= len(self._options)):
                raise ValueError
            return entered
        except ValueError:
            if not self._special_answer:
                print(f'Введи число 1 - {len(self._options)}!')
            else:
                print(self.get_random_mistake())
            return None

    def handle_input(self):
        while True:
            entered = input("Твой ответ: ")
            number = self.try_interpret_as_integer(entered)

            if number is int:
                return self._options[number - 1]
            elif entered.lower() == self._special_answer:
                return self._raise_option

    def handle_player(self, player_stat):
        pass


class RegularOption(Option):
    def __init__(self,
                 choice_text: str,
                 main_text: str,
                 special_answer=None,
                 raise_option=None,
                 back_object=None,
                 *options):
        super().__init__()
        self.choice_text = choice_text
        self._main_text = main_text
        if back_object:
            self._back_object = back_object
        self._special_answer = special_answer
        self._raise_option = raise_option
        self.set_options(*options)


class NextStage(RegularOption):
    def __init__(self,
                 choice_text: str,
                 main_text: str,
                 special_answer=None,
                 raise_option=None,
                 back_object=None,
                 *options):
        super().__init__()


class DropStage(Option):
    def get_random_dead_msg(self):
        return random.choice([
                'Ок',
                'My bad',
                'Нечестно!',
                'Какой кошмар...',
                'Какого?!',
                'Ну патимууууу???',
                'Єх...',
                'ЕЩЕ ПОПЬІТКА!',
                'От жеж кабала!',
                'Чтоб тебя!',
                'Ну, Леша, погоди!',
                'Лолшто?',
                'Абракадабра мать вашу!',
                'Йамете кудасаииииииии!',
                'Заново, так заново.',
                'Ну вот опять!',
                'Ну что ж...',
                'А ведь могло быть и хуже...',
                'Ну, бывает...',
                'Да чтоб тебя!',
                'Это законно вообще?',
                'Ну ты понял, да?',
                'Серьезно?!',
                'Опять двадцать пять!',
                'Ну и дела...',
                'Так не считается!',
                'Как же так-то?!',
                'Это все заговор!',
                'Да что ж ты будешь делать!',
                'Ну и ну...',
                'Ладно, не в этот раз...',
                'Ай, ну почему я?!',
                'Ну все, держитесь!',
                'Было весело... недолго.',
                'Вот это поворот!',
                'Ну, начнем сначала!'
            ])

    def __init__(self, decision, main_text):
        super().__init__()
        self._choise_text = decision
        self._main_text = main_text
        self._back_object = tuple()
        self._options = [self.get_random_dead_msg()]


class BackRequest(Option):
    def __str__(self):
        return "Назад"


class Engine:
    def __init__(self):
        self.history_stack = list()
        self.player_stat = dict()

    def run(self, start_option: Option):
        self.history_stack.append(start_option)

        while True:
            self.history_stack[-1].show()
            self.history_stack[-1].handle_player(self.player_stat)
            try:
                new_state = self.history_stack[-1].handle_input()

                if new_state is NextStage:
                    self.history_stack = [new_state]
                if new_state is DropStage:
                    self.history_stack = self.history_stack[1:]
                if new_state is BackRequest:
                    self.history_stack.pop()

            except Exception as e:
                print(f'Что-то пошло не так... Откат, откат! {e}')
                self.history_stack.pop()

def getLocation0():
    pass
def getLocation1():
    pass
def getLocation2():
    pass
def getLocation3():
    pass
def getLocation4():
    pass
def getLocation5():
    pass
def getLocation6():
    pass
def getLocation7():
    pass
def getLocation8():
    pass


