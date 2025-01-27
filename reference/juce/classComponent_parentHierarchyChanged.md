#### parentHierarchyChanged()


 virtual void Component::parentHierarchyChanged ( ) virtual 
 

Called to indicate that the component's parents have changed.When a component is added or removed from its parent, this method will be called on all of its children (recursively so all children of its children will also be called as well).Subclasses can override this if they need to react to this in some way.See alsogetParentComponent, isShowing, ComponentListener::componentParentHierarchyChanged Reimplemented in Button, ComboBox, Drawable, DrawableComposite, KeyMappingEditorComponent, ListBox, ScrollBar, SidePanel, TextEditor, TopLevelWindow, and WebBrowserComponent.