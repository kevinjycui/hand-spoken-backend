import json

def setGlyphs(src='test_glyphs'):
    with open('font.json') as json_file:
        data = json.load(json_file)
    i = 0
    for key in data['glyphs'].keys():
        if os.path.exists('src/' + src + '/'+str(i)+'.svg') and os.path.isfile('src/' + src + '/'+str(i)+'.svg'):
            data['glyphs'][key]['src'] = 'src/' + src + '/'+str(i)+'.svg'
        else:
            data['glyphs'][key]['src'] = 'src/default.svg'
        i += 1
    with open('font.json', 'w') as outfile:
        json.dump(data, outfile)
