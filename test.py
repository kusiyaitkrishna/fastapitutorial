# demonstate function with return for calculate sum of 10 number from list



def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num

    return total

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = calculate_sum(numbers)
print("The sum of the numbers is:", result)

# generator function to yield squares of numbers from 1 to n
def generate_squares(n):
    for i in range(1, n + 1):
        yield i * i

# Example usage
n = 10
squares_generator = generate_squares(n)
print(f"The squares of numbers from 1 to {n} are:")
for square in squares_generator:
    print(square)