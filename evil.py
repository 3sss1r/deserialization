import pickle

from task import Task


def create_evil_task():
    task = Task('my_task', 'jump')

    with open('task.pkl', mode='wb') as f:
        pickle.dump(task, file=f)


if __name__ == '__main__':
    create_evil_task()
