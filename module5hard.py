import time


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users=[], videos=[], current_user: User = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname: str, password: str):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):  # Пользователь найден
                self.current_user = i
                break
            if i == self.users[-1]:
                print("Пользователь не найден")

    def register(self, nickname: str, password: str, age: int):
        for i in self.users:
            if i.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        self.users.append(User(nickname, password, age))
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args: Video):
        for i in args:
            is_valid = True
            for j in self.videos:
                if i.title == j.title:
                    is_valid = False
            if is_valid:
                self.videos.append(i)

    def get_videos(self, search_word: str):
        found_videos = []
        for i in self.videos:
            if search_word.lower() in i.title.lower():
                found_videos.append(i.title)
        return found_videos

    def watch_video(self, title: str):
        if self.current_user:
            for i in self.videos:
                if i.title == title:
                    if (i.adult_mode and self.current_user.age > 17) or i.adult_mode == False:
                        while i.time_now < i.duration:  # Воспроизведение видео
                            time.sleep(1)
                            i.time_now += 1
                            print(i.time_now, end=' ')
                        print("Конец видео")
                        i.time_now = 0
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


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
