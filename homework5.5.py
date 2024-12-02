import time


class User:
    ls_users = []

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        User.ls_users.append(self.nickname)
        User.ls_users.append(self.password)
        User.ls_users.append(self.age)


class Video:
    ls_videos = []

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = User.ls_users
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        if (nickname in self.users and
                self.users[(self.users.index(nickname))+1] == hash(password)):
            self.current_user = nickname
            print(f"Рады вас видеть, {nickname}!")
        else:
            print("Неверный пароль, повторите попытку!")

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            User(nickname, password, age)
            self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for x in args:
            ls = list(x.__dict__.values())
            if ls[0] in self.videos:
                pass
            else:
                for i in ls:
                    self.videos.append(i)

    def get_videos(self, title):
        result = []
        for i in self.videos:
            if not isinstance(i, str):
                continue
            elif title.lower() in i.lower():
                result.append(i)
            else:
                pass
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            if title in self.videos:
                duration = self.videos[(self.videos.index(title)+1)]
                time_now = self.videos[(self.videos.index(title)+2)]
                adult_mode = self.videos[(self.videos.index(title) + 3)]
                current_user_age = self.users[self.users.index(self.current_user)+2]
                if adult_mode == False or (adult_mode == True and current_user_age >= 18):
                    for i in range(time_now+1, duration+1):
                        print(i, end=' ')
                        time.sleep(1)
                    else:
                        print("Конец видео")
                        self.videos[(self.videos.index(title) + 2)] = 0
                else:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
            else:
                pass


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
