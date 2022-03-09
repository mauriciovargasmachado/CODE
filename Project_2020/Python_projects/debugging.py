def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    while True:
        try:
            num = int(input('Please introduce a number: '))
            if num < 0:
                raise ValueError
            print(divisors(num))
            print("The program has end!!!")
            break
        except ValueError:
            print("you must choose a integer positive number, please!")


if __name__ == '__main__':
    run()