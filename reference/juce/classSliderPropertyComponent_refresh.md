#### refresh()


 void SliderPropertyComponent::refresh ( ) overridevirtual 
 

Updates the property component if the item it refers to has changed.A subclass must implement this method, and other objects may call it to force it to refresh itself.The subclass should be economical in the amount of work is done, so for example it should check whether it really needs to do a repaint rather than just doing one every time this method is called, as it may be called when the value being displayed hasn't actually changed.Implements PropertyComponent.

Member Data Documentation