import pickle

from task import Task
from settings import check_hash


def create_task():
    task = Task('my_safe_task', 'jump')
    pickle_data = pickle.dumps(task)
    pickle_hash = check_hash(pickle_data)
    with open('safe_task.pkl', mode='wb') as f:
        f.write(pickle_hash)
        f.write(pickle_data)


if __name__ == '__main__':
    create_task()
