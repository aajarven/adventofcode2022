from src.chamber import Chamber


def iterate_winds(winds):
    while True:
        for wind in winds:
            yield wind


def tower_height_after(winds, n_rocks):
    chamber = Chamber()
    for wind in iterate_winds(winds):
        chamber.advance_step(wind)
        if chamber.rocks == n_rocks:
            return chamber.height
