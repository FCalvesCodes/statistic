# -*- coding: utf-8 -*-


import os

def terminal_size(string, caractere="" ):
	""" Retorna string ajustada com o tamanho do terminal."""
	size_terminal = os.get_terminal_size().columns
	size_string = len(string)
	size = size_terminal - size_string
	return caractere*(size//2)+string+caractere*(size//2)