import image_processor
import data_processor
import font_generator

def main(dir):
    dirname = dir
    i = 0
    while os.path.exists('my_fonts/'+dirname):
        dirname = dir + str(i)
        i += 1
    image_processor.cropImages(dirname+'jpg', dirname)
    data_processor.setGlyphs(dirname+'jpg', dirname)
    font_generator.configFont('font.json', dir)