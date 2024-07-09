from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
import os

class ElJulyApp(App):
    def build(self):
        carousel = Carousel(direction='bottom')

        imgFolderPath = os.path.join(os.getcwd(), 'images')
        totalImages = len(os.listdir(imgFolderPath))

        imgPathList = []
        for x in range(totalImages):
            imgPathList.append(imgFolderPath + '/' + f'image{x}' + '.jpg')

        for imgPath in imgPathList:
            i = Image(source=imgPath)
            carousel.add_widget(i)
        return carousel

if __name__ == "__main__":
    ElJulyApp().run()
