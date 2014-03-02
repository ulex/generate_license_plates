import sys, os

def svg2png(svgcode, fname='output.png'):
    import cairosvg
    with open(fname, 'wb') as fout:
        cairosvg.svg2png(bytestring=svgcode,write_to=fout)

def set_numbers(svg, numbers='m976mm34'):
    import xml.etree.ElementTree as ET
    tree = ET.fromstring(svg)

    for elem in tree.iter('{http://www.w3.org/2000/svg}text'):
        id = elem.attrib['id']
        if id.startswith('plate'):
            text = ''
            for c in id[5:]:
                text += numbers[int(c)]
            elem[0].text = text
    return ET.tostring(tree)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", '--output')
    parser.add_argument('number')
    args = parser.parse_args()

    pngout = args.number + '.png'
    if args.output:
        pngout = args.output
    print pngout

    code = open(os.path.join(os.path.dirname(__file__), 'ru.svg'), 'r').read()
    code = set_numbers(code, numbers=args.number)

    svg2png(code, pngout)
