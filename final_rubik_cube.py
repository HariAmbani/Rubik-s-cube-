import random
import copy

class Cube:
    def __init__(self):
        self.initial_state = {
            "Top": [
                ["O", "O", "O"], 
                ["O", "O", "O"], 
                ["O", "O", "O"]
            ],
            "Bottom": [
                ["R", "R", "R"], 
                ["R", "R", "R"], 
                ["R", "R", "R"]
            ],
            "Left": [
                ["G", "G", "G"], 
                ["G", "G", "G"], 
                ["G", "G", "G"]
            ],
            "Right": [
                ["B", "B", "B"], 
                ["B", "B", "B"], 
                ["B", "B", "B"]
            ],
            "Front": [
                ["W", "W", "W"], 
                ["W", "W", "W"], 
                ["W", "W", "W"]
            ],
            "Back": [
                ["Y", "Y", "Y"], 
                ["Y", "Y", "Y"], 
                ["Y", "Y", "Y"]
            ]
            }

        self.face = copy.deepcopy(self.initial_state)  # Initialize the cube state
        self.moves = []  # Initialize moves list

        self.moves_dict = {
            'fc': 'Front Clockwise',
            'fa': 'Front Counter-clockwise',
            'bc': 'Back Clockwise',
            'ba': 'Back Counter-clockwise',
            'lc': 'Left Clockwise',
            'la': 'Left Counter-clockwise',
            'rc': 'Right Clockwise',
            'ra': 'Right Counter-clockwise',
            'tc': 'Top Clockwise',
            'ta': 'Top Counter-clockwise',
            'btc': 'Bottom Clockwise',
            'bta': 'Bottom Counter-clockwise',
            'mvc': 'Middle Vertical Clockwise',
            'mva': 'Middle Vertical Counter-clockwise',
            'mhc': 'Middle Horizontal Clockwise',
            'mha': 'Middle Horizontal Counter-clockwise'
            }


    def scramble_cube(self):
        # Randomly rotate the cube
        rotations = [
            'rotate_front_clockwise', 'rotate_front_counter_clockwise',
            'rotate_back_clockwise', 'rotate_back_counter_clockwise',
            'rotate_left_clockwise', 'rotate_left_counter_clockwise',
            'rotate_right_clockwise', 'rotate_right_counter_clockwise',
            'rotate_top_clockwise', 'rotate_top_counter_clockwise',
            'rotate_bottom_clockwise', 'rotate_bottom_counter_clockwise',
            'rotate_middle_vertical_clockwise', 'rotate_middle_vertical_counter_clockwise',
            'rotate_middle_horizontal_clockwise', 'rotate_middle_horizontal_counter_clockwise'
        ]
        for _ in range(20):  # Scramble the cube with 20 random moves
            move = random.choice(rotations)
            getattr(self, move)()  # Call the corresponding rotate method
            self.moves.append(move)  # Store the move in the moves list

    def reset(self):
        # Reset the cube to its initial state
        self.face = copy.deepcopy(self.initial_state)  # Reset the cube state
        self.moves.clear()  # Clear the moves list

    def add_move(self,user_input):
        if user_input in self.moves_dict:
            self.move = self.moves_dict[user_input]
            self.moves.append(self.move)
            

    def solve_cube(self):
        # Print the moves list in reverse order
        print("To solve the cube, follow these moves in order:")
        for move in reversed(self.moves):
            print(move)

    def rotate_face_clockwise(self, face_name):
        face = self.face[face_name]
        ####### Corner cublet rotation ######
        temp = face[0][0]
        face[0][0] = face[2][0]
        face[2][0] = face[2][2]
        face[2][2] = face[0][2]
        face[0][2] = temp

        ###### Edge cublet rotation ######
        temp = face[0][1]
        face[0][1] = face[1][0]
        face[1][0] = face[2][1]
        face[2][1] = face[1][2]
        face[1][2] = temp

    def rotate_face_counter_clockwise(self, face_name):
        face = self.face[face_name]
        ####### Corner cublet rotation ######
        temp = face[0][0]
        face[0][0] = face[0][2]
        face[0][2] = face[2][2]
        face[2][2] = face[2][0]
        face[2][0] = temp

        ###### Edge cublet rotation ######
        temp = face[0][1]
        face[0][1] = face[1][2]
        face[1][2] = face[2][1]
        face[2][1] = face[1][0]
        face[1][0] = temp

    def rotate_top_clockwise(self):
        self.rotate_face_clockwise("Top")
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Right"][0]
        self.face["Right"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Left"][0]
        self.face["Left"][0] = temp
        

    def rotate_bottom_clockwise(self):
        self.rotate_face_clockwise("Bottom")
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Left"][2]
        self.face["Left"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Right"][2]
        self.face["Right"][2] = temp

    def rotate_left_clockwise(self):
        self.rotate_face_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = temp_col[i]

    def rotate_right_clockwise(self):
        self.rotate_face_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = temp_col[i]

    def rotate_front_clockwise(self):
        self.rotate_face_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Left"][i][2]
            self.face["Left"][i][2] = self.face["Bottom"][0][i]
            self.face["Bottom"][0][i] = self.face["Right"][i][0]
            self.face["Right"][i][0] = temp[i]

    def rotate_back_clockwise(self):
        self.rotate_face_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = self.face["Bottom"][2][i]
            self.face["Bottom"][2][i] = self.face["Left"][i][0]
            self.face["Left"][i][0] = temp[i]

    # Counter-clockwise rotation methods
    def rotate_top_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Top")
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Left"][0]
        self.face["Left"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Right"][0]
        self.face["Right"][0] = temp

    def rotate_bottom_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Bottom")
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Right"][2]
        self.face["Right"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Left"][2]
        self.face["Left"][2] = temp

    def rotate_left_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = self.face["Bottom"][2 - i][0]
            self.face["Bottom"][2 - i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = temp_col[i]

    def rotate_right_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = temp_col[i]

    def rotate_front_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Right"][i][0]
            self.face["Right"][i][0] = self.face["Bottom"][0][i]
            self.face["Bottom"][0][i] = self.face["Left"][i][2]
            self.face["Left"][i][2] = temp[i]

    def rotate_back_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Left"][i][0]
            self.face["Left"][i][0] = self.face["Bottom"][2][i]
            self.face["Bottom"][2][i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = temp[i]

            
    def rotate_middle_vertical_clockwise(self):
        # Rotate the middle vertical layer clockwise
        temp_col = [self.face["Front"][i][1] for i in range(3)]
        for i in range(3):
            self.face["Front"][i][1] = self.face["Bottom"][i][1]
            self.face["Bottom"][i][1] = self.face["Back"][i][1]
            self.face["Back"][i][1] = self.face["Top"][i][1]
            self.face["Top"][i][1] = temp_col[i]

    def rotate_middle_vertical_counter_clockwise(self):
        # Rotate the middle vertical layer counter-clockwise
        temp_col = [self.face["Front"][i][1] for i in range(3)]
        for i in range(3):
            self.face["Front"][i][1] = self.face["Top"][i][1]
            self.face["Top"][i][1] = self.face["Back"][i][1]
            self.face["Back"][i][1] = self.face["Bottom"][i][1]
            self.face["Bottom"][i][1] = temp_col[i]

    def rotate_middle_horizontal_clockwise(self):
        # Rotate the middle horizontal layer clockwise
        temp_row = self.face["Front"][1][:]
        self.face["Front"][1] = self.face["Left"][1][:]
        self.face["Left"][1] = self.face["Back"][1][:]
        self.face["Back"][1] = self.face["Right"][1][:]
        self.face["Right"][1] = temp_row

    def rotate_middle_horizontal_counter_clockwise(self):
        # Rotate the middle horizontal layer counter-clockwise
        temp_row = self.face["Front"][1][:]
        self.face["Front"][1] = self.face["Right"][1][:]
        self.face["Right"][1] = self.face["Back"][1][:]
        self.face["Back"][1] = self.face["Left"][1][:]
        self.face["Left"][1] = temp_row

    def print_cube(self):
        # Print Top face name and face
        print("                                ", "TOP")
        print("                               ", " ".join(self.face["Top"][0]))
        print("                               ", " ".join(self.face["Top"][1]))
        print("                               ", " ".join(self.face["Top"][2]))

        print()
            
        # Print Left, Front, Right, Back face names and faces side by side
        print("                         LEFT", " " * 1, "FRONT", "  RIGHT", " " * 1, "BACK")
        for row in range(3):
            print("                        ",end="")
            print(" ".join(self.face["Left"][row]), "|", " ".join(self.face["Front"][row]), "|", 
                  " ".join(self.face["Right"][row]), "|", " ".join(self.face["Back"][row]))
        print()

        # Print Bottom face name and face
        print("                               ", "BOTTOM")
        print("                               ", " ".join(self.face["Bottom"][0]))
        print("                               ", " ".join(self.face["Bottom"][1]))
        print("                               ", " ".join(self.face["Bottom"][2]))
    def run(self):
        self.print_cube()

def run():
    print("\n     3X3 Rubik's Cube simulator using python (By Hari Ambani)    \n")
    cube = Cube()
    print()
    while(True):
        print('''                   RULES
                   -------
    -> fc  - Front  clockwise     -> fa  - Front  counter-clockwise
    -> bc  - Back   clockwise     -> ba  - Back   counter-clockwise
    -> lc  - Left   clockwise     -> la  - Left   counter-clockwise
    -> rc  - Right  clockwise     -> ra  - Right  counter-clockwise
    -> tc  - Top    clockwise     -> ta  - Top    counter-clockwise
    -> btc - Bottom clockwise     -> bta - Bottom counter-clockwise

    -> mvc - middle vertical   clockwise    -> mva - middle verical    counter-clockwise
    -> mhc - middle horizontal clockwise    -> mha - middle horizontal counter-clockwise

    -> scm - scramble    -> s - Solve    -> rst - reset    -> n - stop
        ''')
        
        cube.print_cube()
        print()
        ch = input("Enter your choice : ")
        if ch=='fc':
            cube.add_move(ch)
            cube.rotate_front_clockwise()
            print("\nAfter rotating Front face clockwise:\n")
            cube.print_cube()

        elif ch=='fa':
            cube.add_move(ch)
            cube.rotate_front_counter_clockwise()
            print("\nAfter rotating Front face counter-clockwise:\n")
            cube.print_cube()

        elif ch=='bc':
            cube.add_move(ch)
            cube.rotate_back_clockwise()
            print("\nAfter rotating Back face clockwise:\n")
            cube.print_cube()

        elif ch=='ba':
            cube.add_move(ch)
            cube.rotate_back_counter_clockwise()
            print("\nAfter rotating Back face counter-clockwise:\n")
            cube.print_cube()

        elif ch=='lc':
            cube.add_move(ch)
            cube.rotate_left_clockwise()
            print("\nAfter rotating left face clockwise:\n")
            cube.print_cube()

        elif ch=='la':
            cube.add_move(ch)
            cube.rotate_left_counter_clockwise()
            print("\nAfter rotating left face counter-clockwise:\n")
            cube.print_cube()

        elif ch=='rc':
            cube.add_move(ch)
            cube.rotate_right_clockwise()
            print("\nAfter rotating right face clockwise:\n")
            cube.print_cube()

        elif ch=='ra':
            cube.add_move(ch)
            cube.rotate_right_counter_clockwise()
            print("\nAfter rotating top face counter-clockwise:\n")
            cube.print_cube()

        elif ch=='tc':
            cube.add_move(ch)
            cube.rotate_top_clockwise()
            print("\nAfter rotating top face clockwise:\n")
            cube.print_cube()

        elif ch=='ta':
            cube.add_move(ch)
            cube.rotate_top_counter_clockwise()
            print("\nAfter rotating bottom face counter-clockwise:\n")
            cube.print_cube()

        elif ch=='btc':
            cube.add_move(ch)
            cube.rotate_bottom_clockwise()
            print("\nAfter rotating bottom face clockwise:\n")
            cube.print_cube()

        elif ch=='bta':
            cube.add_move(ch)
            cube.rotate_bottom_counter_clockwise()
            print("\nAfter rotating bottom face counter-clockwise:\n")
            cube.print_cube()

        elif ch=='mvc':
            cube.add_move(ch)
            cube.rotate_middle_vertical_clockwise()
            print("\nAfter rotating middle vertical layer clockwise:\n")
            cube.print_cube()

        elif ch=='mva':
            cube.add_move(ch)
            cube.rotate_middle_vertical_counter_clockwise()
            print("\nAfter rotating middle vertical layer clockwise:\n")
            cube.print_cube()

        elif ch=='mhc':
            cube.add_move(ch)
            cube.rotate_middle_horizontal_clockwise()
            print("\nAfter rotating middle horizontal layer clockwise:\n")
            cube.print_cube()

        elif ch=='mha':
            cube.add_move(ch)
            cube.rotate_middle_horizontal_counter_clockwise()
            print("\nAfter rotating middle horizontal layer clockwise:\n")
            cube.print_cube()

        elif ch == 'scm':
            cube.scramble_cube()
            print("\nAfter scrambling the cube:\n")
            cube.print_cube()
            
        elif ch == 'rst':
            cube.reset()
            print("\nCube has been reset to initial state:\n")
            cube.print_cube()

        elif ch == 's':
            cube.solve_cube()
            print("\n\n")
            cube.reset()
            cube.print_cube()
            u = input("\n\nTo play again press y else any key : ")
            if(u=='y'):
                cube.reset()
            else:
                break
            
        elif ch=='n':
            break

        else:
            print("\nInvalid input \n please enter a valid input given below\n")


            
if __name__ == "__main__":
    run()
