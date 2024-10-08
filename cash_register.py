def cash_register(amount_due,amount_paid):
  if amount_paid < amount_due:
    print("Amount is less than what was due")
    
  change = amount_paid - amount_due 
  denominations = {"R200":20000,"R100" :10000,"R50" :5000,"R20" :2000,"R10" : 1000,"R5" :500,"R2" :200,"R1" :100,"50c" :50,"20c" :20,"10c" :10,"5c" :5}

  change_distribution ={}

  for denominations,value in denominations.items():
      count = change//value
      if count > 0:
        change_distribution[denominations] = count
        change -= count*value
  return change_distribution
print(cash_register(15,20))