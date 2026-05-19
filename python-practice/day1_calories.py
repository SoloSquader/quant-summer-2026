nuts_avocado_raisins=500
omelet=160
cereal=650
nurriShake=150
taroMilkTea=800

print("Nuts/avocado/Raisins:",nuts_avocado_raisins, "calories")
print("Omelet",omelet,"calories")
print("Cereal",cereal,"calories")
print("Nurri Shake",nurriShake,"calories")
print("Taro Milk Tea",taroMilkTea,"calories")
print("Total:",nuts_avocado_raisins+omelet+cereal+nurriShake+taroMilkTea)

def calcalc(item1,item2,item3,item4,item5):
    total=item1+item2+item3+item4+item5
    return total

thisisprinted=calcalc(nuts_avocado_raisins,omelet,cereal,nurriShake,taroMilkTea)
print("total using function:",thisisprinted)

