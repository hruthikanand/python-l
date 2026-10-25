
def to_8bit_binary(num):
    """Convert a signed integer to 8-bit 2's complement."""
    return format(num & 0xFF, '08b')


def signed_value(binary):
    """Convert 8-bit 2's complement to a signed decimal."""
    value = int(binary, 2)
    if value & 0x80:
        value -= 256
    return value


def binary_arithmetic(a, b, operation):
    print(f"\nExpression: ({a}) {operation} ({b})")

    if operation == '-':
        second_operand = -b
    else:
        second_operand = b

    binary_a = to_8bit_binary(a)
    binary_b = to_8bit_binary(second_operand)

    print("First operand  :", binary_a)
    print("Second operand :", binary_b)

    result = (int(binary_a, 2) + int(binary_b, 2))
    result_8bit = result & 0xFF
    binary_result = format(result_8bit, '08b')
    decimal_result = signed_value(binary_result)

    
    mathematical_result = a - b if operation == '-' else a + b
    overflow = not (-128 <= mathematical_result <= 127)

    print("Binary addition:", binary_a, "+", binary_b)
    print("Result (binary):", binary_result)
    print("Result (decimal):", decimal_result)
    print("Expected decimal:", mathematical_result)
    print("Overflow:", "Yes" if overflow else "No")
    print("Verification:",
          "Correct" if decimal_result == mathematical_result
          and not overflow else
          "Overflow / mismatch")


# (a) 45 - (+19)
binary_arithmetic(45, 19, '-')

# (b) (-35) - (-12)
binary_arithmetic(-35, -12, '-')
