#!/usr/bin/env python
# coding=utf-8


from weakref import WeakKeyDictionary

from util import debug


class Event:

    """Superclasse para qualquer evento a ser
    despachado ao EventManager."""

    def __init__(self):
        self.name = "Evento generico"


class TickEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Ciclo de CPU"


class QuitEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Saida do programa"


class AppStartEvent(Event):
    def __init__(self, app):
        Event.__init__(self)
        self.name = "Inicio do programa"
        self.app = app

class GenerateRequestEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Gera um novo mundo"


class ResetEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Reinicia o mundo"


class WorldBuiltEvent(Event):
    def __init__(self, world):
        Event.__init__(self)
        self.name = "um mundo perigoso foi criado, tome cuidado..."
        self.world = world


class FoundDangerEvent(Event):
    def __init__(self, pos):
        Event.__init__(self)
        self.name = "perigo encontrado"
        self.pos = pos


class StepEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Proximo passo"


class ToggleAutoEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Trocar modo manual/auto"


class ToggleViewEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Trocar modo invisivel/visivel"


class HelpEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Exibir ajuda"


class WumpusDieEvent(Event):
    def __init__(self, pos):
        Event.__init__(self)
        self.name = "Wumpus morre"
        self.pos = pos


class PlayerForwardEvent(Event):
    def __init__(self, pos):
        Event.__init__(self)
        self.name = "Jogador move-se a frente"
        self.pos = pos


class ReadyEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Pronto"


class BusyEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Aguardando"


class PlayerTurnEvent(Event):
    direction_list = {'left': 0, 'right': 1}
    def __init__(self, direction, facing):
        Event.__init__(self)
        global direc
        if direction is PlayerTurnEvent.direction_list['left']:
            direc = "esquerda"
        elif direction is PlayerTurnEvent.direction_list['right']:
            direc = "direita"
        self.name = "Jogador move a %s" % direc
        self.direction = direction
        self.facing = facing


class PlayerPickEvent(Event):
    def __init__(self, pos):
        Event.__init__(self)
        self.name = "Jogador pegou o OURO !! ^_^"
        self.pos = pos


class PlayerShootEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Jogador atirou"


class PlayerPerceiveEvent(Event):
    def __init__(self, percept):
        Event.__init__(self)
        self.name = "Jogador percebeu %s" % percept
        self.percept = percept


class PlayerDieEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Jogador morreu @_@"


class EventManager:

    """Event Manager -- coordena a comunicação entre Model,
    View, and Controller."""

    def __init__(self):
        self.listeners = WeakKeyDictionary()

    def register_listener(self, listener):
        self.listeners[listener] = True

    def UnregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def post(self, ev):
        if not (isinstance(ev, TickEvent) or
                    isinstance(ev, StepEvent) or
                    isinstance(ev, HelpEvent) or
                    isinstance(ev, ToggleViewEvent) or
                    isinstance(ev, ToggleAutoEvent) or
                    isinstance(ev, BusyEvent) or
                    isinstance(ev, ReadyEvent)):
            debug(" ** " + ev.name)

        for listener in self.listeners.keys():
            if listener is None:
                del self.listeners[listener]
                continue
            listener.notify(ev)
