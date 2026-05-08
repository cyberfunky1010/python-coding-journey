# program to calculate simple interest using function interest() that receives principle, rate and time as parameters and returns the simple interest.
# do specify values for rate and time as 10% and 2 years respectively.

def interest(principle, rate=10, time=2):
    si = (principle * rate * time) / 100
    return si

prin = float(input(f"enter the principle amount: "))
print(f"simple interest with default time and ROI is {interest(prin)} \n")

ROI = float(input(f"enter rate of interest (ROI): "))

time = float(input(f"enter time in years: "))

print(f"\nSimple Interest with your time and ROI: {interest(prin, ROI, time)}")