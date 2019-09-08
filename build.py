import image_processor
import data_processor
import font_generator

def main(dir):
    dirname = dir
    i = 0
    while os.path.exists('my_fonts/'+dirname):
        dirname = dir + str(i)
        i += 1
    print('Processing image source ...')
    image_processor.cropImages(dirname+'.jpg', dirname)
    print('Building data objects ...')
    data_processor.setGlyphs(dirname+'.jpg', dirname)
    print('Configuring custom font ...')
    font_generator.configFont('font.json', dir)

if __name__ == '__main__':
    print('Hand Spoken 1.0; PennApps Fall 2019. Making the art of handwriting accessible, one voice at a time.')
    print('Dryden, Jennifer\tCui, Kevin\nXu, Stephanie\t\tZhang, Alex')
    print('Launching Hand Spoken ...')
    # main()
    print('Process success!')