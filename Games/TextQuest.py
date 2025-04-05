# Text quest
import random
from copy import deepcopy
from typing import Union

from Common import decode
from Hints import encoded


class Option:
    def __init__(self):
        self._title = None  # Enter to the Option
        self._text = None  # Option story
        self._back = None
        self._special_answer = None
        self._options: list = list()
        self._raise_option = None
        self._is_make_deepcopy = False

    def __eq__(self, other):
        return self._title == other._title and self._text == other._text

    def is_deepcopy_needed(self):
        return self._is_make_deepcopy

    def set_options(self, options=None):
        self._options = options or list()
        if self._back:
            self._options.append(self._back)
        return self

    def __str__(self):
        return self._title

    def show(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self._text)
        print(*(f'{i + 1}. {opt}' for i, opt in enumerate(self._options)), sep='\n')

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
                print(f'Введи число от 1 до {len(self._options)}!')
            return None

    def handle_input(self):
        while True:
            entered = input("Твой ответ: ")
            number = self.try_interpret_as_integer(entered)

            if isinstance(number, int):
                selected_option = self._options[number - 1]
                return selected_option if not selected_option.is_deepcopy_needed() else deepcopy(selected_option)
            elif entered.lower() == self._special_answer.lower():
                selected_option = self._raise_option
                return selected_option if not selected_option.is_deepcopy_needed() else deepcopy(selected_option)
            else:
                print(self.get_random_mistake())
                return None

    def handle_player(self, player_stat):
        pass


class RegularOption(Option):
    def __init__(self,
                 title: str,
                 text: str,
                 options=None,
                 special_answer=None,
                 raise_option=None,
                 back: Union[None, str, Option] = 'Default'):
        super().__init__()
        self._title = title
        self._text = text
        self._back = None if not back else (
            BackRequest() if isinstance(back, str) else back
        )
        self._special_answer = special_answer
        self._raise_option = raise_option
        self.set_options(options)


class NextStage(RegularOption):
    pass


class DropStage(RegularOption):
    @staticmethod
    def get_random_dead_msg():
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

    def __init__(self, title=None):
        super().__init__(title or DropStage.get_random_dead_msg(),
                         'Это техническая строка, как ты её увидела?!')


class BackRequest(RegularOption):
    def __init__(self):
        super().__init__('Назад', '', back=None)


class Engine:
    def __init__(self):
        self.history_stack = list()
        self.player_stat = dict()

    def run(self, start_option: Option):
        self.history_stack.append(start_option)

        while True:
            self.history_stack[-1].handle_player(self.player_stat)
            self.history_stack[-1].show()
            try:
                new_state = self.history_stack[-1].handle_input()

                if new_state is None:
                    continue

                if isinstance(new_state, NextStage):
                    self.history_stack = [new_state]
                elif isinstance(new_state, DropStage):
                    self.history_stack = self.history_stack[:1]
                elif isinstance(new_state, BackRequest):
                    self.history_stack.pop()
                elif new_state != self.history_stack[-1]:
                    self.history_stack.append(new_state)

            except Exception as e:
                print(f'Что-то пошло не так... Откат, откат! {e}')


def getLocation0():
    wait_morning = RegularOption(
        title='Спать до рассвета',
        text='Внезапно пробудившись, ты понимаешь, что оказалась под водой. '
             'И без кислорода ты быстро умираешь. ',
        back=DropStage()
    )

    force_wake_up = RegularOption(
        title='Проснуться',
        text='Ночь. Частью сонного сознания ты понимаешь, что что-то не так...',
        special_answer='проверить кран Маевского',  # TODO: Записка сделана
        options=[
            wait_morning
        ],
        back=None,
        raise_option=getLocation1()
    )

    start = RegularOption(
        title='0. Начало',
        text=f'Тебе что-то снится... Что-то мокрое и горячее...\n'
             f'В твоей голове всплывают слова: {decode(encoded[0])}'
             f'\rЧто бы они могли значить?..',
        back=None,
        options=[
            force_wake_up,
            wait_morning
        ]
    )

    return start


