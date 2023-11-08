with open('words.txt') as file:
    words = file.read().split('\n')

freq_list = {}

for i in range(97, 123):
    letter = chr(i)
    total = 0
    for word in words:
        total += word.count(letter)
    freq_list[letter] = total


def filtered(words, filter, word):

    for b in range(5):
        temp_words = words.copy()
        words = []

        if filter[b] == 'g':
            for i in range(len(temp_words)):
                if temp_words[i][b] == word[b]:
                    words.append(temp_words[i])

        elif filter[b] == 'y':
            for i in range(len(temp_words)):
                if temp_words[i][b] != word[b] and word[b] in temp_words[i]:
                    words.append(temp_words[i])

        else:
            for i in range(len(temp_words)):
                if not word[b] in temp_words[i]:
                    words.append(temp_words[i])

    return words


def best_word(words):

    if len(words) != 1:

        highest = [['', 0], ['', 0]]

        for c in words:

            duplicate = False
            letters = []
            for letter in c:
                if letter in letters:
                    duplicate = True
                letters.append(letter)

            if duplicate:
                total = 0
                for letter in c:
                    total += freq_list[letter]
                if total > highest[1][1]:
                    highest[1] = [c, total]

            else:
                total = 0
                for letter in c:
                    total += freq_list[letter]
                if total > highest[0][1]:
                    highest[0] = [c, total]

        if highest[0][0]:
            return highest[0][0]
        print('there are repeating letters')
        return highest[1][0]

    print('Last possible option')
    return words[0]

def random_best_words(words, filter, word):

    position = filter.index('n')

    letters = []
    for a in words:
        letters.append(a[position])

    with open('words.txt') as file:
        new_words = file.read().split('\n')

    while True:

        if len(letters) != 1:

            highest = ['', 0]
            for b in new_words:
                count = 0
                for c in letters:
                    if c in b:
                        count += 1
                if count > highest[1]:
                    highest = [b, count]

            print('Since there are many options')
            print(letters)
            print('Test word is', highest[0])

            filter = list(input('Enter result: '))
            print()

            if 'g' in filter and filter[position] == 'g':
                new_word = ''
                for i in range(5):
                    if i == position:
                        new_word += highest[0][position]
                    else:
                        new_word += word[i]

                letters.remove(highest[0][position])
                print('Test word is', new_word)
                filter = list(input('Enter result: '))
                break

            elif 'y' in filter:

                for a in range(5):
                    if filter[a] == 'y' and highest[0][a] in letters:
                        new_word = ''
                        for i in range(5):
                            if i == position:
                                new_word += highest[0][a]
                            else:
                                new_word += word[i]

                        letters.remove(highest[0][a])
                        print('Test word is', new_word)
                        filter = list(input('Enter result: '))
                        break
                else:
                    for i in highest[0]:
                        if i in letters:
                            letters.remove(i)

            else:
                for i in highest[0]:
                    if i in letters:
                        letters.remove(i)

            print()

        else:
            print('Last possible option')
            new_word = ''
            for i in range(5):
                if i == position:
                    new_word += letters[0]
                else:
                    new_word += word[i]
            print('Test word is', new_word)
            filter = list(input('Enter result: '))

prev = []

while True:

    word = best_word(words)
    print('Possible words remaining:', len(words))
    print('Test word is', word)

    filter = input('Enter result: ')
    print()

    if filter == 'left':
        print(words)

    elif filter == 'next':
        words.remove(word)
        word, filter = prev

    elif len(filter) == 5 and filter.replace('y', '').replace('n', '').replace('g', '') == '':

        filter = list(filter)

        if filter.count('g') == 4:
            prev = [word, filter]
            words = filtered(words, filter, word)
            random_best_words(words, filter, word)

        prev = [word, filter]
        words = filtered(words, filter, word)

    else:
        print('Invalid answer')