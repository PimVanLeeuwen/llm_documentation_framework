#### setBoundsToFit()


 void Component::setBoundsToFit ( Rectangle< int > targetArea, 
 
 Justification justification, 
 bool onlyReduceInSize ) 

Positions the component within a given rectangle, keeping its proportions unchanged.If onlyReduceInSize is false, the component will be resized to fill as much of the rectangle as possible without changing its aspect ratio (the component's current size is used to determine its aspect ratio, so a zerosize component won't work here). If onlyReduceInSize is true, it will only be resized if it's too big to fit inside the rectangle.It will then be positioned within the rectangle according to the justification flags specified.See alsosetBounds