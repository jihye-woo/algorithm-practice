# beakjoon1076

from sys import stdin

def solution_BJ1076():
    color_dict = {"black": 0,
                  "brown": 1,
                  "red": 2,
                  "orange": 3,
                  "yellow": 4,
                  "green": 5,
                  "blue": 6,
                  "violet": 7,
                  "grey": 8,
                  "white": 9
                  }

    colors = [stdin.readline().strip() for i in range(3)]

    resistance_val = (color_dict[colors[0]] * 10 + color_dict[colors[1]])
    multiply_val = 10 ** color_dict[colors[2]]
    print(resistance_val * multiply_val)

solution_BJ1076()