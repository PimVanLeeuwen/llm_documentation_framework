#### mouseDownOnKey()


 virtual bool MidiKeyboardComponent::mouseDownOnKey ( int midiNoteNumber, const MouseEvent & e ) virtual 
 

Callback when the mouse is clicked on a key.You could use this to do things like handle rightclicks on keys, etc.Return true if you want the click to trigger the note, or false if you want to handle it yourself and not have the note played.See alsomouseDraggedToKey