def app(*date,**kwargs):
    min_date=min(date)
    max_date=max(date)
    average=sum(date)/len(date)
    if kwargs.get("round") is not None:
        average=round(average,kwargs.get("round"))
    if kwargs.get("print"):
        print("Minimum:", min_date)
        print("Maximum:", max_date)
        print("Average:", average)
    return min_date, max_date, average

print(app(10, 20, 32, 40, 50,11, round=2, print=True))