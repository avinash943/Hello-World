# fibonacci.py
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

if __name__ == "__main__":
    try:
        count = int(input("Enter how many Fibonacci numbers to generate: "))
        fibonacci(count)
    except ValueError:
        print("Please enter a valid number.")