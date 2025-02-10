#### paintEntireComponent()


 void Component::paintEntireComponent ( Graphics & context, 
 
 bool ignoreAlphaLevel ) 

Draws this component and all its subcomponents onto the specified graphics context.You should very rarely have to use this method, it's simply there in case you need to draw a component with a custom graphics context for some reason, e.g. for creating a snapshot of the component.It calls paint(), paintOverChildren() and recursively calls paintEntireComponent() on its children in order to render the entire tree.The graphics context may be left in an undefined state after this method returns, so you may need to reset it if you're going to use it again.If ignoreAlphaLevel is false, then the component will be drawn with the opacity level specified by getAlpha(); if ignoreAlphaLevel is true, then this will be ignored and an alpha of 1.0 will be used.