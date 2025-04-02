from base64 import b64encode, b64decode
from typing import Dict, Any


class Options:
    def __init__(self, opts: Dict[str, Any], default_prompt="Enter your option number: "):
        self.opts = opts
        self.default_prompt = default_prompt

    def get_user_choice(self):
        print(*(f"{i}. {desc}" for i, desc in enumerate(self.opts.keys())), sep='\n')
        user_choice = int(input(self.default_prompt))

        return next(filter(
            lambda i_key: i_key[0] == user_choice,
            enumerate(self.opts.values())
        ))[1]

    def __getitem__(self, item):
        return self.opts[item]


def main():
    programs = Options({
        'Quit': 'Quit.py',
        'A less or greater game': 'LessGreater.py',
    })

    do = Options({
        'Read': lambda file: open(file, 'r', encoding='utf-8').read(),
        'Encode': lambda file: b64encode(bytes(do["Read"](file), encoding='utf-8')),
        'Decode': lambda file: b64decode(do["Encode"](file)).decode('utf-8'),
        'Run': lambda file: exec(do["Read"](file)),
    })

    while True:
        print(f"Result: \n{do.get_user_choice()(programs.get_user_choice())}\n")


if __name__ == '__main__':
    main()
