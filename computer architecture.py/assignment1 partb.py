
def rotate_left_without_carry(binary, positions):
    print("\nRotate Left Without Carry (ROL)")
    print("Original binary:", binary)

    result = binary

    for i in range(positions):
        msb = result[0]
        result = result[1:] + msb
        print(f"After rotation {i + 1}: {result}")

    print("Final result:", result)


def rotate_left_with_carry(binary, positions, carry=0):
    print("\nRotate Left With Carry (RCL)")
    print("Original binary:", binary)
    print("Initial carry:", carry)

    result = binary

    for i in range(positions):
        msb = int(result[0])
        result = result[1:] + str(carry)
        carry = msb

        print(f"After rotation {i + 1}: {result}, Carry = {carry}")

    print("Final result:", result)
    print("Final carry:", carry)


binary = "10110110"

rotate_left_without_carry(binary, 2)


rotate_left_with_carry(binary, 2, 0)
