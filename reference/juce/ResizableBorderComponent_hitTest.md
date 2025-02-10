#### hitTest()


 bool ResizableBorderComponent::hitTest ( int x, int y ) overrideprotectedvirtual 
 

Tests whether a given point is inside the component.Overriding this method allows you to create components which only intercept mouseclicks within a userdefined area.This is called to find out whether a particular x, y coordinate is considered to be inside the component or not, and is used by methods such as contains() and getComponentAt() to work out which component the mouse is clicked on.Components with custom shapes will probably want to override it to perform some more complex hittesting.The default implementation of this method returns either 'client' or 'none', depending on the value that was set by calling setInterceptsMouseClicks() ('client' is the default return value).Note that the hittest region is not related to the opacity with which areas of a component are painted.Applications should never call hitTest() directly instead use the contains() method, because this will also test for occlusion by the component's parent.Note that for components on the desktop, this method will be ignored, because it's not always possible to implement this behaviour on all platforms.Parameters

 x the x coordinate to test, relative to the left hand edge of this component. This value is guaranteed to be greater than or equal to zero, and less than the component's width 
 
 y the y coordinate to test, relative to the top edge of this component. This value is guaranteed to be greater than or equal to zero, and less than the component's height 



Returnstrue if the click is considered to be inside the component 
See alsosetInterceptsMouseClicks, contains Reimplemented from Component.