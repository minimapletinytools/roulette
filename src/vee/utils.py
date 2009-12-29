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
def getChildWithAttribute(node,tag,attribute,value):
    for e in node.childNodes:
        if e.nodeType == xml.dom.Node.ELEMENT_NODE and e.tagName == tag:
            if e.hasAttribute(attribute) and e.getAttribute(attribute) == value:
                return e
    return None
def getChildren(node,tag):
    """
    returns all immediete children with a certain tagname
    xml: 
    tagname: Str, name of tag
    
    returns list of xml
    """
    import xml
    return [w for w in node.childNodes if w.nodeType == xml.dom.Node.ELEMENT_NODE and w.tagName == tag]