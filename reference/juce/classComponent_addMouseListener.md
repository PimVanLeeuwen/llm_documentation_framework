#### addMouseListener()


 void Component::addMouseListener ( MouseListener \* newListener, 
 
 bool wantsEventsForAllNestedChildComponents ) 

Registers a listener to be told when mouse events occur in this component.If you need to get informed about mouse events in a component but can't or don't want to override its methods, you can attach any number of listeners to the component, and these will get told about the events in addition to the component's own callbacks being called.Note that a MouseListener can also be attached to more than one component.Parameters

 newListener the listener to register 
 
 wantsEventsForAllNestedChildComponents if true, the listener will receive callbacks for events that happen to any child component within this component, including deeplynested child components. If false, it will only be told about events that this component handles. 



See alsoMouseListener, removeMouseListener