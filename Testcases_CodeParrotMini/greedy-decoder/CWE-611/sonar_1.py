from lxml import etree

def get_root():
    '''
    create a XML parser, parse from a file and return the root
    '''
	root = etree.parse(os.path.join(os.path.dirname(__file__),