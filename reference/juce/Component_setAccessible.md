#### setAccessible()


 void Component::setAccessible ( bool shouldBeAccessible ) 
 

Sets whether this component and its children are visible to accessibility clients.If this flag is set to false then the getAccessibilityHandler() method will return nullptr and this component and its children will not be visible to any accessibility clients.By default this is set to true.See alsoisAccessible, getAccessibilityHandler