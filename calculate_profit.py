#solution 1
class entry:
	def __init__(self, attr):
		self.cost=attr['cost_price']
		self.sell=attr['sell_price']
		self.inventory=attr['inventory']
	
	def prof(self):
		return((self.sell-self.cost)*self.inventory)
	
def profit(info):
	return(round(entry(info).prof()))


print (profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))

#solution 2
def profit(info):
	return round((info["inventory"])*(info["sell_price"] - info["cost_price"]))

print (profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))