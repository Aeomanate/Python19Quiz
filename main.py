import os
from typing import Dict, Any
import Common
import Hints


class Options:
    def __init__(self, opts: Dict[str, Any], default_prompt='Enter your option number: '):
        self.opts = opts
        self.default_prompt = default_prompt

    def get_user_choice(self):
        print(*(f'{i}. {desc}' for i, desc in enumerate(self.opts.keys())), sep='\n')
        user_choice = int(input(self.default_prompt))

        return next(filter(
            lambda i_key: i_key[0] == user_choice,
            enumerate(self.opts.values())
        ))[1]

    def __getitem__(self, item):
        return self.opts[item]


def import_games():
    games: Dict[str, Any] = {}
    for game in os.listdir('Games'):
        with open(f'Games/{game}', 'r', encoding='utf-8') as f:
            game_desc = f.readline().strip('#').strip()
            games[game_desc] = os.path.abspath(f'Games/{game}')
    return games


def read(file):
    return open(file, 'r', encoding='utf-8').read()


def show_hints():
    print(*[f'3+{i}. {Common.decode(hint)}' for i, hint in enumerate(Hints.encoded)], sep='\n')


def main():
    programs = Options({
        'Quit': 'Quit.py'
    })

    programs.opts.update(import_games())

    do = Options({
        'Encode': Common.encode,
        'Show hints': show_hints,
        'Run': lambda file: exec(read(file)),
    })

    while True:
        chosen_action = do.get_user_choice()
        if chosen_action != show_hints:
            print(f'Result: \n{chosen_action(programs.get_user_choice())}\n')
        else:
            chosen_action()


if __name__ == '__main__':
    main()
