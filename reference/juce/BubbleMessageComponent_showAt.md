#### showAt() [2/2]


 void BubbleMessageComponent::showAt ( Component \* component, 
 
 const AttributedString & message, 
 int numMillisecondsBeforeRemoving, 
 bool removeWhenMouseClicked = true, 
 bool deleteSelfAfterUse = false ) 

Shows a message bubble next to a particular component.This shows the bubble with its stem pointing at the given component.Parameters

 component the component that you want to point at 
 
 message the text to display 
 numMillisecondsBeforeRemoving how long to leave it on the screen before removing itself from its parent component. If this is 0 or less, it will stay there until manually removed. 
 removeWhenMouseClicked if this is true, the bubble will disappear as soon as a mouse button is pressed (anywhere on the screen) 
 deleteSelfAfterUse if true, then the component will delete itself after it becomes invisible