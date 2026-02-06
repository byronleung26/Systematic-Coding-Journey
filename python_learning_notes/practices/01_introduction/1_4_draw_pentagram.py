#习题1.4：绘制多个起点相同但大小不同的五角星
import turtle as t
def draw_fiveStars(leng):
    count=1
    while count <=5:
        t.forward(leng)#向前走指定的像素
        t.right(144)#想右转144
        count +=1
    leng +=10#设置五角星的大小
    if leng <=100:
        draw_fiveStars(leng)
def main():
    t.penup()
    t.backward(100)
    t.pendown()
    t.pensize(2)
    t.pencolor('red')
    seqment=50
    draw_fiveStars(seqment)
    t.exitonclick()
if __name__=='__main__':
    main()