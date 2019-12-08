import tv

tele = tv.TV()
tele.show_status()
tele.on()
tele.show_status()
tele.set_channels('TVP1')
tele.set_channels('TVP2')
tele.set_channels('Polsat')
tele.set_channels('TVN')
tele.set_channels('Filmbox')
tele.set_channels('PoloTV')
tele.set_channels('DisneyXD')

tele.turn_up()
tele.set_channel(6)
tele.show_status()

tele.turn_up()
tele.turn_up()
tele.set_channel(7)
tele.show_status()

tele.turn_down()
tele.set_channel(8)
tele.show_status()