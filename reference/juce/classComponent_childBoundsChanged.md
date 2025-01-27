#### childBoundsChanged()


 virtual void Component::childBoundsChanged ( Component \* child ) virtual 
 

Called when one of this component's children is moved or resized.If the parent wants to know about changes to its immediate children (not to children of its children), this is the method to override.See alsomoved, resized, parentSizeChanged Reimplemented in AudioDeviceSelectorComponent, CallOutBox, DrawableComposite, ResizableWindow, and TabBarButton.