class ShortsOption(RegularOption):
    def __init__(self, title, text):
        super().__init__(title, text, options=[self])
        self.watch_counter = 1
        self.text_template = text
        self.end_text_template = ('Прошёл весь день, а ты так и не поела, залипая в шортсах.\n'
                                  'К сожалению, сегодня был не тот день,\n'
                                  'когда твой организм мог попустительски отнестись к голодовке.\n'
                                  'Ты умерла.')
        self._is_make_deepcopy = True

    def handle_player(self, player):
        if self.watch_counter > 1:
            self._is_make_deepcopy = False

        if 0 <= self.watch_counter <= 10:
            self._text = self.text_template.format(ShortsOption.gen_shorts_description())
        if self.watch_counter == 5:
            self._back = None
            self.set_options([self])
        if self.watch_counter == 11:
            self._text = self.end_text_template
            self._back = DropStage(
                'Умереть от голода'
            )
            self.set_options()

    def show(self):
        super().show()
        self.watch_counter += 1

    @staticmethod
    def gen_shorts_description():
        return random.choice([
            'Забавный котик пьёт воду',
            'Злой профессионал обозревает плохой ремонт чьего-то дома',
            'Парень сделал предложение на крыше небоскрёба',
            'Девушка делает макияж с закрытыми глазами',
            'Повар готовит ужин вслепую — и это шедевр',
            'Реакция отца на первый шаг ребёнка',
            'Трюки с бутылками — невозможно повторить!',
            'Как звучат языки мира, если читать одно и то же слово',
            'Реакция учителя на подарок от класса',
            'Геймер проигрывает на последних секундах — больно смотреть',
            'Трансформация комнаты до и после ремонта',
            'Угадай песню по одной ноте — челлендж',
            'Как рисовать аниме-глаз за 30 секунд',
            'Собака научилась говорить с помощью кнопок',
            'Девушка впервые пробует острые корейские лапши',
            'Парень превращает обычную доску в произведение искусства',
            'Невероятный лайфхак с фольгой, о котором ты не знал',
            'Кошка злится, потому что ей не дали пиццу',
            'Парень играет 20 ролей в одном видео',
            'Детская реакция на лимон — умора!',
            'Нарисовал Мону Лизу… в Minecraft!',
            'Как выглядел бы Гарри Поттер, если бы его снимали в 2025 году',
            'Разблокировал старый айфон, найденный в реке',
            'Парень воссоздаёт известные фильмы дома',
            'Реакция мамы на первый клип сына',
            'Секретные функции iPhone, о которых ты не знал',
            'Девушка пробует еду из разных стран — выпуск 1',
            'Как звучит голос под водой — удивительно!',
            'Танец, который захватил весь TikTok',
            'Сравнение еды из ресторана и дома — разница шокирует',
            'Реакция кота на новый аквариум',
            'Парень делает костюм Железного человека своими руками',
            'Как приготовить суши за 30 секунд — магия!',
            'Девочка поёт, как взрослая — мурашки!',
            'Парень играет на пианино, но... клавиш нет!',
            'История любви в одном шорте',
            'Самая неловкая ситуация на свидании',
            'Секретный рецепт бабушки раскрыт!',
            'Парень стал невидимым (или почти)',
            'Что произойдёт, если не спать 48 часов?',
            'Момент, когда он понял, что влюбился',
            'Как выглядел бы Instagram в 90-х',
            'Реальные звуки космоса — страшно и красиво',
            'Что если бы люди были как симсы?',
            'Девочка станцевала лучше всех взрослых',
            'Собака спасла хозяина — всё на видео!',
            'Трюк с картой, который обманет твой мозг',
            'Как сделать меч из бумаги — круто и просто',
            'Парень потерял голос, но всё равно поёт',
            'Отец делает завтрак под музыку Баха',
            'Кот реагирует на видеозвонок — это надо видеть',
            'Кот увидел себя в зеркале и испугался',
            'Мальчик исполняет трюк на скейтборде впервые',
            'Как звучит айсберг, когда он трескается — дико!',
            'Слепой тест: газировка или вода?',
            'Девушка прошла 10 км в туфлях — вот что случилось',
            'Парень пытался быть веганом неделю — результат',
            'Пёс учит ребёнка ходить',
            'Разговор двух попугаев — как будто люди!',
            'Что будет, если добавить Mentos в сок',
            'Превратил старую куртку в модный жилет',
            'Провёл день как персонаж GTA',
            'Попробовал самые острые чипсы мира',
            'Обратная съёмка готовки — выглядит как магия',
            'Танцует на крыше машины — закончилось не так, как думал',
            'Момент, когда учитель понял, что ошибся',
            'Кто лучше поёт — человек или кот?',
            'Парень открыл банку одним пальцем',
            'Пробую все позиции меню за 1000 рублей',
            'Как звучит твой голос под гелием и под грушей',
            'Угадай песню по эмодзи — челлендж с другом',
            'Сколько пельменей можно съесть за минуту?',
            'Трюк с картами, который взорвёт мозг',
            'Кот впервые увидел огурец',
            'Собака делает массаж своему хозяину',
            'Нарисовал Джокера зубной пастой',
            'Парень играет бит на ложках — круто звучит',
            'Школьник отвечает на вопрос, и учитель в шоке',
            'Как выглядел бы Apple в 80-х',
            'Пробую жить как Гарри Поттер 1 день',
            'Снял кино на смартфон за 0 рублей',
            'Как сделать слайм из 3 ингредиентов',
            'Парень делает саундтрек из звуков кухни',
            'Разобрался с налогами за 30 секунд (почти)',
            'Кот принёс тапки — но это не твои',
            'Что в коробке? Реакция девочки бесценна',
            'Девочка поёт на улице — прохожие замирают',
            'Из картошки сделал... спиннер',
            'Самая странная еда из супермаркета',
            'Маленький ребёнок объясняет, как устроен космос',
            'Попробовал говорить только “мяу” весь день',
            'Кошка реагирует на видео с тигром',
            'Сняли клип за один дубль на парковке',
            'Сделал гигантскую конфету своими руками',
            'Что если не смотреть в экран весь день?',
            'Реакция бабушки на первый VR-шлем',
            'Говорящий попугай ругается как пират',
            'Танец, который делают все в 2025',
            'Девочка объясняет экономику — и всё становится ясно',
            'Как выглядят звуки на песке — гипнотизирует',
            'Этот кот точно был человеком в прошлой жизни',
        ])


