import random


learning_late = 0.01
loop_max = 1000

def main():
    initial = random.uniform(-10, 10)
    old = initial
    new = 0.0
    for _ in range(1000):
        # 更新
        new = old - learning_late * diff_func(old)

        y = object_func(new)
        print(y)

        old = new

    print(new, y)

def object_func(x):
    return x * x + x

def diff_func(x):
    return 2 * x + 1

if __name__ == '__main__':
    main()