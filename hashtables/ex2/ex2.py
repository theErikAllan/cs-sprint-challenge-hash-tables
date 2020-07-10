#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

ticket_dict = {}

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # We loop through the tickets in the tickets array
    for ticket in tickets:
        # For each ticket, we create a key:value pair in the ticket dictionary with the source airport as the key and the destination airport as the value
        ticket_dict[ticket.source] = ticket.destination

        # We use a couple conditionals to find the starting ticket and final ticket
        if ticket.source == 'NONE':
            starting_ticket = ticket
        if ticket.destination == 'NONE':
            final_ticket = ticket

    # We initialize the output array
    route = []

    # Since we are given the length of the trip, we use a for loop to piece it together
    for i in range(length):
        # We use conditionals to make sure the first and last elements in the output array are the starting location and final destination, respectively
        if i == 0:
            ticket_destination = starting_ticket.destination
            route.append(starting_ticket.destination)
        elif i == length:
            route.append(final_ticket.source)
        # Once the first and last elements are taken care of, we fill the gaps
        else:
            # First, we set the source of the next flight to be the destination of the current flight
            next_ticket_source = ticket_destination
            # Then we use a conditional to check if the source of the next flight is in our ticket dictionary
            if next_ticket_source in ticket_dict:
                # If it is, we append the destination of the current flight to the output array
                route.append(ticket_dict[next_ticket_source])
                # And we set the ticket destination to be the destination of the next flight
                ticket_destination = ticket_dict[next_ticket_source]

    return route
