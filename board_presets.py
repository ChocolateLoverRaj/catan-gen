'''
Catan Seafarers Scenario Presets
'''

class Scenario:
    def __init__(self, boardstring, hexes, numbers):
        self.boardstring = boardstring
        self.hexes = hexes
        self.numbers = numbers

def create_hexes(deserts=0, golds=0, fields=0, hills=0, mountains=0, pastures=0, forests=0):
    return {'W': fields,
            'H': hills,
            'M': mountains,
            'P': pastures,
            'F': forests,
            'D': deserts+golds}

def create_numbers(two, three, four, five, six, eight, nine, ten, eleven, twelve):
    return {2:two, 3:three, 4:four, 5:five, 6:six, 8:eight, 9:nine, 10:ten, 11:eleven, 12:twelve}

S0_3P = ("- - - - - - -\n"
        "- - M M M - -\n"
         "- M M M M - -\n"
        "- M M M M M -\n"
         "- M M M M - -\n"
        "- - M M M - -\n"
         "- - - - - - -\n")

S0_3P_hexes = create_hexes(1,0,4,3,3,4,4)
S0_3P_numbers = create_numbers(1,2,2,2,2,2,2,2,2,1)

S0_4P = ("- - - - - - -\n"
        "- - M M M - -\n"
         "- M M M M - -\n"
        "- M M M M M -\n"
         "- M M M M - -\n"
        "- - M M M - -\n"
         "- - - - - - -\n")

S0_4P_hexes = create_hexes(1,0,4,3,3,4,4)
S0_4P_numbers = create_numbers(1,2,2,2,2,2,2,2,2,1)

S0_3P = ('- - - - - - - - -\n'
        '- - M M M M - -\n'
         '- - M M M - -\n'
        '- - M M M M - -\n'
         '- M M M M M -\n'
        '- - M - - - - M -\n'
         '- - - M M M - - -\n'
        '- - - - - M - - -\n'
         '- - - - - - - - -\n')

# S1: Heading for New Shores, 3-Player, 9x9
S1_3P = ('- - - - - - - - -\n'
        '- - - M M M - - -\n'
         '- - M M M M - - -\n'
        '- - - M M M M - -\n'
         '- M - M M M - M -\n'
        '- - M - - - - M -\n'
         '- - - M M M - - -\n'
        '- - - - - M - - -\n'
         '- - - - - - - - -\n')

S1_3P_hexes = create_hexes(0,2,4,4,4,5,3)
S1_3P_numbers = create_numbers(1,2,3,3,2,3,2,3,2,1)

# S1: Heading for New Shores, 4-Player, 9x10
S1_4P = ('- - - - - - - - -\n'
        '- - - M M M - - -\n'
         '- - M M M M - - -\n'
        '- - M M M M M - -\n'
         '- - M M M M - M -\n'
        '- M - M M M - M -\n'
         '- M - - - - - - -\n'
        '- - - M M M M - -\n'
         '- - - - M - - - -\n'
        '- - - - - - - - -\n')

S1_4P_hexes = create_hexes(1,2,5,5,5,5,5)
S1_4P_numbers = create_numbers(2,3,3,3,3,3,3,3,3,1)

# S2: The Four Islands, 3-Player, 9x9
S2_3P = ('- - - - - - - - -\n'
        '- - - M M M - - -\n'
         '- - - M M - M - -\n'
        '- - - - M - M M -\n'
         '- - M - - - M - -\n'
        '- - M M - M - - -\n'
         '- - M - M M M - -\n'
        '- - - - - M M - -\n'
         '- - - - - - - - -\n')

S2_3P_hexes = create_hexes(0,0,4,4,4,4,4)
S2_3P_numbers = create_numbers(1,2,2,3,2,2,3,2,2,1)

# S2: The Four Islands, 4-Player, 9x9
S2_4P = ('- - - - - - - - -\n'
        '- - - M M M - - -\n'
         '- - M M M - M - -\n'
        '- - - M - - M M -\n'
         '- M - - M - - M -\n'
        '- - M M - M M - -\n'
         '- - M - M M M - -\n'
        '- - - - - M M - -\n'
         '- - - - - - - - -\n')

S2_4P_hexes = create_hexes(0,0,5,4,4,5,5)
S2_4P_numbers = create_numbers(1,2,3,3,2,2,3,3,3,1)

# S3: The Fog Islands, 3-Player, 9x10
S3_3P = ('- - - - - - - - -\n'
        '- - - - - - - - -\n'
         '- - M M M M - - -\n'
        '- - - M M M - - -\n'
         '- - - - - - - - -\n'
        '- - - - - - - - -\n'
         '- - - - - - - - -\n'
        '- - - M M M M - -\n'
         '- - - M M M - - -\n'
        '- - - - - - - - -\n')

S3_3P_hexes = create_hexes(0,0,2,2,2,4,4)
S3_3P_numbers = create_numbers(0,1,1,2,2,2,2,1,2,1)

# S3: The Fog Islands, 4-Player, 9x10
S3_4P = ('- - - - - - - - -\n'
        '- - - M M M - - -\n'
         '- - M M M M - - -\n'
        '- - - - - - - - -\n'
         '- - - - - - - - -\n'
        '- - - - - - - - -\n'
         '- - - - - M M - -\n'
        '- - M M M M M - -\n'
         '- - - M M M - - -\n'
        '- - - - - - - - -\n')

S3_4P_hexes = create_hexes(0,0,3,3,3,4,4)
S3_4P_numbers = create_numbers(1,2,2,2,2,2,2,2,1,1)

S0_3P_scenario = Scenario(S0_3P, S0_3P_hexes, S0_3P_numbers)
S0_4P_scenario = Scenario(S0_4P, S0_4P_hexes, S0_4P_numbers)
S1_3P_scenario = Scenario(S1_3P, S1_3P_hexes, S1_3P_numbers)
S1_4P_scenario = Scenario(S1_4P, S1_4P_hexes, S1_4P_numbers)
S2_3P_scenario = Scenario(S2_3P, S2_3P_hexes, S2_3P_numbers)
S2_4P_scenario = Scenario(S2_4P, S2_4P_hexes, S2_4P_numbers)
S3_3P_scenario = Scenario(S3_3P, S3_3P_hexes, S3_3P_numbers)
S3_4P_scenario = Scenario(S3_4P, S3_4P_hexes, S3_4P_numbers)

scenarios = {('normal', 3):         S0_3P_scenario,
             ('normal', 4):         S0_4P_scenario,
             ('new_shores', 3):     S1_3P_scenario,
             ('new_shores', 4):     S1_4P_scenario,
             ('four_islands', 3):   S2_3P_scenario,
             ('four_islands', 4):   S2_4P_scenario,
             ('fog_islands', 3):    S3_3P_scenario,
             ('fog_islands', 4):    S3_4P_scenario}
