import random

POSSIBLE_SEAT_STATES = ['A', 'S', 'K', 'E']

def InitSeats(seats: list) -> None:
    for i in range(15):
        seats.append([[], []])

    return seats

def FillUpSeats(seats: list) -> None:
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            for k in range(10):
                seats[i][j].append(POSSIBLE_SEAT_STATES[random.randint(0, 3)])

    return seats

def RequestSeats(seatAmount: int, seats: list) -> int:
    availableNumSeatsInRow: int = 0

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            for k in range(len(seats[i][j])):
                if seats[i][j][k] == 'E':
                    availableNumSeatsInRow += 1
                else:
                    availableNumSeatsInRow = 0

                if availableNumSeatsInRow == seatAmount:
                    return i + 1

    return -1

def PrintSeats(seats: list) -> None:
    for i in range(len(seats)):
        print(seats[i])

def Main() -> None:
    seats: list = []
    InitSeats(seats)
    FillUpSeats(seats)
    print(RequestSeats(3, seats))

if __name__ == "__main__":
    Main()
