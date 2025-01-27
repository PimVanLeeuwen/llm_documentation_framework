#### layOutComponents()


 void StretchableLayoutManager::layOutComponents ( Component \*\* components, 
 
 int numComponents, 
 int x, 
 int y, 
 int width, 
 int height, 
 bool vertically, 
 bool resizeOtherDimension ) 

Takes a set of components that correspond to the layout's items, and positions them to fill a space.This will try to give each item its preferred size, whether that's a relative size or an absolute one.Parameters

 components an array of components that correspond to each of the numbered items that the StretchableLayoutManager object has been told about with setItemLayout() 
 
 numComponents the number of components in the array that is passedin. This should be the same as the number of items this object has been told about. 
 x the left of the rectangle in which the components should be laid out 
 y the top of the rectangle in which the components should be laid out 
 width the width of the rectangle in which the components should be laid out 
 height the height of the rectangle in which the components should be laid out 
 vertically if true, the components will be positioned in a vertical stack, so that they fill the height of the rectangle. If false, they will be placed sidebyside in a horizontal line, filling the available width 
 resizeOtherDimension if true, this means that the components will have their other dimension resized to fit the space i.e. if the 'vertically' parameter is true, their xpositions and widths are adjusted to fit the x and width parameters; if 'vertically' is false, their ypositions and heights are adjusted to fit the y and height parameters.