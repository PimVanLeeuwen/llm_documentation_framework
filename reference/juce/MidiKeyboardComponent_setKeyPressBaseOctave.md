#### setKeyPressBaseOctave()


 void MidiKeyboardComponent::setKeyPressBaseOctave ( int newOctaveNumber ) 
 

Changes the base note above which keypresstriggered notes are played.The set of keymappings that trigger notes can be moved up and down to cover the entire scale using this method.The value passed in is an octave number between 0 and 10 (inclusive), and indicates which C is the base note to which the keymapped notes are relative.