import json
import os

def setGlyphs(src='test_glyphs'):
    with open('font.json') as json_file:
        data = json.load(json_file)
    i = 0
    val=['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for key in data['glyphs'].keys():
        if os.path.exists('my_fonts/' + src + '/'+val[i]+'.svg') and os.path.isfile('my_fonts/' + src + '/'+val[i]+'.svg'):
            data['glyphs'][key]['src'] = 'my_fonts/' + src + '/'+val[i]+'.svg'
        else:
            data['glyphs'][key]['src'] = 'my_fonts/default.svg'
        i += 1
    with open('font.json', 'w') as outfile:
        json.dump(data, outfile)
