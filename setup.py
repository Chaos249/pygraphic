import pyglet

window = pyglet.window.Window(800, 400, "Test")

def draw_label(name, x_int, y_int):
	label = pyglet.text.Label(name, x = x_int, y = y_int)
	return label

@window.event
def on_draw():
	window.clear()
	draw_label("test label", 100, 100).draw()

if __name__ == "__main__":
	pyglet.app.run()
	print("this shit should work")

