strip = neopixel.create(DigitalPin.P16, 24, NeoPixelMode.RGB_RGB)
strip.set_brightness(255)
strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.RED))
strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.ORANGE))
strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.YELLOW))
strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.GREEN))
strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.BLUE))
strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.INDIGO))
strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.VIOLET))
strip.set_pixel_color(8, neopixel.colors(NeoPixelColors.PURPLE))
strip.set_pixel_color(9, neopixel.colors(NeoPixelColors.WHITE))
strip.set_pixel_color(10, neopixel.colors(NeoPixelColors.BLACK))
strip.show()

def on_every_interval():
    for index in range(2):
        basic.show_leds("""
            # . . . .
                        # . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . # # . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . # # .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . # #
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . #
                        . . . . #
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . #
                        . . . . #
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . #
                        . . . . #
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . #
                        . . . . #
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . # #
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . # # .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . # # . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
                        # . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . . . .
                        # . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        # . . . .
                        # . . . .
                        . . . . .
                        . . . . .
        """)
    for index2 in range(3):
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . # .
                        . . . # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . # # .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . # . . .
                        . # . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # . . .
                        . # . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . # # . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . # # .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . # .
                        . . . # .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . # .
                        . . . # .
                        . . . . .
        """)
loops.every_interval(500, on_every_interval)

def on_forever():
    strip.rotate(1)
    strip.set_brightness(randint(20, 255))
    strip.show()
    basic.pause(100)
basic.forever(on_forever)
