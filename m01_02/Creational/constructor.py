class Floor:
    def __init__(self):
        self.name = 'floor'

    def build(self):
        print(f'Build {self.name}')


class Ceiling:
    def __init__(self):
        self.name = 'ceiling'

    def build(self):
        print(f'Build {self.name}')


class Wall:
    def __init__(self):
        self.name = 'wall'

    def build(self):
        print(f'Build {self.name}')


# class Building:
#     def __init__(self, floor: Floor, ceiling: Ceiling, wall: Wall):
#         self.floor = floor
#         self.ceiling = ceiling
#         self.wall = wall

class Building:
    def __init__(self):
        self.floor = None
        self.ceiling = None
        self.wall = None


def build():
    house = Building()
    house.floor = Floor()
    house.ceiling = Ceiling()
    house.wall = Wall()
    return house


if __name__ == '__main__':
    # house = Building(Floor(), Ceiling(), Wall())
    # house.floor.build()
    # house.ceiling.build()
    # house.wall.build()

    house = build()
    house.floor.build()
    house.ceiling.build()
    house.wall.build()
    