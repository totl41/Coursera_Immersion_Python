import sys

print(f"int arg: {'sys.argv'}")

if len(sys.argv) < 2:
    sys.exit("Введена пустая строка")

if not sys.argv[1].isdigit():
    sys.exit("В качестве аргумента, могут быть, только цыфры")

number_of_steps = int(sys.argv[1])

if number_of_steps == 0:
    sys.exit("Количество ступенек = 0")

number_of_steps = number_of_steps + 1

add_space = " "
add_lattice = "#"
step_ladder = ""

for counter_spac in range(number_of_steps):

    step_ladder = (add_space * (number_of_steps - counter_spac)) + (add_lattice * counter_spac)

    print(step_ladder)


