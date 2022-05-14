#This program asks a user for two integers a and b and performs the following operations:

int_a = int(input("Enter a: "))
int_b = int(input("Enter b: "))
print(f"{int_a} in binary: {bin(int_a)}")
print(f"{int_b} in binary: {bin(int_b)}")
not_a = ~int_a
a_and_b = int_a & int_b
a_or_b = int_a | int_b
binary_a_or_b = bin(a_or_b)
sliced_a_or_b = binary_a_or_b[2:]
a_exclusive_or_b = int_a ^ int_b
shift_exclusive = a_exclusive_or_b << 3
print(f"(NOT {int_a}) in binary {bin(not_a)}")
print(f"({int_a} AND {int_b}) in binary {bin(a_and_b)}")
print(f"({int_a} OR {int_b}) in binary (without prefix) {sliced_a_or_b}")
print(f"({int_a} XOR {int_b}) shifted left by 3 positions in binary {bin(shift_exclusive)}")
