#### getComponent()


 Component \* Desktop::getComponent ( int index ) const noexcept 
 

Returns one of the toplevel desktop window components.The index is from 0 to getNumComponents() 1. This could return 0 if the index is outofrange.See alsogetNumComponents, Component::addToDesktop