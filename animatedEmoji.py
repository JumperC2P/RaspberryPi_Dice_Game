from sense_hat import SenseHat
from time import sleep


class AnimatedEmoji:

    def __init__(self):
        # initiate 3 images path
        self.__1stPicture = 'images/spider.png'
        self.__2ndPicture = 'images/deadpool.png'
        self.__3rdPicture = 'images/volleyball.png'

    def start(self):
        # create an object of SenseHat
        sense = SenseHat()

        # use while loop to display 3 images.
        while True:
            sense.load_image(self.__1stPicture)
            sleep(3)
            sense.load_image(self.__2ndPicture)
            sleep(3)
            sense.load_image(self.__3rdPicture)
            sleep(3)


if __name__ == '__main__':
    animatedEmoji = AnimatedEmoji()
    animatedEmoji.start()
