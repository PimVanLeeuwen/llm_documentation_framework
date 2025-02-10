#### getKeyPosition()


 virtual Range< float > KeyboardComponentBase::getKeyPosition ( int midiNoteNumber, float keyWidth ) const virtual 
 

Calculates the position of a given midinote.This can be overridden to create layouts with custom keywidths.Parameters

 midiNoteNumber the note to find 
 
 keyWidth the desired width in pixels of one key see setKeyWidth() 



Returnsthe start and length of the key along the axis of the keyboard