import random

POSSIBLE_SEAT_STATES = ['A', 'S', 'K', 'E']

def InitSeats(seats: list) -> list:
    for i in range(15):
        seats.append([[], []])

    return seats

def FillUpSeats(seats: list) -> list:
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            for k in range(10):
                seats[i][j].append(POSSIBLE_SEAT_STATES[random.randint(0, 3)])

    return seats

def Main():
    seats: list = []
    InitSeats(seats)
    FillUpSeats(seats)

if __name__ == "__main__":
    Main()
