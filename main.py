import random

def generate_random_number():
    """
    Generates a random number between 1 and 100
    """
    return random.randint(1, 100)

if __name__ == '__main__':
    number = generate_random_number()
    print(f'Random number: {number}')
