# A deshuffle sentences game
from Common import decode
from Hints import encoded


def side():
    import random

    sentences = [
        "Я обязательно заработаю много-много денег!",
        "Каждая моя неудача будет шагом на пути к достижению моих целей!",
        "Самообучение может стать действительно увлекательнее, чем когда-либо!"
    ]

    for stage in range(len(sentences)):
        sentence_words = sentences[stage].split(' ')
        shuffled = ' '.join([''.join(random.sample(word, len(word))) for word in sentences[stage].split(' ')])

        full_ans = [''] * len(sentence_words)
        while full_ans != sentence_words:
            if stage > 0:
                print("Next stage!\n")

            if any(full_ans):
                aligning = [' '*len(word) for word in sentence_words]
                aligned = [word if word else align for word, align in zip(full_ans, aligning)]
                print(f'Already known words:     {" ".join(aligned)}')

            print(f'Stage {1+stage}/{len(sentences)}, deshuffle it: {shuffled}')
            ans = input('Your answer: ')

            ans = ans.split(' ')
            for i, word in enumerate(sentence_words):
                if i < len(ans) and i < len(sentence_words) and word.lower() == ans[i].lower():
                    full_ans[i] = word

        print('You\'ve got it!')


side()

