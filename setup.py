import pyglet

window = pyglet.window.Window(800, 400, "Modus Operandi")

def draw_label(name, x_int, y_int):
	label = pyglet.text.Label(name, x = x_int, y = y_int)
	return label

def draw_image(img):
	image = pyglet.resource.image(img)
	return image

#final draw funciton
@window.event
def on_draw():
	window.clear()
	image = draw_image("test.png")
	image.blit(182, 0) # these are cartesian coordinates
	draw_label("test label", 50, 100).draw()

if __name__ == "__main__":
	pyglet.app.run()

