#### mouseDown()


 void Component::mouseDown ( const MouseEvent & event ) overridevirtual 
 

Called when a mouse button is pressed.The MouseEvent object passed in contains lots of methods for finding out which button was pressed, as well as which modifier keys (e.g. shift, ctrl) were held down at the time.Once a button is held down, the mouseDrag method will be called when the mouse moves, until the button is released.Parameters

 event details about the position and status of the mouse event, including the source component in which it occurred 
 



See alsomouseUp, mouseDrag, mouseDoubleClick, contains Reimplemented from MouseListener.Reimplemented in MenuBarComponent, MidiKeyboardComponent, MPEKeyboardComponent, ResizableBorderComponent, ResizableCornerComponent, ResizableEdgeComponent, ResizableWindow, ScrollBar, Slider, StretchableLayoutResizerBar, TableHeaderComponent, TextEditor, Toolbar, and Viewport.