from turtle import*
color('blue','yellow') #اولی رنگ بدنه ست دومیه رنگ داخلش
begin_fill()
while True:
    forward(200)
    left(170)

    if abs(pos()) < 1:  #abs نشونه قدرمطلقه
        # pos موقعیت کنونی اون فلشه ست 
        # pos() in turtle python مدل سرچ
        break
end_fill()
done()
# میتونی سرعت حرکتش رو تعیین کنی