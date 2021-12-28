import pandas as pd
import SendKeys
from pynput.mouse import Button, Controller

moves = []
mouse = Controller()

def moveNclick(pos):
	mouse.position = pos
	mouse.click(Button.Left, 1)

def task(**row_values):
	moveNclick(moves[0])
	moveNclick(moves[1])
	moveNclick(moves[2])


df = pd.read_csv(r'path.csv')
rows,cols = df.shape
for i in range(rows):
	cell1,cell2 = df.loc[i,["cell1","cell2"]]
	task(cell1)