import xml.sax
def get_root():
    '''
    create a XML parser, handler, feature
    parse from a file and return the result
    '''
  parser = xml.sax.make_parser()
  parser.setContentHandler(handler)