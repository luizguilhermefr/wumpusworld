#!/usr/bin/env python
# coding=utf-8


from event import EventManager
from view import MainFrame
from controller import *
from app import App
from ai import Agent

def main():
    """Início do sistema"""
    ev_manager = EventManager()

    main_frame = MainFrame(ev_manager)
    spinner = CPUSpinnerController(ev_manager)
    keybd = KeyboardController(ev_manager)
    ai = Agent(ev_manager)
    app = App(ev_manager)

    spinner.run()


if __name__ == "__main__":
    main()
