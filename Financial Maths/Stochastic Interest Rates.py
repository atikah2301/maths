# Stochastic Interest Rates are used to model interest over time that accounts for a degree of uncertainty
# Case (1) : Fixed interest rates (FIR) - chosen by a random variable, R, at the start of a loan or investment etc.
# Case (2) : Varying interest rates (VIR) - chosen by a random variable, where the rate is decided at the beginning of each year.
# Case (3) : Varying interest rates with regular deposits - a fixed amount is deposited at the start of each year

import math

FIGS = 5

def sig_figs(num, figs):
    """Round a number to a given number of significant figures."""
    return round(num, figs - int(math.floor(math.log10(abs(num)))) - 1)


def FIR_E(R: list[tuple()], P_0: int, n: int, round=False, figs=FIGS) -> int:
    """Calculate the expected accumulated wealth under the fixed interest rate model."""
    intermediate_sum = 0
    for r, p in R:
        intermediate_sum += p*((1+r)**n)
    expectation = P_0*intermediate_sum
    if round: return sig_figs(expectation, figs)
    else: return expectation


def FIR_Var(R: list[tuple()], P_0: int, n: int, round=False, figs=FIGS) -> int:
    """Calculate the variance of the accumulated wealth under the fixed interest rate model."""
    mu = FIR_E(R, P_0, n, round=round, figs=figs)
    intermediate_sum = 0
    for r, p in R:
        intermediate_sum += p*((1+r)**(2*n))
    variance = (P_0**2)*(intermediate_sum - mu**2)
    if round: return sig_figs(variance, figs)
    else: return variance


def VIR_mu(R: list[tuple()], n: int, round=False, figs=FIGS) -> int:
    """Calculate expectation of R"""
    mu = 0
    for r, p in R:
        mu += p*r
    if round: return sig_figs(mu, figs)
    else: return mu


def VIR_E(R: list[tuple()], P_0: int, n: int, round=False, figs=FIGS) -> int:
    """Calculate the expected accumulated wealth under the varying interest rate model."""
    mu = VIR_mu(R, n, round=round, figs=figs)
    expectation = P_0*((1 + mu)**n)
    if round: return sig_figs(expectation, figs)
    else: return expectation


def VIR_sigma(R: list[tuple()], n: int, round=False, figs=FIGS) -> int:
    """Calculate variance of R"""
    mu = VIR_mu(R, n, round=round, figs=figs)
    intermediate_sum = 0
    for r, p in R:
        intermediate_sum += (r**2)*p
    sigma_sqr = intermediate_sum - mu**2
    if round: return sig_figs(sigma_sqr, figs)
    else: return sigma_sqr


def VIR_Var(R: list[tuple()], P_0: int, n: int, round=False, figs=FIGS) -> int:
    """Calculate the variance of the accumulated wealth under the varying interest rate model."""
    mu = VIR_mu(R, n, round=round, figs=figs)
    sigma_sqr = VIR_sigma(R, n, round=round, figs=figs)
    variance = (P_0**2)*(((1 + mu)**2 + sigma_sqr)**n - (1 + mu)**(2*n))
    if round: return sig_figs(variance, figs)
    else: return variance


def VIR_regular_desposits():
    """Calculate the accumulated wealth under the varying interest rate model."""
    pass

# Probability Density Function for the possible rates of interest
all_r = [0.02, 0.0225, 0.03] #[0.06, 0.08, 0.10]
all_p = [0.3, 0.5, 0.2] #[0.2, 0.7, 0.1]
R = list(zip(all_r, all_p))

# Principal value, or deposit amount 
P_0 = 200 #5000
P_i = 200

# Number of years
n = 2


print("ROUNDED AFTER CALCULATION")
print()
print(f"Exp of accumulation for FIR = {round(FIR_E(R, P_0, n), 2)}")
print(f"Var of accumulation for FIR = {round(FIR_Var(R, P_0, n), 2)}")
print()
print(f"E(R) = {sig_figs(VIR_mu(R, n), 3)}")
print(f"Var(R) = {sig_figs(VIR_sigma(R, n), 3)}")
print()
print(f"Exp of accumulation for VIR = {round(VIR_E(R, P_0, n), 2)}")
print(f"Var of accumulation for VIR = {round(VIR_Var(R, P_0, n), 2)}")
print()

# print("ROUNDED DURING & AFTER CALCULATION")
# print()
# print(f"Exp of accumulation for FIR = {round(FIR_E(R, P_0, n, round=True), 2)}")
# print(f"Var of accumulation for FIR = {round(FIR_Var(R, P_0, n, round=True), 2)}")
# print()
# print(f"Exp of accumulation for VIR = {round(VIR_E(R, P_0, n, round=True), 2)}")
# print(f"Var of accumulation for VIR = {round(VIR_Var(R, P_0, n, round=True), 2)}")
# print()
