import random
import tkinter
class RandomBall():
    """
    定义球的运动
    """
    def __init__(self, canvas, scrnwidth, scrnhight):
        '''
        canvas:画布，所有的内容都应该在画布上呈现出来此处通过这个变量传入
        scrnwidth/scrnhight>屏幕的宽高
        '''
        self.canvas = canvas
        self.xpos = random.randint(10,int(scrnwidth)-20)
        #球出现的初始位置的随机、
        # xpos 表示球出现的x坐标
        self.ypos = random.randint(10,int(scrnwidth)-10)
        # ypos 表示球出现的y的坐标
        self.xvelocity = random.randint(4,20)
        #定义球的运动速度
        #模拟运动：不断的擦掉原画面，然后在一个新的地方再从此你绘制
        #此处xvolocity 模拟的是x方向的运动
        self.yvelocity = random.randint(4, 20)
        #yvelocity 表示的是y轴的运动
        self.scrnwidth = scrnwidth
        #宽
        self.scrnhight = scrnhight
        #高
        #定义屏幕的大小
        self.radius = random.randint(20,120)
        #定义球的大小,随机
        #此处用球的半径来表示球的大小
        c = lambda: random.randint(0,255)
        self.color = '#%02x%02x%02x'%(c(),c(),c())

    def create_ball(self):
        '''
        用构造函数定义的变量值，在canvas上画出一个球
        '''
        #tkinter没有画圆形的函数，只有画椭圆的函数
        #在一个长方形内画椭圆，我们只需要定义长方形左上角和右下角就好
        #求两个坐标的方法是，已知圆心的坐标
        x1 =  self.xpos - self.radius
        y1 =  self.ypos - self.radius
        x2 =  self.xpos + self.radius
        y2 =  self.ypos + self.radius
        #在有两个对角坐标的前提先，可以进行画圆
        self.item = self.canvas.create_oval(x1,y1,x2,y2, fill=self.color, outline=self.color)
    def move_ball(self):
        # 移动球的时候，需要控制球的方向
        #在画布上挪移图形
        #每次移动后，球都有一个新的坐标
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        #撞墙的算法
        #右边墙
        if self.xpos + self.radius+1 >= self.scrnwidth:
            self.xvelocity = -self.xvelocity
        #左边墙
        if self.xpos+1 <= self.radius :
            self.xvelocity = -self.xvelocity
        #下边墙
        if self.ypos + self.radius+1 >= self.scrnwidth:
            self.yvelocity = -self.yvelocity
        #上边墙
        if self.ypos+1 <= self.radius :
            self.yvelocity = -self.yvelocity
        self.canvas.move(self.item,self.xvelocity,self.yvelocity)


class ScreenSaver():
    """
    定义屏保的类
    可以被启动
    """
    #如何装随机产生的球
    balls = []
    def __init__(self): #每次启动的球的数量都是随机的
        self.num_balls = random.randint(6,20)
        self.root = tkinter.Tk()
        #取消边框
        self.root.overrideredirect(1)
        #self.root.attributes('-alpha', 0.3)
        #任何鼠标移动都需要自动取消
        self.root.bind('<Motion>',self.myquit)
        # self.root.bind('<Motion>', self.myquit)
        w,h = self.root.winfo_screenwidth(),self.root.winfo_screenheight()
        self.canvas = tkinter.Canvas(self.root,width=w,height=h,)#bg='#00FFFF'
        self.canvas.pack()
        #在画布上画球
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas,scrnwidth=w,scrnhight=h)
            ball.create_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for  ball in  self.balls:
            ball.move_ball()
        #after是200 毫秒后启动一个函数，需要启动的函数是第二个参数
        self.canvas.after(20,self.run_screen_saver)
    def myquit(self,e):
        #此处只是利用事件的处理机制
        #实际上并不关心事件的类型
        self.root.destroy()

if __name__ == "__main__":
    #屏保启动
   ScreenSaver()

