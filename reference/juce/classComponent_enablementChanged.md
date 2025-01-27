#### enablementChanged()


 virtual void Component::enablementChanged ( ) virtual 
 

Callback to indicate that this component has been enabled or disabled.This can be triggered by one of the component's parent components being enabled or disabled, as well as changes to the component itself.The default implementation of this method does nothing; your class may wish to repaint itself or something when this happens.See alsosetEnabled, isEnabled Reimplemented in Button, ComboBox, DrawableButton, GroupComponent, Label, PropertyComponent, Slider, TextEditor, ToolbarButton, and TreeView.