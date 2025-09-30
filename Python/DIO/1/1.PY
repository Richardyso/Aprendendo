class RubiksCube:
    def __init__(self):
        self.faces = {
            'U': [['W'] * 3 for _ in range(3)],  # Up (branco)
            'D': [['Y'] * 3 for _ in range(3)],  # Down (amarelo)
            'F': [['G'] * 3 for _ in range(3)],  # Front (verde)
            'B': [['B'] * 3 for _ in range(3)],  # Back (azul)
            'L': [['O'] * 3 for _ in range(3)],  # Left (laranja)
            'R': [['R'] * 3 for _ in range(3)],  # Right (vermelho)
        }

    def print_face(self, face):
        for row in self.faces[face]:
            print(' '.join(row))
        print()

    def print_cube(self):
        print("Up:")
        self.print_face('U')
        print("Front:")
        self.print_face('F')
        print("Down:")
        self.print_face('D')
        print("Back:")
        self.print_face('B')
        print("Left:")
        self.print_face('L')
        print("Right:")
        self.print_face('R')

    def rotate_face_clockwise(self, face):
        self.faces[face] = [list(row) for row in zip(*self.faces[face][::-1])]

# Uso
cube = RubiksCube()
cube.print_cube()
cube.rotate_face_clockwise('U')  # Rotaciona a face superior no sentido horário
cube.print_cube()
