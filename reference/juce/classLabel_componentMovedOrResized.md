#### componentMovedOrResized()


 void Label::componentMovedOrResized ( Component & component, bool wasMoved, bool wasResized ) overrideprotectedvirtual 
 

Called when the component's position or size changes.Parameters

 component the component that was moved or resized 
 
 wasMoved true if the component's topleft corner has just moved 
 wasResized true if the component's width or height has just changed 



See alsoComponent::setBounds, Component::resized, Component::moved Reimplemented from ComponentListener.