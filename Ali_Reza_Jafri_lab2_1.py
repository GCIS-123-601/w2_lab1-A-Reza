import turtle as t

def test_drive():
    t.forward(100)
    t.right(87)
    t.setheading(127)
    t.up()
    t.down()
    t.goto(100, 100)
    t.home()
    t.circle(25)

def main():
    test_drive()

main()