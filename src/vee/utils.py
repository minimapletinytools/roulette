#This contains a whole bunch of useful utilities

#FUNCTIONS
def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.
    
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])

def openAnything(source):            
    """URI, filename, or string --> stream

    This function lets you define parsers that take any input source
    (URL, pathname to local or network file, or actual data as a string)
    and deal with it in a uniform manner.  Returned object is guaranteed
    to have all the basic stdio read methods (read, readline, readlines).
    Just .close() the object when you're done with it.
    
    Examples:
    >>> from xml.dom import minidom
    >>> sock = openAnything("http://localhost/kant.xml")
    >>> doc = minidom.parse(sock)
    >>> sock.close()
    >>> sock = openAnything("c:\\inetpub\\wwwroot\\kant.xml")
    >>> doc = minidom.parse(sock)
    >>> sock.close()
    >>> sock = openAnything("<ref id='conjunction'><text>and</text><text>or</text></ref>")
    >>> doc = minidom.parse(sock)
    >>> sock.close()
    """
    if hasattr(source, "read"):
        return source

    if source == '-':
        import sys
        return sys.stdin

    # try to open with urllib (if source is http, ftp, or file URL)
    import urllib                         
    try:                                  
        return urllib.urlopen(source)     
    except (IOError, OSError):            
        pass                              
    
    # try to open with native open function (if source is pathname)
    try:                                  
        return open(source)               
    except (IOError, OSError):            
        pass                              
    
    # treat source as string
    import StringIO                       
    return StringIO.StringIO(str(source)) 


#CLASSES

#XML
import xml
def loadAttributes(xml,d):
    """
    dumps all attributes by name into dictionary
    """
    pass
def getTextNode(node,i=0):
    return getNode(node,xml.dom.Node.TEXT_NODE,i)
def getNode(node, type, i=0):
    """
    returns ith text node of node
    """
    if i == 0:
        for w in node.childNodes: 
            if w.nodeType == type:
                return w
    return getNodes(node,type)[i]
def getNodes(node, type):
    """
    returns ith text node of node
    """
    return [w for w in node.childNodes if w.nodeType == type]
def getChildWithAttribute(node,tag,attribute,value):
    """
    returns children of type ELEMENT_NODE that have specified tag and attribute of specified value
    """
    for e in node.childNodes:
        if e.nodeType == xml.dom.Node.ELEMENT_NODE and e.tagName == tag:
            if e.hasAttribute(attribute) and e.getAttribute(attribute) == value:
                return e
    return None
def getChild(node,tag,i = 0):
    #i = 0 case we do separately for efficiency
    if i == 0:
        for w in node.childNodes: 
            if w.nodeType == xml.dom.Node.ELEMENT_NODE and w.tagName == tag:
                return w
    return getChildren(node,tag)[i]
def getChildren(node,tag):
    """
    returns all immediete children with a certain tagname
    xml: 
    tagname: Str, name of tag
    
    returns list of xml
    """
    return [w for w in node.childNodes if w.nodeType == xml.dom.Node.ELEMENT_NODE and w.tagName == tag]