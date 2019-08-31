# Print a triangle consisting of * characters

triangle_side = int(input("Height? "))
to_print = '*'

for number in range(triangle_side):
    print((to_print * number).rjust(triangle_side - 1) + to_print + (to_print * number).ljust(triangle_side - 1))