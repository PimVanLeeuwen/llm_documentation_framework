#### mouseDrag()


 virtual void MouseListener::mouseDrag ( const MouseEvent & event ) virtual 
 

Called when the mouse is moved while a button is held down.When a mouse button is pressed inside a component, that component receives mouseDrag callbacks each time the mouse moves, even if the mouse strays outside the component's bounds.Parameters

 event details about the position and status of the mouse event, including the source component in which it occurred 
 



See alsomouseDown, mouseUp, mouseMove, contains, setDragRepeatInterval Reimplemented in AlertWindow, Button, CodeEditorComponent, ComboBox, Component, MenuBarComponent, MidiKeyboardComponent, MPEKeyboardComponent, ResizableBorderComponent, ResizableCornerComponent, ResizableEdgeComponent, ResizableWindow, ScrollBar, SidePanel, Slider, StretchableLayoutResizerBar, TableHeaderComponent, and TextEditor.