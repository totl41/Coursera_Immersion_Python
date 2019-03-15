import sys

print(f"int args: '{sys.argv}'")

if len(sys.argv) < 2:
    sys.exit('Введена пустая строка')

sum_digits: int =0

for list_item in sys.argv[1]:
    sum_digits = sum_digits + int(list_item)

print(sum_digits)