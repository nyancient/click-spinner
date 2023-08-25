import itertools

__bar = ['-', '/', '|', '\\']
bar_counter_clockwise = itertools.cycle(__bar)
bar_clockwise = itertools.cycle(reversed(__bar))

__arrows = ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙']
arrows_clockwise = itertools.cycle(__arrows)
arrows_counter_clockwise = itertools.cycle(reversed(__arrows))

__dot = ['⠁', '⠂', '⠄', '⡀', '⢀', '⠠', '⠐', '⠈']
dot_clockwise = itertools.cycle(reversed(__dot))
dot_counter_clockwise = itertools.cycle(__dot)

__snake = ['⣆', '⡇', '⠏', '⠛', '⠹', '⢸', '⣰', '⣤']
snake_clockwise = itertools.cycle(__snake)
snake_counter_clockwise = itertools.cycle(reversed(__snake))
