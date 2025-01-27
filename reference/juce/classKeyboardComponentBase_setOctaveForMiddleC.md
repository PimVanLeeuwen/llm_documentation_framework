#### setOctaveForMiddleC()


 void KeyboardComponentBase::setOctaveForMiddleC ( int octaveNumForMiddleC ) 
 

This sets the octave number which is shown as the octave number for middle C.This affects only the default implementation of getWhiteNoteText(), which passes this octave number to MidiMessage::getMidiNoteName() in order to get the note text. See MidiMessage::getMidiNoteName() for more info about the parameter.By default this value is set to 3.See alsogetOctaveForMiddleC