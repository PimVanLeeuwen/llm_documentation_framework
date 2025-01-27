#### invalidateAccessibilityHandler()


 void Component::invalidateAccessibilityHandler ( ) 
 

Invalidates the AccessibilityHandler that is currently being used for this component.Use this to indicate that something in the accessible component has changed and its handler needs to be updated. This will trigger a call to createAccessibilityHandler().