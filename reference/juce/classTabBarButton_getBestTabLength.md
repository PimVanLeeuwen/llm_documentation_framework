#### getBestTabLength()


 virtual int TabBarButton::getBestTabLength ( int depth ) virtual 
 

Chooses the best length for the tab, given the specified depth.If the tab is horizontal, this should return its width, and the depth specifies its height. If it's vertical, it should return the height, and the depth is actually its width.