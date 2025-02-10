#### setView()


 void UIViewComponent::setView ( void \* uiView ) 
 

Assigns an UIView to this peer.The view will be retained and released by this component for as long as it is needed. To remove the current view, just call setView (nullptr).Note: A void\* is used here to avoid including the cocoa headers as part of JuceHeader.h, but the method expects an UIView\*.