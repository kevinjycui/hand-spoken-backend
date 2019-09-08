import font_generator as fnt
import data_processor as dat

def main(dir):
    dat.setGlyphs(dir)
    fnt.configFont('font.json')