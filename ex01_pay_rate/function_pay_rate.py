def paycheck(hours, rate):
    if hours > 40:
        reg = hours * rate
        otp = (hours-40)*(rate*0.5)
        pay = reg+otp
    else:
        pay = hours * rate
    return pay

fh = float(input("Enter hours: "))
fr = float(input("Enter rate: "))

xp = paycheck(fh, fr)
print("Pay:", xp)
