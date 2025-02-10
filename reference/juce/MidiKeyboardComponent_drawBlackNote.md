#### drawBlackNote()


 virtual void MidiKeyboardComponent::drawBlackNote ( int midiNoteNumber, Graphics & g, Rectangle< float > area, bool isDown, bool isOver, Colour noteFillColour ) virtual 
 

Use this method to draw a black note of the keyboard in a given rectangle.isOver indicates whether the mouse is over the key, isDown indicates whether the key is currently pressed down.When doing this, be sure to note the keyboard's orientation.