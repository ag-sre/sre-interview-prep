class Flight:
	def __init__(self, flight_number, base_price, additional_premium_cost):
		self.flight_number = flight_number
		self.seats = []
		self.additional_premium_cost = additional_premium_cost
		self.base_price = base_price

		for i in range(1,21):
			new_seat = Seat(i, self.base_price)
			self.seats.append(new_seat)

		for i in range(21,51):
			new_seat = Seat(i, self.base_price, self.additional_premium_cost)
			self.seats.append(new_seat)

	def getAvailableSeats(self):
		return self.seats

	def assignSeat(self, seat_number):
		i = 0
		for seat in self.seats:
			if seat_number == seat.seat_number:
				return self.seats.pop(i)
			i += 1
		return None


class Seat:
	def __init__(self, seat_number, base_price, additional_premium_cost=0):
		self.seat_number = seat_number
		self.total_price = additional_premium_cost + base_price



class Passenger:
	def __init__(self, passenger_id):
		self.passenger_id = passenger_id
		self.seats = []

	def takeSeat(self, flight, seat_number):
		passenger_seat = flight.assignSeat(seat_number)
		if passenger_seat:
			self.seats.append(passenger_seat)
		else:
			print("Requested seat is not available")


flight_EK500 = Flight("EK500", 500, 50)
new_passenger = Passenger(1)
new_passenger.takeSeat(flight_EK500, 30)

print("New passenger's seat")
for seat in new_passenger.seats:
	print("Seat Number:", seat.seat_number, " Seat Total Price:", seat.total_price)

print("Updated available seats")
for seat in flight_EK500.getAvailableSeats():
	print("Seat Number:", seat.seat_number," Seat Total Price:", seat.total_price)

print("Trying to take the same seat again")
new_passenger.takeSeat(flight_EK500, 30)


