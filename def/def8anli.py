# 电商订单计算器
def calc_order_cost(*arges,coupon,score,express):
    """
    arges: 商品信息(名,价格,数量)
    coupon: 优惠券折扣
    score: 积分
    express: 运费
    return: 订单总价=商品总金额-优惠券折扣-积分抵扣+运费
    """
    # 计算总价
    total_price =[goods[1]*goods[2] for goods in arges]
    total_cost=sum(total_price)
    #优惠券
    if total_cost>=5000 and coupon<=total_cost:
        total_cost-=coupon
    #积分
    if total_cost>=5000 and score/100<=total_cost:
        total_cost-=score/100
    #运费
    total_cost+=express
    return total_cost
total_cost=round(calc_order_cost(("鼠标",100.22,2),("键盘",2000,4),coupon=500,score=1000,express=20),2)
print("订单总价:",total_cost)

        
    
