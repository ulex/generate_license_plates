import sys

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

def main():
    code = open('ru.svg', 'r').read()
    code = set_numbers(code, numbers=sys.argv[1])
    svg2png(code, 'output.png')


if __name__ == '__main__':
    assert len(sys.argv) == 2, "specify number to generate"
    main()
