import turtle as t
import Ali_Reza_Jafri_lab2_1 as aaa

def turtle_state():
    print(t.isdown())
    print(t.heading())
    print(t.xcor,"" , t.ycor)

def main():
    turtle_state()
    aaa.test_drive()
    turtle_state()
main()
