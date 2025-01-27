def InitSeats(seats: list) -> list:
    for i in range(15):
        seats.append([[], []])

    return seats

def Main():
    seats: list = []
    InitSeats(seats)

if __name__ == "__main__":
    Main()
