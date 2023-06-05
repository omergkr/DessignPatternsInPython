class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from {filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self.bitmap = None

    def draw(self):
        if not self.bitmap:
            self.bitmap = Bitmap(self.filename)
        self.bitmap.draw()


def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')


bmp = Bitmap('facepalm.jpg')  # Bitmap The image is loaded even though the draw method is not called
draw_image(bmp)

bmp = LazyBitmap('facepalm.jpg')  # Bitmap
draw_image(bmp)
