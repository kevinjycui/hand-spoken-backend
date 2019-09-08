import json
import os

def setGlyphs(src='test_glyphs'):
    with open('font.json') as json_file:
        data = json.load(json_file)
    i = 0
    for key in data['glyphs'].keys():
        if os.path.exists('my_fonts/' + src + '/'+str(i)+'.svg') and os.path.isfile('my_fonts/' + src + '/'+str(i)+'.svg'):
            data['glyphs'][key]['src'] = 'my_fonts/' + src + '/'+str(i)+'.svg'
        else:
            data['glyphs'][key]['src'] = 'my_fonts/default.svg'
        i += 1
    with open('font.json', 'w') as outfile:
        json.dump(data, outfile)
