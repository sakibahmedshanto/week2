def move_rover(instructions, grid_size):
    x, y = 0, 0
    directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    current_direction = 'N'

    for instruction in instructions:
        if instruction == 'L':
            if current_direction == 'N':
                current_direction = 'W'
            elif current_direction == 'W':
                current_direction = 'S'
            elif current_direction == 'S':
                current_direction = 'E'
            elif current_direction == 'E':
                current_direction = 'N'
        elif instruction == 'R':
            if current_direction == 'N':
                current_direction = 'E'
            elif current_direction == 'E':
                current_direction = 'S'
            elif current_direction == 'S':
                current_direction = 'W'
            elif current_direction == 'W':
                current_direction = 'N'
        elif instruction == 'M':
            dx, dy = directions[current_direction]
            x = max(0, min(x + dx, grid_size[0] - 1))
            y = max(0, min(y + dy, grid_size[1] - 1))

    return x, y, current_direction

# Example usage:
instructions = "MMRMMRMM"
grid_size = (5, 5)
result = move_rover(instructions, grid_size)
print(result)  # Output: (2, 0, 'S')
