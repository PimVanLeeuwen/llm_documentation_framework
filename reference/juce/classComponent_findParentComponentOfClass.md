#### findParentComponentOfClass()


template<class TargetClass > 

 TargetClass \* Component::findParentComponentOfClass ( ) const 
 

Searches the parent components for a component of a specified class.For example findParentComponentOfClass <MyComp>() would return the first parent component that can be dynamically cast to a MyComp, or will return nullptr if none of the parents are suitable.