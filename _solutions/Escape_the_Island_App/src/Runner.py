from GameController import GameController

class Runner:

    def __init__(self):
        self.number_of_games_played = 0
        self.maximum_number_of_days_survived = 0
        self.playing = True

    def play(self):
        # Intro message
        print("Welcome to Escape the Island! A game of survival... Will you succumb to starvation, thirst, or the many dangers of the island, or do you have what it takes to Escape the Island?")
        while(self.playing):
            newGame = GameController()
            newGame.play()
            self.save_max_number_of_days(newGame.days) # Do this later
            self.number_of_games_played += 1
            self.playing = self.ask_to_play_again()
        else:
            print("Thanks for playing Escape the Island!")

    def ask_to_play_again(self):
        while(True):
            play_again = input("Play Again? (Y/N) ")
            if play_again == 'Y':
                return True
            elif play_again == 'N':
                return False
            else:
                print("Inavalid input.\n")

    def save_max_number_of_days(self, days_survived):
        if days_survived > self.maximum_number_of_days_survived:
            self.maximum_number_of_days_survived = days_survived
        print("You have survived a maximum number of "+str(self.maximum_number_of_days_survived)+" days.")
