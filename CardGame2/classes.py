"""Base classes"""
import random
import tkinter


class UI(tkinter.Frame):
    def __init__(self, game, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.game = game
        self.stack = tkinter.Label(self)
        self.stack["text"] = "Stack: " + str(game.stack)
        self.stack.pack()
        self.input = tkinter.Entry(self)
        self.question = tkinter.Label(self)
        self.question["text"] = "Index:"
        self.actions = [tkinter.Button(self), tkinter.Button(self), tkinter.Button(self), tkinter.Button(self)]
        self.actions[0]["text"] = "CONCEDE"
        self.actions[0]["command"] = self.concede
        self.actions[1]["text"] = "PASS"
        self.actions[1]["command"] = self.pass_priority
        self.actions[2]["text"] = "PLAY"
        self.actions[2]["command"] = self.play
        self.actions[3]["text"] = "ACTIVATE"
        self.actions[3]["command"] = self.activate
        for action in self.actions:
            action.pack()
        self.question.pack()
        self.input.pack()
        self.cards = list()
        self.phase = tkinter.Label(self)
        self.phase["text"] = "Phase:" + str(game.phase)
        self.phase.pack()
        for player in game.players:
            button = tkinter.Button(self)
            button["text"] = player.name
            button["command"] = player.player_window
            button.pack()

    def concede(self):
        self.master.destroy()

    def pass_priority(self):
        self.game.priority.pass_priority(self.game)
        self.refresh()

    def play(self):
        index = self.input.get()
        self.game.priority.hand.play(int(index), self.game.priority, self.game)
        self.refresh()

    def activate(self):
        index = self.input.get()
        self.game.priority.battlefield.activate(int(index), self.game.priority, self.game)
        self.refresh()

    def refresh(self):
        self.phase["text"] = "Phase:" + str(self.game.phase)
        self.stack["text"] = "Stack: " + str(self.game.stack)


class Game:
    def __init__(self, players):
        self.players = players.copy()
        self.turn = self.players[0]
        self.turn_num = 0
        self.stack = list()
        self.priority = self.players[0]
        self.priority_number = 0
        self.phase = 1

    def __str__(self):
        ret_str = ""
        i = 0
        ret_str += ("Stack:" + str(self.stack) + "\n")
        ret_str += ("Priority:" + str(self.priority) + "\n")
        ret_str += ("Phase:" + str(self.phase) + "\n")
        for player in self.players:
            ret_str += ("Player: " + str(i) + "\n")
            ret_str += ("Name: " + player.name + "\n")
            ret_str += ("Hand: " + str(player.hand.cards) + "\n")
            ret_str += ("Battlefield: " + str(player.battlefield.cards) + "\n")
            ret_str += ("Graveyard: " + str(player.graveyard.cards) + "\n")
            ret_str += ("Exile: " + str(player.exile.cards) + "\n")
            ret_str += ("Deck: " + str(player.deck.cards) + "\n")
            ret_str += ("Life Total: " + str(player.life_total) + "\n")
            ret_str += ("Mana Pool: " + str(player.mana_pool) + "\n")
            i += 1
        return ret_str

    def pass_priority(self):
        self.priority_number += 1
        if self.priority_number >= len(self.players):
            if len(self.stack) > 0:
                self.resolve()
            else:
                self.phase += 1
                for player in self.players:
                    player.mana_pool = []
                if self.phase > 9:
                    self.phase = 1
                    self.turn_num += 1
                    for player in self.players:
                        for card in player.battlefield.cards:
                            if isinstance(card, Creature):
                                if card.check_death():
                                    player.battlefield.remove(card)
                                    player.graveyard.append(card)
                    if self.turn_num >= len(self.players):
                        self.turn_num = 0
                        self.turn = self.players[self.turn_num]
                    for permanent in self.turn.battlefield.cards:
                        permanent.tapped = False
                        permanent.sick = False
                    self.turn.played_land = False
                elif self.phase == 3:
                    self.turn.draw_card()
            self.priority_number = 0
            self.priority = self.players[self.priority_number]

    def resolve(self):
        self.stack[-1][0].resolve(self.stack[-1][1])
        self.stack.pop(-1)


class Hand:
    def __init__(self):
        self.cards = list()

    def play(self, index, player, game):
        self.cards[index].play(player, game)
        self.cards.pop(index)

    def new_window(self):
        window = tkinter.Tk()
        for card in self.cards:
            label = tkinter.Label(window)
            label["text"] = card.name
            label.pack()


class Battlefield:
    def __init__(self):
        self.cards = list()

    def activate(self, index, player, game):
        abilities = self.cards[index].get_abilities()
        if len(abilities) == 1:
            abilities[0][0](player, game)
        elif len(abilities) == 0:
            pass
        else:
            i = 0
            for tup in abilities:
                print(str(i) + ": " + tup[1])
                i += 1
            ability = input("Ability to activate:")
            abilities[int(ability)][0](player, game)

    def new_window(self):
        window = tkinter.Tk()
        for card in self.cards:
            label = tkinter.Label(window)
            label["text"] = card.name
            label.pack()


class Deck:
    def __init__(self, cards):
        self.cards = cards.copy()

    def shuffle(self):
        random.shuffle(self.cards)


class Graveyard:
    def __init__(self):
        self.cards = list()


class Exile:
    def __init__(self):
        self.cards = list()


class Player:
    def __init__(self, deck, life_total, name):
        self.deck = Deck(deck.copy())
        self.hand = Hand()
        self.battlefield = Battlefield()
        self.graveyard = Graveyard()
        self.life_total = life_total
        self.exile = Exile()
        self.dead = False
        self.played_land = False
        self.mana_pool = list()
        self.name = name
        for card in self.deck.cards:
            card.owner = self

    def draw_card(self):
        if len(self.deck.cards) == 0:
            self.dead = True
        else:
            self.hand.cards.append(self.deck.cards[0])
            self.deck.cards.pop(0)

    def pass_priority(self, game):
        if game.priority.name == self.name:
            game.pass_priority()

    def player_window(self):
        window = tkinter.Tk()
        label = tkinter.Label(window)
        label["text"] = self.mana_pool
        label.pack()
        button = tkinter.Button(window)
        button["text"] = "Hand"
        button["command"] = self.hand.new_window
        button.pack()
        button = tkinter.Button(window)
        button["text"] = "Battlefield"
        button["command"] = self.battlefield.new_window
        button.pack()


class Card:
    def __init__(self):
        self.owner = None
        self.img = None

    def getFrame(self):
        return self.img


class Permanent(Card):
    def __init__(self):
        Card.__init__(self)
        self.abilities = list()
        self.tapped = False
        self.sick = True

    def get_abilities(self):
        return self.abilities


class Creature(Permanent):
    def __init__(self):
        self.tapped = False
        self.mana_cost = [0]
        self.name = ""
        self.flash = False
        self.targetable = True
        self.power = 0
        self.toughness = 0
        self.damage = 0
        Permanent.__init__(self)

    def play(self, player, game):
        if (
            (game.turn == player) and
            (self.flash or (game.phase == 4 or game.phase == 8))
        ):
            window = tkinter.Tk()
            mana_pool = player.mana_pool.copy()
            castable = True
            label = tkinter.Label(window)
            label["text"] = 'Casting ' + self.name
            label.pack()
            waiting = tkinter.IntVar(window)
            mana_text = tkinter.Label(window, text=("Mana Pool: " + str(mana_pool)))
            mana_text.pack()
            inp_box = tkinter.Entry(window)
            inp_box.pack()
            button = tkinter.Button(window, text="Submit", command=lambda: waiting.set(1))
            button.pack()
            for mana in self.mana_cost[1]:
                label["text"] = 'Pay ' + mana
                mana_text["text"] = "Mana Pool: " + str(mana_pool)
                button.wait_variable(waiting)
                inp = inp_box.get()
                if inp == 'NO':
                    castable = False
                    break
                elif mana_pool[int(inp)] != mana:
                    castable = False
                    break
                else:
                    mana_pool.pop(int(inp))
            if castable:
                i = 0
                while i < self.mana_cost[0]:
                    label["text"] = 'Pay Generic'
                    mana_text["text"] = "Mana Pool: " + str(mana_pool)
                    button.wait_variable(waiting)
                    inp = inp_box.get()
                    if inp == 'NO':
                        castable = False
                        break
                    else:
                        mana_pool.pop(int(inp))
                    i += 1
            if castable:
                game.stack.append((self, player))
                player.mana_pool = mana_pool.copy()
            else:
                player.hand.cards.append(self)
        else:
            player.hand.cards.append(self)
        window.destroy()

    def resolve(self, player):
        player.battlefield.cards.append(self)

    def check_death(self):
        if self.damage >= self.toughness:
            return True


class TrainedSpecialist(Creature):
    def __init__(self):
        Creature.__init__(self)
        self.mana_cost = [1, ['Y']]
        self.power = 2
        self.toughness = 1
        self.name = "Trained Specialist"
        self.targetable = False
        self.abilities = [(self.deal_damage, "Deal 1 damage to any target")]

    def deal_damage(self, player, game):
        if not self.sick:
            if not self.tapped:
                self.tapped = True
                targets = list()
                for players in game.players:
                    targets.append(players)
                    for card in players.battlefield.cards:
                        if isinstance(card, Creature):
                            if card.targetable:
                                targets.append(card)
                print(targets)
                inp = input("Index:")
                if isinstance(targets[int(inp)], Player):
                    targets[int(inp)].life_total -= 1
                else:
                    if targets[int(inp)].targetable:
                        targets[int(inp)].damage += 1
                    else:
                        print("Invalid target")
                        self.tapped = False
        return player


class Land(Permanent):
    def __init__(self):
        Permanent.__init__(self)

    def play(self, player, game):
        if (
            (game.turn == player)
            and (not player.played_land)
            and (game.phase == 4 or game.phase == 8)
        ):
            player.battlefield.cards.append(self)
            player.played_land = True
        else:
            player.hand.cards.append(self)
        return game


class Ruins(Land):
    def __init__(self):
        Land.__init__(self)
        self.abilities = [(self.add_purple_mana, "Add P")]
        self.name = "Ruins"

    def add_purple_mana(self, player, game):
        if not self.tapped:
            self.tapped = True
            player.mana_pool.append('P')
        return game


class Garrison(Land):
    def __init__(self):
        Land.__init__(self)
        self.abilities = [(self.add_yellow_mana, "Add Y")]
        self.name = "Garrison"

    def add_yellow_mana(self, player, game):
        if not self.tapped:
            self.tapped = True
            player.mana_pool.append('Y')
        return game


class Lake(Land):
    def __init__(self):
        Land.__init__(self)
        self.abilities = [(self.add_blue_mana, "Add Y")]

    def add_blue_mana(self, player, game):
        if not self.tapped:
            self.tapped = True
            player.mana_pool.append('B')
        return game


class Marsh(Land):
    def __init__(self):
        Land.__init__(self)
        self.abilities = [(self.add_gray_mana, "Add Y")]

    def add_gray_mana(self, player, game):
        if not self.tapped:
            self.tapped = True
            player.mana_pool.append('G')
        return game


class CorruptedFort(Ruins, Garrison):
    def __init__(self):
        Ruins.__init__(self)
        Garrison.__init__(self)
        self.tapped = True
        self.abilities = [
            (self.add_purple_mana, "Add P"),
            (self.add_yellow_mana, "Add Y")
        ]
        self.name = "Corrupted Fort"
