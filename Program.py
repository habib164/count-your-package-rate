weight = float(input("Input your weight in lbs: "))
cost_ground = 0
cost_drone = 0
#ground shipping list
price_per_pound_1 = 1.50
price_per_pound_2 = 3.00
price_per_pound_3 = 4.00
price_per_pound_4 = 4.75

flat_charge_ground = 20.00

#drone shipping list
drone_ship_price_1 = 4.50
drone_ship_price_2 = 9.00
drone_ship_price_3 = 12.00
drone_ship_price_4 = 14.25

flat_charge_drone = 0.00

#count ground shipping 
if weight <= 2:
  cost_ground = weight * price_per_pound_1 + flat_charge_ground
if weight > 2 and weight <= 6:
  cost_ground = weight * price_per_pound_2 + flat_charge_ground
if weight > 6 and weight <= 10:
  cost_ground = weight * price_per_pound_3 + flat_charge_ground
if weight > 10:
  cost_ground = weight * price_per_pound_4 + flat_charge_ground

print("Ground cost: $", cost_ground)

cost_premium_ground = 125.00

print("Ground Shipping Premium $", cost_premium_ground)

#count Drone shipping
if weight <= 2:
  cost_drone = weight * drone_ship_price_1 + flat_charge_drone
if weight > 2 and weight <= 6:
  cost_drone = weight * drone_ship_price_2 + flat_charge_drone
if weight > 6 and weight <= 10:
  cost_drone = weight * drone_ship_price_3 + flat_charge_drone
if weight > 10:
  cost_drone = weight * drone_ship_price_4 + flat_charge_drone

print("Drone cost: $", cost_drone)