"""Island Perimeter."""


def _is_land_perimeter(grid):

    answer = 0
    height = len(grid)
    width = len(grid[0])
    dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def is_water(i, j):
        if i < 0 or i == height or j < 0 or j == width:
            return 1
        return 1 - grid[i][j]

    for i in xrange(height):
        for j in xrange(width):
            if grid[i][j] == 1:
                for d in dir:
                    answer = answer + is_water(i + d[0], j + d[1])
    return answer


if __name__ == '__main__':
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print (_is_land_perimeter(grid))
    print (_is_land_perimeter([[1]]))
