#### moved()


 void SidePanel::moved ( ) overridevirtual 
 

Called when this component's position has been changed.This is called when the position relative to its parent changes, not when its absolute position on the screen changes (so it won't be called for all child components when a parent component is moved).The method is called synchronously as a result of the setBounds, setTopLeftPosition or any of the other repositioning methods, and like resized(), it will be called each time those methods are called.If the component is a toplevel window on the desktop, its position could also be changed by operatingsystem factors beyond the application's control.See alsoresized, setBounds Reimplemented from Component.