from utils import greet, add_numbers

def main():
    name = input("Your name: ")
    print(greet(name))

    print("Let's do a simple calculation.")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The sum is: {add_numbers(a, b)}")

if __name__ == "__main__":
    main()

