#!/usr/bin/env python
# coding=utf-8

import os

#
# definição das cores
#

color = {
    'gray': (100, 100, 100),
    'black': (0, 0, 0),
    'red': (250, 0, 0),
    'green': (0, 250, 0),
    'light_green': (20, 60, 20),
    'background': (30, 30, 30),
    'urgent': (150, 50, 50),
    'white': (255, 255, 255),
    'help': (153, 255, 51),
    'info': (153, 255, 51),
    'danger': (60, 30, 30)
    }

instruction = "H => ajuda, ESPACO => passo-a-passo, Q => sair"

help = """
  Instrucoes

   H: Exibir ajuda
   Espaco: Passo-a-passo
   C: Alterar modo manual/auto
   V: Visualizar todo o mapa
   R: Reiniciar
   Q: Sair
   
   A luz no canto inferior
   esquerdo, quando vermelha,
   demonstra ocupado e,
   quando verde, pronto para
   o proximo passo.
"""

# frames por segundo
fps = 20

# luz de status
light_flick_ticks = 5

# No modo automático, quantos ciclos aguardar antes de gerar o próximo
# passo
wait_ticks = 10

status_font = (os.path.join('font', 'FreeMono.ttf'), 23)
help_font = status_font
