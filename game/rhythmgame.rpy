init python:
    import pickle

    SPEED = 10
    BORDER_UP = 150
    BORDER_HEIGHT = 30
    POSITION_A = 1920 / 6 * 1 + 25
    POSITION_B = 1920 / 6 * 2
    POSITION_C = 1920 / 6 * 3
    POSITION_D = 1920 / 6 * 4
    POSITION_E = 1920 / 6 * 5
    POSITION_F = 1920 / 6 * 6 - 25

    MAX_NOTES_PER_TYPE = 4  # Максимум нот одного типа на экране

    class Note:
        def __init__(self, identity, strumTime, position):
            self.idnum = identity
            self.strum = strumTime
            self.active = False
            self.num = position  # Номер позиции как число
            self.image = None

            # Устанавливаем изображение и стартовую позицию
            if position == 1:
                self.image = 'images/notes/a.png'
                self.position = (POSITION_A, -100)
            elif position == 2:
                self.image = 'images/notes/b.png'
                self.position = (POSITION_B, -100)
            elif position == 3:
                self.image = 'images/notes/c.png'
                self.position = (POSITION_C, -100)
            elif position == 4:
                self.image = 'images/notes/d.png'
                self.position = (POSITION_D, -100)
            elif position == 5:
                self.image = 'images/notes/e.png'
                self.position = (POSITION_E, -100)
            elif position == 6:
                self.image = 'images/notes/f.png'
                self.position = (POSITION_F, -100)

        def reset(self, strumTime):
            self.strum = strumTime
            self.active = True
            self.position = (self.position[0], -100)

        def update_position(self):
            if self.active:
                self.position = (self.position[0], self.position[1] + SPEED)
                if self.position[1] > 500:  # Если нота вышла за экран
                    self.active = False
            print(self.position)

    class RhythmGame:
        def __init__(self):
            self.pools = {i: [] for i in range(1, 7)}  # Пул для нот от 1 до 6
            self.notes = []
            self.next_note_idx = 0

            # Загружаем карту битов
            absolute_path = os.path.abspath("pytarded/game/audio/pickled/notes")
            beatarray = pickle.load(open(absolute_path, "rb"))

            try:
                beatmap, ending_time = beatarray
            except:
                print('Unable to read audio file')
                return

            for idx, beat in enumerate(beatmap):
                timing = beat['time']
                position = beat['position']
                self.notes.append({"strum": timing, "position": position})

            self.note_images = {
                1: Image("images/notes/a.png"),
                2: Image("images/notes/b.png"),
                3: Image("images/notes/c.png"),
                4: Image("images/notes/d.png"),
                5: Image("images/notes/e.png"),
                6: Image("images/notes/f.png"),
            }

        def get_note_from_pool(self, note_type, strumTime):
            pool = self.pools.get(note_type)  # Пул с числом
            # Если есть неактивная нота в пуле
            for note in pool:
                if not note.active:
                    note.reset(strumTime)
                    return note

            # Если в пуле недостаточно нот, создаём новую
            if len(pool) < MAX_NOTES_PER_TYPE:
                new_note = Note(len(pool), strumTime, note_type)
                pool.append(new_note)
                return new_note

            return None  # Если лимит превышен

    def update_notes():
        time = renpy.music.get_pos()
        game = store.rhythm_game

        if not time:
            renpy.music.play("audio/music/barabere.ogg", channel="music")
            renpy.restart_interaction()
            return

        while game.next_note_idx < len(game.notes):
            note_data = game.notes[game.next_note_idx]
            if note_data["strum"] / 100000.0 <= time / 100.0:
                spawned_note = game.get_note_from_pool(note_data["position"], note_data["strum"])
                if spawned_note:
                    spawned_note.active = True
                game.next_note_idx += 1
            else:
                break

        # Обновляем позиции активных нот
        for pool in game.pools.values():
            for note in pool:
                note.update_position()
        SetVariable("game", game)
    

transform note_position(x, y):
    xpos x
    ypos y



screen rhythm_game(game):
    zorder 10
    timer 0.016 action Function(update_notes) repeat True
    window:
        style "default"
        text "нажимай на цифры на клавиатуре лошок!!" xalign 0.5 yalign 0.0
        # Отображаем активные ноты
        for note_type, notes in game.pools.items():
            for note in notes:
                imagebutton:
                    idle Image(note.image)
                    hover Image("images/notes.pressed.png")
                    xpos int(note.position[0])
                    ypos int(note.position[1])

