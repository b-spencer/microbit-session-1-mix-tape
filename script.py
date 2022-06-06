def on_button_pressed_a():
    if state == 3:
        basic.show_arrow(ArrowNames.WEST)
    elif state == 4:
        sprite.move(-1)
        music.play_tone(262, music.beat(BeatFraction.SIXTEENTH))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if state == 4:
        if music.volume() == 0:
            music.set_volume(220)
        else:
            music.set_volume(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if state == 3:
        basic.show_arrow(ArrowNames.EAST)
    elif state == 4:
        sprite.move(1)
        music.play_tone(392, music.beat(BeatFraction.SIXTEENTH))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    global state
    game.pause()
    basic.clear_screen()
    state = state + 1
    if state == 3:
        basic.show_leds("""
            . # # # .
                        # . . . #
                        . . # # .
                        . . . . .
                        . . # . .
        """)
    elif state == 4:
        music.set_volume(0)
        game.resume()
    elif state > 4:
        state = 0
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

sprite: game.LedSprite = None
state = 0
state = 0
sprite = game.create_sprite(2, 2)
music.set_volume(0)
game.pause()
basic.show_icon(IconNames.YES)
basic.clear_screen()

def on_forever():
    if state == 1:
        basic.show_icon(IconNames.HEART)
    elif state == 2:
        basic.show_icon(IconNames.SMALL_SQUARE)
        if state == 2:
            basic.show_icon(IconNames.SQUARE)
basic.forever(on_forever)
