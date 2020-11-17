import pickle
import hmac

from settings import check_hash


def execute_task():
    with open('safe_task.pkl', 'rb') as f:
        hash_creator = f.read(32)
        pickle_data = f.read()

        if hmac.compare_digest(hash_creator, check_hash(pickle_data)):
            task = pickle.loads(pickle_data)
            print(f'Task {task.name} was executed')
            print(f'Result: {task.action}')
        else:
            print('Creator is not confirmed')


if __name__ == '__main__':
    execute_task()
