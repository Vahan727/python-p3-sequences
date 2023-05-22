#!/usr/bin/env python3

# def print_fibonacci(length):
#     fibonacci_sequence = []
#     if length <= 0:
#         print(fibonacci_sequence)
#     elif length <= 1:
#         fibonacci_sequence = [0]
#         print(fibonacci_sequence)
#     elif length <=2:
#         fibonacci_sequence = [0, 1]
#         print(fibonacci_sequence)
#     else:
#         fibonacci_sequence = [0, 1]
#         for num in range(2, length):
#             fibonacci_sequence.append(fibonacci_sequence[num - 1] + fibonacci_sequence[num - 2])
#         print(fibonacci_sequence)


def print_fibonacci(length):
    fibonacci_sequence = []
    if length > 0:
        fibonacci_sequence.append(0)
        if length > 1:
            fibonacci_sequence.append(1)
            if length > 2:
                for num in range(2, length):
                    fibonacci_sequence.append(fibonacci_sequence[num - 1] + fibonacci_sequence[num - 2])      
    print(fibonacci_sequence)
   
   