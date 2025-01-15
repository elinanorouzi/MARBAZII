#کتابخانه هاي مورد نياز
import turtle
import time
import random
#کنترل سرعت بازي
delay = 0.1
score = 0
high_score = 0
#صفحه بازي
wn = turtle.Screen()
wn.title("mar baziii")
wn.bgcolor("green")
wn.setup(600, 600)
wn.tracer(0)
#ايجاد سر مار
head = turtle.Turtle()
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"
#ايجاد غذا
food = turtle.Turtle()
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0, 100)
#نمايش امتياز
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center", font=("candara", 24, "bold"))

#ليست ذخيره کردن بدن مار
segments = []

#تابع براي جهت مار
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

#حرکت سر مار
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#کليد هاي کنترل
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#حلقه براي بروزرساني مداوم صفحه بازي
while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        #ريست شدن بازي
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        
        score = 0
        delay = 0.1
    #خوردن غذا و افزايش طول
    if head.distance(food) < 20:
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

        #جابجايي غذا
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        #چاپ امتياز در بالاي صفحه
        score += 10
        if score > high_score:
            high_score = score
        delay -= 0.001
    #حرکت بدن مار
    for index in range(len(segments) - 1, 0, -1):
        #بدست اوردن موقعيت قبلي بدن مار
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    #منتقل کردن اولين بخش بدن مار به موقعيت سر مار
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    #بررسي کردن جهت فعلي مار
    move()

    pen.clear()
    pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
    #مديريت تاخير
    time.sleep(delay)
#جهت باز ماندن برنامه و اجراي تغييرات
wn.mainloop()
