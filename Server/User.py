

class User:
    user_list = []

    def __init__(self, username, password, score):
        self.username = username
        self.password = password
        self.score = score

        User.user_list.append(self)

    def change_score(self, change):
        self.score += change

    @classmethod
    def user_exist(cls, username):
        for user in User.user_list:
            if user.username == username:
                return True

        return False

    @classmethod
    def login(cls, username, password):
        for user in User.user_list:
            if user.username == username and user.password == password:
                return user

        return None
