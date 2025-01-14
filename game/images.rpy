image street_day:
    "images/street.jpg"

image day_sun:
    "images/light/sun.jpg"
    blend "add"
    alpha 0.3
    
image sunrise:
    "images/light/sunrise.jpg"
    blend "multiply"

image late_night:
    "images/light/late_night.jpg"
    blend "multiply"

image pink:
    "images/light/pink.jpg"
    blend "add"
    alpha 0.3

image electric:
    "images/light/electric.jpg"
    blend "multiply"
    alpha 0.4

image students:
    im.Scale("images/students.png", 1100, 1100)
    matrixcolor BrightnessMatrix(0.4)
    
image students2:
    im.Scale("images/students2.png", 1300, 1300)
    matrixcolor BrightnessMatrix(0.4)
    

    

image smoke:
    "images/smoke/d (1).png"
    pause 0.02
    "images/smoke/d (2).png"
    pause 0.02
    "images/smoke/d (3).png"
    pause 0.02
    "images/smoke/d (4).png"
    pause 0.02
    "images/smoke/d (5).png"
    pause 0.02
    "images/smoke/d (6).png"
    pause 0.02
    "images/smoke/d (7).png"
    pause 0.02
    "images/smoke/d (8).png"
    pause 0.02
    "images/smoke/d (9).png"
    pause 0.02
    "images/smoke/d (10).png"
    pause 0.02
    "images/smoke/d (11).png"
    pause 0.02
    "images/smoke/d (12).png"
    pause 0.02
    "images/smoke/d (13).png"
    pause 0.02
    "images/smoke/d (14).png"
    pause 0.02
    "images/smoke/d (15).png"
    pause 0.02
    "images/smoke/d (16).png"
    pause 0.02
    "images/smoke/d (17).png"
    pause 0.02
    "images/smoke/d (18).png"
    pause 0.02
    "images/smoke/d (19).png"
    pause 0.02
    "images/smoke/d (20).png"
    pause 0.02
    "images/smoke/d (21).png"
    pause 0.02
    "images/smoke/d (22).png"
    pause 0.02
    "images/smoke/d (23).png"
    pause 0.02
    "images/smoke/d (24).png"
    pause 0.02
    "images/smoke/d (25).png"
    pause 0.02
    "images/smoke/d (26).png"
    pause 0.02
    "images/smoke/d (27).png"
    pause 0.02
    "images/smoke/d (28).png"
    pause 0.02
    "images/smoke/d (29).png"
    pause 0.02
    "images/smoke/d (30).png"
    pause 0.02
    "images/smoke/d (31).png"
    pause 0.02
    "images/smoke/d (32).png"
    pause 0.02
    "images/smoke/d (33).png"
    pause 0.02
    "images/smoke/d (34).png"
    pause 0.02
    "images/smoke/d (35).png"
    pause 0.02
    "images/smoke/d (36).png"
    pause 0.02
    "images/smoke/d (37).png"
    pause 0.02
    "images/smoke/d (38).png"
    pause 0.02
    "images/smoke/d (39).png"
    pause 0.02
    "images/smoke/d (40).png"
    pause 0.02
    "images/smoke/d (41).png"
    pause 0.02
    "images/smoke/d (42).png"
    pause 0.02
    "images/smoke/d (43).png"
    pause 0.02
    "images/smoke/d (44).png"
    pause 0.02
    "images/smoke/d (45).png"
    pause 0.02
    "images/smoke/d (46).png"
    pause 0.02
    "images/smoke/d (47).png"
    pause 0.02
    "images/smoke/d (48).png"
    pause 0.02
    "images/smoke/d (49).png"
    pause 0.02
    "images/smoke/d (50).png"
    pause 0.02
    "images/smoke/d (51).png"
    pause 0.02
    "images/smoke/d (52).png"
    pause 0.02
    "images/smoke/d (53).png"
    pause 0.02
    "images/smoke/d (54).png"
    pause 0.02
    "images/smoke/d (55).png"
    pause 0.02
    "images/smoke/d (56).png"
    pause 0.02
    "images/smoke/d (57).png"
    pause 0.02
    "images/smoke/d (58).png"
    pause 0.02
    "images/smoke/d (59).png"
    pause 0.02
    "images/smoke/d (60).png"
    pause 0.02
    "images/smoke/d (61).png"
    pause 0.02
    "images/smoke/d (62).png"
    pause 0.02
    

screen smoke:
    add "smoke"
    timer 3.0 action Hide("smoke")
    
image clock:
    "gui/clock/f (1).gif"
    pause 0.01
    "gui/clock/f (2).gif"
    pause 0.01
    "gui/clock/f (3).gif"
    pause 0.01
    "gui/clock/f (4).gif"
    pause 0.01
    "gui/clock/f (5).gif"
    pause 0.01
    "gui/clock/f (6).gif"
    pause 0.01
    "gui/clock/f (7).gif"
    pause 0.01
    "gui/clock/f (8).gif"
    pause 0.01
    "gui/clock/f (9).gif"
    pause 0.01
    "gui/clock/f (10).gif"
    pause 0.01
    "gui/clock/f (11).gif"
    pause 0.01
    "gui/clock/f (12).gif"
    pause 0.01
    "gui/clock/f (13).gif"
    pause 0.01
    "gui/clock/f (14).gif"
    pause 0.01
    "gui/clock/f (15).gif"
    pause 0.01
    "gui/clock/f (16).gif"
    pause 0.01
    "gui/clock/f (17).gif"
    pause 0.01
    "gui/clock/f (18).gif"
    pause 0.01
    "gui/clock/f (19).gif"
    pause 0.01
    "gui/clock/f (20).gif"
    pause 0.01
    repeat

image wait = Movie(channel="movie", play="videos/dance_wait.mp4")
image dance_1 = Movie(channel="movie", play="videos/dance_1.mp4")
image dance_2 = Movie(channel="movie", play="videos/dance_2.mp4")
image dance_3 = Movie(channel="movie", play="videos/dance_3.mp4")