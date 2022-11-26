import re

def filterScriptTags(content): 
    '''
    remove script tags from content argument
    '''
	content = re.sub(r'\s+','', content)
	content = re.sub(r'\s+', '