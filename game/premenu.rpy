init python:
    class Chapter:
        def __init__(self, title, num):
            self._status = persistent.nums[num-1] # Default status
            self.num = num
            self.title = title

        @property
        def status(self):
            return persistent.nums[self.num-1]

        @status.setter
        def status(self, value):
            persistent.nums[self.num-1]=value
            renpy.save_persistent() 
            
            print("SET")  # This should print when the status is set

    def clear_variables():
        pass

    def make_start_label(num):
        return "start" + str(num)




screen bg_viewport():
    zorder 1
    viewport id "main":
        xysize (config.screen_width, config.screen_height)
        child_size (3000, 1280)
        edgescroll (150, 1280)
        xinitial 150
        yinitial 150
        draggable True
        grid 3 2:
            for i in range(6):
                add "gui/premenu/seamless.png"

screen premenu():
        tag menu
        modal True
        zorder 2
        use bg_viewport()
        vpgrid:
            cols 3
            spacing 50
            draggable True
            mousewheel True
            
            for i in range(len(chapters)):
                window:
                    style "default"
                    ypos renpy.random.choice([-75, 75])
                    background im.Scale("gui/premenu/cloud.png", 1300, 1300)
                    textbutton chapters[i].title:
                        ypos 800
                        xpos 250
                        text_size gui.welcome_title_text_size
                        text_idle_color "#f700ff"
                        text_hover_color "#696200"
                        action If(chapters[i].status==1, Start(make_start_label(chapters[i].num)), If(chapters[i].status==2, ShowMenu("load"),  Confirm("Вы уже прошли эту часть истории. Хотите переформатировать диск?", yes=clear_variables, no=ShowMenu('main'))))
                    add im.Scale(f"gui/premenu/part{chapters[i].num}.jpg", 400, 400) xpos 450 ypos 400
                    hbox:
                        xpos 300
                        ypos 850
                        if chapters[i].status == 1:
                            add im.Scale("gui/premenu/whole.png", 100, 120)
                            text "ЕЩЁ НЕ ПРОЙДЕНА" ypos 50
                        elif chapters[i].status == 2:
                            add im.Scale("gui/premenu/eaten.png", 100, 120)
                            text "В ПРОЦЕССЕ" ypos 50
                        elif chapters[i].status == 3:
                            add im.Scale("gui/premenu/bite.png", 100, 120)
                            text "ЗАВЕРШЕНО" ypos 50