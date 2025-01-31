define james_zoom__koef = 0.79
define dave_zoom_koef = 0.88
define lars_zoom__koef = 0.8
define kirk_zoom_koef = 0.72
define nick_zoom__koef = 0.7
define girl_zoom_koef = 0.7

image dave think = At('dave think demo', sprite_highlight('dave'))
image dave think demo:
    zoom dave_zoom_koef
    "images/dave think.png"
image dave side1 = At('dave side1 demo', sprite_highlight('dave'))
image dave side1 demo:
    zoom dave_zoom_koef
    "images/dave side1.png"
image dave side2 = At('dave side2 demo', sprite_highlight('dave'))
image dave side2 demo:
    zoom dave_zoom_koef
    "images/dave side2.png"
image dave angry = At('dave angry demo', sprite_highlight('dave'))
image dave angry demo:
    zoom dave_zoom_koef
    "images/dave angry.png"
image dave sad = At('dave sad demo', sprite_highlight('dave'))
image dave sad demo:
    zoom dave_zoom_koef
    "images/dave sad.png"
image dave smile = At('dave smile demo', sprite_highlight('dave'))
image dave smile demo:
    zoom dave_zoom_koef
    "images/dave smile.png"
image dave pink normal = At('dave pink normal demo', sprite_highlight('dave'))
image dave pink normal demo:
    zoom 0.77
    "images/dave pink normal.png"
image dave pink smile = At('dave pink smile demo', sprite_highlight('dave'))
image dave pink smile demo:
    zoom 0.77
    "images/dave pink smile.png"

image james blush = At("james blush demo", sprite_highlight('james'))
image james blush demo:
    "images/james blush.png"
    zoom james_zoom__koef
image james normal = At("james normal demo", sprite_highlight('james'))
image james normal demo:
    "images/james normal.png"
    zoom james_zoom__koef
image james smile = At("james smile demo", sprite_highlight('james'))
image james smile demo:
    "images/james smile.png"
    zoom james_zoom__koef
image james sad = At("james sad demo", sprite_highlight('james'))
image james sad demo:
    "images/james sad.png"
    zoom james_zoom__koef

image lars blush naked = At("lars blush naked demo", sprite_highlight('lars'))
image lars blush naked demo:
    "images/lars blush naked.png"
    zoom lars_zoom__koef
image lars angry = At("lars angry demo", sprite_highlight('lars'))
image lars angry demo:
    "images/lars angry.png"
    zoom lars_zoom__koef
image lars cow greeting = At("lars cow greeting demo", sprite_highlight('lars'))
image lars cow greeting demo:
    "images/lars cow greeting.png"
    zoom lars_zoom__koef
image lars please = At("lars please demo", sprite_highlight('lars'))
image lars please demo:
    "images/lars please.png"
    zoom lars_zoom__koef
image lars cow offense = At("lars cow offense demo", sprite_highlight('lars'))
image lars cow offense demo:
    "images/lars cow offense.png"
    zoom lars_zoom__koef
image lars normal = At("lars normal demo", sprite_highlight('lars'))
image lars normal demo:
    "images/lars normal.png"
    zoom lars_zoom__koef
image lars happy naked = At("lars happy naked demo", sprite_highlight('lars'))
image lars happy naked demo:
    "images/lars happy naked.png"
    zoom lars_zoom__koef
image lars irritated = At("lars irritated demo", sprite_highlight('lars'))
image lars irritated demo:
    "images/lars irritated.png"
    zoom lars_zoom__koef
image lars blush naked = At("lars blush naked demo", sprite_highlight('lars'))
image lars blush naked demo:
    "images/lars blush naked.png"
    zoom lars_zoom__koef
image lars smile = At("lars smile demo", sprite_highlight('lars'))
image lars smile demo:
    "images/lars smile.png"
    zoom lars_zoom__koef
image lars sad = At("lars sad demo", sprite_highlight('lars'))
image lars sad demo:
    "images/lars sad.png"
    zoom lars_zoom__koef

image nick sad = At("nick sad demo", sprite_highlight('nick'))
image nick sad demo:
    "images/nick sad.png"
    zoom nick_zoom__koef
image nick side = At("nick side demo", sprite_highlight('nick'))
image nick side demo:
    "images/nick side.png"
    zoom nick_zoom__koef
image nick normal = At("nick normal demo", sprite_highlight('nick'))
image nick normal demo:
    "images/nick normal.png"
    zoom nick_zoom__koef
image nick smile = At("nick smile demo", sprite_highlight('nick'))
image nick smile demo:
    "images/nick smile.png"
    zoom nick_zoom__koef

image kirk sad = At("kirk sad demo", sprite_highlight('kirk'))
image kirk sad demo:
    "images/kirk sad.png"
    zoom kirk_zoom_koef
image kirk normal = At("kirk normal demo", sprite_highlight('kirk'))
image kirk normal demo:
    "images/kirk normal.png"
    zoom kirk_zoom_koef

image gerard normal = At("gerard normal demo", sprite_highlight("sonya"))
image gerard normal demo:
    "images/gerard normal.png"
    zoom girl_zoom_koef

image gerard side = At("gerard side demo", sprite_highlight("sonya"))
image gerard side demo:
    "images/gerard side.png"
    zoom girl_zoom_koef


define narrator = Character(None,window_background="gui/textboxes/narrator.png")
define d = Character("дйв", color="#3a0a0a", image="dave", window_background="gui/textboxes/dave.png", callback=name_callback, cb_name="dave")
define l = Character("срал улей", color="#c45e9d", image="lars", window_background="gui/textboxes/lars.png",callback=name_callback, cb_name="lars")
define j = Character("джйм", color="#bac45e", image="james", window_background="gui/textboxes/james.png",callback=name_callback, cb_name="james")
define n = Character("вкид менза", color="#575757", image="nick", window_background="gui/textboxes/neutral.png",callback=name_callback, cb_name="nick")
define k = Character("кириешка", color="#201212", image="kirk", window_background="gui/textboxes/neutral.png",callback=name_callback, cb_name="kirk")
define board = Character(kind=nvl, what_color="#fff", what_font="gui/code2.ttf")
define se = Character("1000-7", color="#868686", image="sonya", window_background="gui/textboxes/neutral.png",callback=name_callback, cb_name="sonya")
