"Runs the game"
import tkinter
import classes


deck = [
    classes.TrainedSpecialist(),
    classes.Ruins(),
    classes.Garrison()
    ]
player = classes.Player(deck, 20, 'player')
game = classes.Game([player])
root = tkinter.Tk()
root.state("zoomed")
app = classes.UI(game, root)
app.mainloop()
