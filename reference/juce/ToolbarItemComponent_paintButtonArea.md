#### paintButtonArea()


 virtual void ToolbarItemComponent::paintButtonArea ( Graphics & g, int width, int height, bool isMouseOver, bool isMouseDown ) pure virtual 
 

Your subclass should use this method to draw its content area.The graphics object that is passedin will have been clipped and had its origin moved to fit the content area as specified get getContentArea(). The width and height parameters are the width and height of the content area.If the component you're writing isn't a button, you can just do nothing in this method.Implemented in ToolbarButton.