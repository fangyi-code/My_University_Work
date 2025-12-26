class Tool():
    def __init__(self,rocket):
        self.rocket = rocket

    def print_name(self):
        if self.rocket == '天问一号':
            print("发射时间:2020年")
            print("天问一号是我国自行研制的探测器，负责执行我国第一次自主火星探测任务。")
        elif self.rocket == '长征十一号运载火箭':
            print("发射时间:2020年")
            print("长征十一号是我国最早研制的一型四级全固体运载火箭，主要用于快速机动发射应急卫星、满足自然灾害、突发事件等应急情况下的卫星发射需求")
        else:
            print("发射时间:2020年")
            print("长征五号B运载火箭是专门为我国航天工程空间站建设而研制的一型新型运载火箭，以长征五号火箭为基础改进而成，是我国近地轨道运载能力最大的新一代运载火箭")


print("欢迎使用查询工具！输入'天问一号'或'长征十一号运载火箭'或'长征五号B运载火箭'可查询到对应信息。")

while True:
    rocket = input()
    if rocket == '天问一号' or rocket == '长征十一号运载火箭' or rocket == '长征五号B运载火箭':
        tool = Tool(rocket)
        result = tool.print_name()
    else:
        print("未查询到此航空器/火箭！请重新输入")