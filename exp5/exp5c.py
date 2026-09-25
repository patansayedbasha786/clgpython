import math
# Binomial Distributio
n =int(input("Enter number of trials (n): "))
p =float(input("Enter probability of success (p): "))
x =int(input("Enter number of successes (x): "))
# Binomial probability formula
binomial=(math.comb(n,x)*(p**x)*((1-p)**(n-x)))
print("\nBinomial Distribution")
print("P(X =",x,")=",binomial)
# Poisson Distribution
lam=float(input("\nEnter mean rate (lambda): "))
x=int(input("Enter number of occurrences (x): "))
# Poisson probability formula
poisson=((math.exp(-lam)*(lam**x))/math.factorial(x))
print("\nPoisson Distribution")
print("P(X=",x,")=",poisson)
