def calca(*date):
    min_date=min(date)
    max_date=max(date)
    average=sum(date)/len(date)
    print("Minimum:", min_date)
    print("Maximum:", max_date)
    print("Average:", average)
    return min_date, max_date, average
print(calca(10, 20, 30, 40, 50))