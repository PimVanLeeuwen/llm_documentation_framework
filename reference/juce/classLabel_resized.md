#### resized()


 void Label::resized ( ) overrideprotectedvirtual 
 

Called when this component's size has been changed.A component can implement this method to do things such as laying out its child components when its width or height changes.The method is called synchronously as a result of the setBounds or setSize methods, so repeatedly changing a components size will repeatedly call its resized method (unlike things like repainting, where multiple calls to repaint are coalesced together).If the component is a toplevel window on the desktop, its size could also be changed by operatingsystem factors beyond the application's control.See alsomoved, setSize Reimplemented from Component.