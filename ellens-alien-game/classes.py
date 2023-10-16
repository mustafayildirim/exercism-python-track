class Alien:
    x_coordinate = 0
    y_coordinate = 0
    health = 0
    total_aliens_created = 0

    def __init__(self, location_x, location_y):
        self.x_coordinate = location_x
        self.y_coordinate = location_y
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        pass

def new_aliens_collection(alien_start_positions):
    alien_list = []
    for alien_position in alien_start_positions:
        location_x = alien_position[0]
        location_y = alien_position[1]
        alien_list.append(Alien(location_x,location_y))

    return alien_list
