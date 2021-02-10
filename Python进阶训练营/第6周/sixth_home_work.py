# 背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。
#
# 这个类可以使用如下形式为动物园增加一只猫：
#
# 复制代码
# if __name__ == '__main__':
#     # 实例化动物园
#     z = Zoo('时间动物园')
#     # 实例化一只猫，属性包括名字、类型、体型、性格
#     cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
#     # 增加一只猫到动物园
#     z.add_animal(cat1)
#     # 动物园是否有猫这种动物
#     have_cat = hasattr(z, 'Cat')
# 具体要求：
#
# 定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
# 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。

from abc import ABCMeta, abstractmethod


# 元类的作用是控制如何创建类的？
class Animals(metaclass=ABCMeta):
    def __init__(self, name, category, size, nature):
        self.name = name
        self.category = category
        self.size = size
        self.nature = nature

    # property 属性这块的知识，掌握的比较薄弱
    @property
    def is_beast(self):
        if self.category == "食肉" and self.size in ("中", "高") and self.nature == "凶猛":
            return True
        else:
            return False


class Cat(Animals):
    sound = "喵喵~"

    def __init__(self, name, category, size, nature):
        super().__init__(name, category, size, nature)  # super 查了老师的课件，才会使用

    @property
    def is_pet(self):
        if self.is_beast:
            return "不适合作为宠物"
        else:
            return "适合作为宠物"


class Dog(Animals):
    sound = "汪汪~"

    def __init__(self, name, category, size, nature):
        super().__init__(name, category, size, nature)

    @property
    def is_pet(self):
        if self.is_beast:
            return "不适合作为宠物"
        else:
            return "适合作为宠物"


class Zoo(object):
    def __init__(self, name):
        self.name = name

    # 这块的内容完全不会，需要重新复习下课程的视频的资料
    def add_animal(self, specific_animal):
        if not hasattr(self, specific_animal.__class__.__name__):
            setattr(self, specific_animal.__class__.__name__, 1)


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    print(z)
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫1', '食肉', '小', '温顺')
    print(cat1.is_pet)

    # # 增加一只猫到动物园
    z.add_animal(cat1)
    # # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)
