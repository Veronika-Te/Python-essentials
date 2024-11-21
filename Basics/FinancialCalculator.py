# Create a dictionary with functions for various financial calculations (e.g., compound interest, loan payment, investment return).
# Write a function financial_calculator(operation, **kwargs) that uses this dictionary to perform the requested calculation.
from decimal import Decimal

def isDecimal(variable):
    """Checks if variable is decimal"""
    if Decimal(variable):
       return True
    return False 

#ROI-return on investment

def calculate_ROI(**kwargs)->Decimal:
    """Calculates return on investment(ROI)"""
    current_share_price=kwargs['current_share_price']
    total_dividends_received=kwargs['total_dividends_received']
    original_share_price=kwargs['original_share_price']
    
    if not current_share_price or not total_dividends_received or not original_share_price:
       return 0
    if isDecimal(current_share_price)  and isDecimal((total_dividends_received)) and isDecimal(original_share_price):
       roi=((current_share_price + total_dividends_received - original_share_price)/original_share_price)*100
       return Decimal(roi)
    return 0 

#Compound interest(CI)
#Used to calculate the total income taking into account compound interest with monthly capitalisation:
#annual rate-10%
def calculate_compound_interest(**kwargs)->Decimal:
    """Calculates compound interest"""
    #St-final amount
    #S-initial deposit
    #P-annual rate /100
    #Pm=P/12 annual rate in months
    #t-contractual term in months 
    initial_deposit=kwargs['initial_deposit']
    annual_rate=kwargs['annual_rate']
    t=kwargs['t']

    if not initial_deposit or not annual_rate or not t:
       return 0
    if int(t): 
       if isDecimal(initial_deposit) and isDecimal(annual_rate):
          P=annual_rate/100
          Pm=P/12
          final_income=initial_deposit *  ((1+Pm)**t)
          return Decimal(final_income)
       return 0 
    return 0 

#Loan Payment
def calculate_loan_payment(**kwargs)->Decimal:
    """Calculates loan payment"""
    #S-initial deposit
    #P-annual rate /100
    #Pm=P/12 annual rate in months
    #t-contractual term in months 
    initial_deposit=kwargs['initial_deposit']
    annual_rate=kwargs['annual_rate']
    t=kwargs['t']
    if not initial_deposit or not annual_rate or not t:
       return 0
    if int(t):
       if isDecimal(initial_deposit) and isDecimal(annual_rate):
          P=annual_rate/100
          Pm=P/12
          x=((1+Pm)**t)-1
          lp=initial_deposit * (Pm + (Pm/x))
          return Decimal(lp)
       return 0
    return 0

def get_keys(dictionary:dict)->set:
    """Creates set with keys of the given dictionary"""
    if not dictionary: 
       return 0
    return set(dictionary.keys())

def financial_calculator(operation:str, **kwargs):
    """Uses dictionary to perform the requested calculation."""
    financial_calculations={'ROI':calculate_ROI, 'Compound Interest':calculate_compound_interest, 'Loan Payment': calculate_loan_payment}
    keys=get_keys(financial_calculations)
    if not operation or not kwargs:
       return 0
    if operation in keys:
       if operation=='ROI':
          roi=financial_calculations.get(operation)
          res_roi=roi(**kwargs)
          return res_roi
       elif operation=='Compound Interest':
          ci=financial_calculations.get(operation)
          res_ci=ci(**kwargs)
          return res_ci
       elif operation=='Loan Payment':
          lp=financial_calculations.get(operation)
          res_lp=lp(**kwargs)
          return res_lp
       else:
          return 0
      
    else:
       return 0 #"Unknown operation"

def main():
   
   print("_______Financial calculations________")
   #ROI
   roi=financial_calculator('ROI',current_share_price=15,total_dividends_received=1.5,original_share_price=10)
   print("ROI:"+" "+str(roi) +'%')
  
   #Compound Interest
   # annual_rate=10 #10%
   # t=12 months
   ci=financial_calculator('Compound Interest',initial_deposit=150000,annual_rate=10,t=24)
   print(f"Compound interest, final amount: {ci}")

   #Loan payment
   lp=financial_calculator('Loan Payment',initial_deposit=200000,annual_rate=12,t=24)
   print(f"Loan payment per month: {lp}")


if __name__=="__main__":
   main()
 
 
 