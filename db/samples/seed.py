from database import SessionLocal
from models import Task, User

db = SessionLocal()


def seed():
    task_titles = [
        'TEST TASK 1',
        'TEST TASK 2',
        'TEST TASK 3'
    ]
    tasks = [Task(title=title) for title in task_titles]

    user = User(username='testman', email='hogehoge@hoge.jp')
    user.tasks = tasks  # リレーションも丸ごと表現できる

    db.add(user)
    db.commit()


if __name__ == '__main__':
    BOS = '\033[92m'  # 緑色表示用
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()