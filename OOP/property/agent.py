from valid import get_valid_input
from main import HouseRental, HousePurchase, ApartmentRental, ApartmentPurchase
class Agent:
	"""docstring for Agent"""
	type_map = {
	("house","rental"): HouseRental,
	("house","purchase"): HousePurchase,
	("apartment","rental"): ApartmentRental,
	("apartment","purchase"): ApartmentPurchase
	}
	def __init__(self):
		self.property_list = []

	def display(self):
		for proprty in self.property_list:
			proprty.display()

	def add_property(self):
		proprty_type = get_valid_input("what type of property?",("house","apartment")).lower()
		payment_type =  get_valid_input("what payment type?",("purchase","rental")).lower()
		PropertyClass = self.type_map[(proprty_type,payment_type)]
		init_args = PropertyClass.prompt_init()
		self.property_list.append(PropertyClass(**init_args))



