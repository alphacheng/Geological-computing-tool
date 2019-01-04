import random


def create_data():
    with open('./input/input_data.txt', 'w') as f:
        for i in range(0, 100):
            f.write(str(i*(-1)))
            f.write(' ' + str(random.uniform(0, 100)*(-1)) + '\n')


if __name__ == '__main__':
    create_data()
