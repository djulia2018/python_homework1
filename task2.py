# Задача 2
# Заданы размеры прямоугольного отверстия hole_x, hole_y и размеры кубика с гранью cube_x
# Пройдет ли кубик через прямоугольное отверстие?

hole_x,hole_y = 8,9
cube_x = 11

# cube_x = 6
# cube_x = 3
# cube_x = 10
# cube_x = 5
# cube_x = 9
# cube_x = 8

# Раскомментируйте нужную строку

if cube_x <= hole_x and cube_x <= hole_y:
    print(f'Кубик с гранью {cube_x} пройдет через прямоугольное отверстие со сторонами {hole_x} и {hole_y}')
else:
    print(f'Кубик с гранью {cube_x} не пройдет через прямоугольное отверстие со сторонами {hole_x} и {hole_y}')