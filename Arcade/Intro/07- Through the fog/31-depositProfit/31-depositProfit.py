#link https://app.codesignal.com/arcade/intro/level-7/8PxjMSncp9ApA4DAb

def depositProfit(deposit, rate, threshold):
    years = 0
    while deposit < threshold:
        years += 1
        deposit += deposit * (rate/100)
    return years
