import matplotlib.pyplot as plt

def main():
    fig, axes = plt.subplots(1, 1)
    axes.set_xlabel('Monthly payment ($)')
    axes.set_ylabel('Time to payoff (yrs)')
    axes.set_ylim(0, 40)
    axes.minorticks_on()
    axes.grid()
    
    p1, ht1, lt1 = years_vs_payment(0.068, 147000)
    p2, ht2, lt2 = years_vs_payment(0.04315, 147000)
    axes.plot(p1, ht1, 'ro')
    axes.plot(p1, lt1, 'ro')
    axes.plot(p2, ht2, 'bo')
    axes.plot(p2, lt2, 'bo')
    
    fig.show()
    while True:
        pass

def B(t, r, Bo, P):
    '''args float t, float r, float Bo, float P
    
    returns the balance of a loan after t years, given a 
    starting balance Bo, yearly interest rate r, and yearly
    payment P'''
    
    return ( Bo*(1 + r)**t - P*(float(1 - (1 + r)**t)/(-r)) )

def find_zero(r, Bo, P):
    t = 0
    if B(0, r, Bo, P) <= B(1, r, Bo, P):
        return None
    while B(t, r, Bo, P) > 0:
        t += 1
    while B(t, r, Bo, P) < 0:
        t -= 0.1
    while B(t, r, Bo, P) > 0:
        t += 0.01
    return t
    
def years_vs_payment(r, Bo):
    
    rm = (1 + r)**(1.0/12) - 1
    print('Yearly interest rate is', r)
    print('Monthly interest rate is', rm)
    high_times = []
    low_times = []
    monthly_payments = []
    
    for p in range(4000):
        high_payoff_time = find_zero(r, Bo, 12*p)
        if high_payoff_time == None:
            continue
        low_payoff_time = find_zero(r, Bo-12*p, 12*p)
        high_times.append(high_payoff_time)
        low_times.append(low_payoff_time)
        monthly_payments.append(p)
    
    return monthly_payments, high_times, low_times
        

if __name__=='__main__':
    main()
    