def getLocation1():
    stuck_in_shorts = ShortsOption(
        title='Свайпнуть и залипать дальше',
        text='На твоём экране видео: "{}"'
    )

    enter_random_password = RegularOption(
        title='Ввести какой-нибудь пароль',
        text='Ошибка! Неправильный пароль!'
    )

    morning_routine = RegularOption(
        title='Привести себя в порядок и поесть',
        text='Ты бодро направилась в ванную и сделала все свои дела.\n'
             'Приступила к еде. В это время телефон твоего парня запел:'
             + decode(encoded[2]) +
             '\rЧтобы отключить адский звук,\n'
             'тебе нужно вспомнить пароль его телефона'
             '(который он недавно сменил).\n'
             'Какой же теперь он у него?',
        options=[
            enter_random_password
        ],
        back=None,
        special_answer='С новым годом!',  # TODO: Записка сделана!
        raise_option=getLocation2()
    )

    view_shorts = RegularOption(
        title='Смотреть шортсы',
        text='Перед тобой открыт тикток/инста/ютуб/линкедын/чимченын. Что делаем?',
        options=[
            stuck_in_shorts
        ]
    )

    start = NextStage(
        title='1. Утро настало и Лёша задолбал!',
        text='Настало славное лучезарное утро!\n'
             'Ты предотвратила потоп этой ночью и пора начинать этот день!\n'
             'Что скажешь?',
        back=None,
        options=[
            view_shorts,
            morning_routine
        ]
    )

    return start


def getLocation2():
    talk_with_friend = RegularOption(
        title='Поговорить с подругой несколько часов',
        text='Пу-пу-пу. Говоришь с подругой. Пу-пу-пу.',
    )
    talk_with_friend.set_options([talk_with_friend])

    love_rosa = RegularOption(
        title='Приласкать Розу',
        text='Выбрала близкого, а не далёкого. Как романтично! Ах!\n'
             'Но Розы нигде нет. Что же это такое?\n'
             'Из соседней комнаты ты слышишь: '
             + decode(encoded[4]) + '\r' +
             'Прибежав на кухню, ты ничего не поняла, розу не нашла.\n'
             'Так где ж она была?',
        back=None,
        special_answer='На вершине бытия!',  # TODO: Записка сделана
        raise_option=getLocation3()
    )

    start = NextStage(
        title='2. Пора искать розу',
        text='Справившись з порождением ада, перед тобой встал выбор:',
        options=[
            talk_with_friend,

        ],
        back=None
    )

    return start


def getLocation3():
    start = NextStage(

    )

    return start


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


Engine().run(getLocation1())
