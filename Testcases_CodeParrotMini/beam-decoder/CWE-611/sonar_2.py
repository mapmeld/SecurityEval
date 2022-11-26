from lxml import etree
def get_root():
    '''
    create a XML parser, parse from a file, validate the XML and return the schema
    '''
	root = etree.parse(os.path.join(os.path.dirname