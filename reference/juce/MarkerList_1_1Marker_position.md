#### position


 RelativeCoordinate MarkerList::Marker::position 
 

The marker's position.The expression used to define the coordinate may use the names of other markers, so that markers can be linked in arbitrary ways, but be careful not to create recursive loops of markers whose positions are based on each other! It can also refer to "parent.right" and "parent.bottom" so that you can set markers which are relative to the size of the component that contains them.To resolve the coordinate, you can use the MarkerList::getMarkerPosition() method.