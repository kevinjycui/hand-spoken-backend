import json

def setGlyphs(src='test_glyphs'):
    with open('font.json') as json_file:
        data = json.load(json_file)
    val = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
    i = 0
    for key in data['glyphs'].keys():
        if os.path.exists(src + '/'+str(i)+'.svg') and os.path.isfile(src + '/'+str(i)+'.svg'):
            data['glyphs'][key]['src'] = src + '/'+str(i)+'.svg'
        else:
            data['glyphs'][key]['src'] = 'src/default.svg'
        i += 1
    with open('font.json', 'w') as outfile:
        json.dump(data, outfile)
