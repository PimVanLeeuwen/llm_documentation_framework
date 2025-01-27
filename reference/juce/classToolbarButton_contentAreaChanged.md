#### contentAreaChanged()


 void ToolbarButton::contentAreaChanged ( const Rectangle< int > & newBounds ) overridevirtual 
 

Callback to indicate that the content area of this item has changed.This might be because the component was resized, or because the style changed and the space needed for the text label is different.See getContentArea() for a description of what the area is.Implements ToolbarItemComponent.