import random


class gameBagels:
    def __init__(self):
        self.NUM_DIGITS = 3
        self.MAX_GUESSES = 10

    def play(self):
        print('''           Bagels
            I am thinking of a {}-digit number with no repeated digits.
            Try to guess what it is. Here are some clues:
            When I say:     That means:
            Catch        One digit is correct and in the right position.
            Flose        One digit is correct but in the wrong position.
            Bagels       No digit is correct.
            '''.format(self.NUM_DIGITS))

        while True:
            secret_num = self.get_secret_num()
            print('I have a number in my head.')
            print('You have {} guesses to get it.'.format(self.MAX_GUESSES))

            num_guesses = 1
            while num_guesses <= self.MAX_GUESSES:
                guess = ''
                while len(guess) != self.NUM_DIGITS or not guess.isdecimal():
                    print('Guess #{}: '.format(num_guesses))
                    guess = input('> ')

                clues = self.get_clues(guess, secret_num)
                print(clues)

                if guess == secret_num:
                    print('You got it!')
                    break
                
                num_guesses += 1
                if num_guesses > self.MAX_GUESSES:
                    print('Sorry! You have run out of guesses.')
                    print('The answer was {}.'.format(secret_num))

            play_again = input('Play again?(yes or no) ')
            if not play_again.lower().startswith('y'):
                break

        print('Thanks for playing!')

    def get_secret_num(self):
        """
        Returns a string of unique random digits
        """
        numbers = list('0123456789')
        random.shuffle(numbers)
        secret_num = ''
        for i in range(self.NUM_DIGITS):
            secret_num += str(numbers[i])
        return secret_num

    def get_clues(self, guess, secret_num):
        """Returns a string with Match, Close and Bagels for a guess """
        if guess == secret_num:
            return 'You got it!'

        clues = []
        for i in range(len(guess)):
            if guess[i] == secret_num[i]:
                clues.append('Catch')
            elif guess[i] in secret_num:
                clues.append('Flose')

        if len(clues) == 0:
            return 'Bagels'
        else:
            clues.sort()
            return ' '.join(clues)

