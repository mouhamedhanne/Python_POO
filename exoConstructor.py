def __init__ (self):
    self.tools = []
    
def add_tool(self, tool):
    """Add a tool to the list of tools"""
    #self.tools.append(tool)
    pass

def remove_tool(self, tool):
    """Remove a tool from the list of tools"""
    #self.tools.remove(tool)
    pass

class Screwdriver:
    """Tournevis."""
    def __init__ (self, size):
        """Initialise la taille."""
        self.size = size
        
    def tighten(self, screw):
         """Serrer une vis."""
         pass
     
    def loosen(self, screw):
        """Desserre une vis."""
        pass
    
class Hammer:
    """Marteau."""
    def __init__ (self, color="red"):
        """Initialise la couleur."""
        self.color = color
        
    def pain (self, color):
         """Paint le marteau."""
         pass
    
    def hammer_in (self, nail):
        """Enfonce un clou."""
        pass
    
    def remove (self, nail):
        """Enleve un clou."""
        pass
