def arc(botton,high):
    area=botton*high/2
    return area
def car(str):
    num=0
    for i in str:
        if i in "aeiouAEIOU":
            num+=1
    return num
def calss(score):
    max_score=max(score)
    min_score=min(score)
    avg_score=sum(score)/len(score)
    return max_score,min_score,avg_score
print(arc(5,10))
print(car("Hello World"))
print(calss([90, 80, 70, 60, 50]))


