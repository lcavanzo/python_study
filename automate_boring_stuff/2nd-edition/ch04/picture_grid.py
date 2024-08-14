# Picture_grid.
"""
write code that uses it to print the image.
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
"""
grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]

print(f"row = {len(grid)}")
print(f"column = {len(grid[0])}")
print("--------------------------------")

for row in range(len(grid[0])):
    print()
    for column in range(len(grid)):
        # print(f"{column}-{row}", end=" ")  # review what happens if end is changed to ""
        print(grid[column][row], end="")
