from MainMenu import MainMenu


class UserDataBase:

    @classmethod
    def create(cls, username, score, window):
        cls.username = username
        cls.score = score
        MainMenu.create(window)
