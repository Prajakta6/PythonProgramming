import TaxCalculation

def CallToTaxCalculation():
    amount = int(input("Enter your amount: "))
    tax = float(input("Enter your tax slab: "))
    totalTax = TaxCalculation.CalculateTax(amount,tax)
    print("Total Tax = ",totalTax)

def main():
   CallToTaxCalculation()

if __name__ == "__main__":
    main()
