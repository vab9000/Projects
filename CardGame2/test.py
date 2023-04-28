"""Tests the game"""
import classes

deck = [
    classes.CorruptedFort(),
    classes.Garrison(),
    classes.TrainedSpecialist()
    ]
player = classes.Player(deck, 20, 'player')
player.battlefield.cards = [
    classes.CorruptedFort(),
    classes.Garrison(),
    classes.TrainedSpecialist()
]
game = classes.Game([player])
game.players[0].pass_priority(game)
game.players[0].pass_priority(game)
game.players[0].pass_priority(game)
player.battlefield.activate(0, player, game)
player.battlefield.activate(1, player, game)
player.battlefield.activate(2, player, game)
print(game)
