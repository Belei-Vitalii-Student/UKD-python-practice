from PIL import Image
from termcolor import colored
import os

IMAGE_FOLDER = 'image/'
FORMATTED_IMAGE_FOLDER = 'formatted/'
IMAGE_TYPE = '.png'
FORMATTED_TYPE = '.jpg'

if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

if not os.path.exists(FORMATTED_IMAGE_FOLDER):
    os.makedirs(FORMATTED_IMAGE_FOLDER)

availableFiles = list(filter(lambda x : x[-len(IMAGE_TYPE):] == IMAGE_TYPE, os.listdir(IMAGE_FOLDER)))


print('=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t')

if len(availableFiles) == 0:
    print(colored('No available files in image directory({}). Add some images in folder.'.format(IMAGE_FOLDER), 'red'))
else:
    print('Choose number of file for convert. Available only ' + IMAGE_TYPE + ' files.')
    print('Available files:')

    for x in range(len(availableFiles)):
        print('\t[{}] {}'.format(x, availableFiles[x]))
    
    number = -1
    while number not in(0, len(availableFiles)-1):
        print('Enter number of file for converting [{}-{}]:'.format(0, len(availableFiles)-1), end='')
        try:
            number = int(input())
        except:
            print(colored('Failed⚠️  Input data must be a number. Try again.', 'yellow'))
            continue

        if number not in(0, len(availableFiles)-1):
            print(colored('Failed⚠️  Input data must be a number in range({}-{}). Try again.'.format(0, len(availableFiles)-1), 'yellow'))

    IMAGE_NAME = availableFiles[number]
    FORMATED_NAME = FORMATTED_IMAGE_FOLDER + IMAGE_NAME + '(formatted)' + FORMATTED_TYPE

    image = Image.open(IMAGE_FOLDER + IMAGE_NAME)
    new_image = image.convert('RGB')
    new_image.save(FORMATED_NAME)

    print(colored('Successefully converting | 🖼️  | Created new file {}'.format(FORMATED_NAME), 'green'))

print('=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t=====\t')