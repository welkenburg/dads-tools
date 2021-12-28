from pynput.mouse import Listener

def mouse_pressed(x, y, button, pressed):
	if pressed:
		print(f'{x=}, {y=}')

with Listener(on_click=mouse_pressed) as listener:
	listener.join()