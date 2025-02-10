#### beginDragAutoRepeat()


 void Desktop::beginDragAutoRepeat ( int millisecondsBetweenCallbacks ) 
 

Ensures that a nonstop stream of mousedrag events will be sent during the current mousedrag operation.This allows you to make sure that mouseDrag() events are sent continuously, even when the mouse isn't moving. This can be useful for things like autoscrolling components when the mouse is near an edge.Call this method during a mouseDown() or mouseDrag() callback, specifying the minimum interval between consecutive mouse drag callbacks. The callbacks will continue until the mouse is released, and then the interval will be reset, so you need to make sure it's called every time you begin a drag event. Passing an interval of 0 or less will cancel the autorepeat.See alsomouseDrag