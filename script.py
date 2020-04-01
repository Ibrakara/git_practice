premium_ground_shipping = 125

def ground_shipping_cost(weight):
  if weight <= 2:
    gsc = (weight * 1.5) + 20
  elif 6 >= weight > 2 :
    gsc = (weight * 3.0) + 20
  elif 10 >= weight > 6 :
    gsc = (weight * 4.0) + 20
  else:
    gsc = (weight * 4.75) + 20
  return gsc



def drone_shiiping_cost(weight):
  
  if weight <= 2:
    dsc = (weight * 4.5)
  elif 6 >= weight > 2 :
    dsc = (weight * 9.0)
  elif 10 >= weight > 6 :
    dsc = (weight * 12.00)
  else:
    dsc = (weight * 14.75)
  return dsc



def price_comparison(weight):
  gsc = ground_shipping_cost(weight)
  dsc = drone_shiiping_cost(weight)
  pgsc = premium_ground_shipping = 125.0
  
  if pgsc > gsc > dsc or gsc > pgsc > dsc:
    return 'The cheapest shipping method is drone shipping with the value of ' + str(dsc)
  elif dsc > pgsc > gsc or pgsc > dsc > gsc:
    return 'The cheapest shipping method is ground shipping with the value of ' + str(gsc)
  elif gsc > dsc > pgsc or dsc > gsc > pgsc:
    return 'The cheapest shipping method is premium ground shipping with the value of ' + str(pgsc)
    
  

  
print(price_comparison(4.8))
print(price_comparison(41.5))