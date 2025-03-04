# Taking user inputs
a = int(input("Enter the first number: "))
operator = input("Enter any operator (+, -, *, /, %, //, **, >, <, ==, !=, >=, <=, &, |, ^, ~, <<, >>, and, or, not): ")
b = int(input("Enter the second number: ")) if operator not in ["~", "not"] else None  # Second number not needed for unary operators

# Performing operations based on the chosen operator
print("\nResult:")
if operator == '+':
    print(f"{a} + {b} = {a + b}")
elif operator == '-':
    print(f"{a} - {b} = {a - b}")
elif operator == '*':
    print(f"{a} * {b} = {a * b}")
elif operator == '/':
    print(f"{a} / {b} = {a / b}" if b != 0 else "Division by zero is not allowed.")
elif operator == '%':
    print(f"{a} % {b} = {a % b}" if b != 0 else "Modulus by zero is not allowed.")
elif operator == '//':
    print(f"{a} // {b} = {a // b}" if b != 0 else "Floor division by zero is not allowed.")
elif operator == '**':
    print(f"{a} ** {b} = {a ** b}")
elif operator == '>':
    print(f"{a} > {b} = {a > b}")
elif operator == '<':
    print(f"{a} < {b} = {a < b}")
elif operator == '==':
    print(f"{a} == {b} = {a == b}")
elif operator == '!=':
    print(f"{a} != {b} = {a != b}")
elif operator == '>=':
    print(f"{a} >= {b} = {a >= b}")
elif operator == '<=':
    print(f"{a} <= {b} = {a <= b}")
elif operator == '&':
    print(f"{a} & {b} = {a & b}")
elif operator == '|':
    print(f"{a} | {b} = {a | b}")
elif operator == '^':
    print(f"{a} ^ {b} = {a ^ b}")
elif operator == '~':
    print(f"~{a} = {~a}")
elif operator == '<<':
    print(f"{a} << {b} = {a << b}")
elif operator == '>>':
    print(f"{a} >> {b} = {a >> b}")
elif operator == 'and':
    print(f"{bool(a)} and {bool(b)} = {bool(a and b)}")
elif operator == 'or':
    print(f"{bool(a)} or {bool(b)} = {bool(a or b)}")
elif operator == 'not':
    print(f"not {bool(a)} = {not bool(a)}")
else:
    print("Invalid operator entered.")
