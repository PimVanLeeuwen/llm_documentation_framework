#### mouseDraggedToKey()


 virtual bool MidiKeyboardComponent::mouseDraggedToKey ( int midiNoteNumber, const MouseEvent & e ) virtual 
 

Callback when the mouse is dragged from one key onto another.Return true if you want the drag to trigger the new note, or false if you want to handle it yourself and not have the note played.See alsomouseDownOnKey