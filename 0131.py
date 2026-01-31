class CuteCat:
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color
    def speak(self):
        print("喵"*self.age)
    def think(self,content):
        print(f"小猫{self.name}在思考{content}...")

cat1 = CuteCat("jojo", 2, "橙色")
print(f"小猫{cat1.name}的年龄是{cat1.age}岁,花色是{cat1.color}")
cat1.speak()
cat1.think("现在要去哪")

cat2 = CuteCat("tom",3,"白色")
print(f"小猫{cat2.name}的年龄是{cat2.age}岁,花色是{cat2.color}")
cat2.speak()
cat2.think("我是谁")



# 小猫叫唤的次数和年龄成正比
