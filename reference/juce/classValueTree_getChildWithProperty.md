#### getChildWithProperty()


 ValueTree ValueTree::getChildWithProperty ( const Identifier & propertyName, 
 
 const var & propertyValue ) const 

Looks for the first subtree that has the specified property value.This will scan the child trees in order, until it finds one that has property that matches the specified value. If no such tree is found, it'll return an invalid object. (You can use isValid() to check whether a tree is valid)