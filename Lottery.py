import argparse
import random

class lotteryTicket:
    def __init__(self, setLengths, numberRange):
        self.setLengths = setLengths
        self.numberRange = numberRange


def generateTickets(numOfTickets, lotteryTicketType):
    tickets = []
    for i in range(0, numOfTickets):
        ticket = []
        for i in range(0,len(lotteryTicketType.setLengths)):
            ticketSet = []
            ticketPool = [*range(1, lotteryTicketType.numberRange)]
            remainingPool = len(ticketPool) - 1 if ticketPool else None
            for j in range(0, lotteryTicketType.setLengths[i]):
                ticketSet.append(ticketPool.pop(random.randint(0, remainingPool))) if ticketPool is not None else None
                remainingPool -= 1 if ticketPool else None
            ticket.append(ticketSet)
        tickets.append(ticket)
    return tickets


if __name__ == '__main__':
    switchParser = argparse.ArgumentParser(description="Lottery switch parser")
    lottoType = switchParser.add_mutually_exclusive_group(required=True)

    lottoType.add_argument('-649', action='store_const', dest='lottery', const=lotteryTicket([6, 10], 49), help='Generate a Loto649 Ticket')
    lottoType.add_argument('-max', action='store_const', dest='lottery', const=lotteryTicket([7, 7, 7], 50), help='Generate a LottoMax Ticket')
    lottoType.add_argument('-ota', action='store_const', dest='lottery', const=lotteryTicket([6, 6], 45), help='Generate a Lottario Ticket')
    switchParser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    switchParser.add_argument('-n', help="Number of tickets you would like to generate", type=int, default=1)
    switch = switchParser.parse_args()

    generatedTickets = generateTickets(switch.n, switch.lottery)

    for i in range(0, len(generatedTickets)):
        print(f"Ticket {i + 1}: {generatedTickets[i]}")

    # write generated tickets to file
    try:
        fhandle = open("Tickets.txt", "w")
        fhandle.write(str(generatedTickets))
    except IOError as e:
        print("Exception caught: Unable to write to file  ", e)
    except Exception as e:
        print("Error: ", e)
    else:
        print("Find your ticket numbers in Tickets.txt")
        fhandle.close()
