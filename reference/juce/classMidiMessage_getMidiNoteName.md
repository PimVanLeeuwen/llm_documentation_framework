#### getMidiNoteName()


 static String MidiMessage::getMidiNoteName ( int noteNumber, bool useSharps, bool includeOctaveNumber, int octaveNumForMiddleC ) static 
 

Returns the name of a midi note number.E.g "C", "D#", etc.Parameters

 noteNumber the midi note number, 0 to 127 
 
 useSharps if true, sharpened notes are used, e.g. "C#", otherwise they'll be flattened, e.g. "Db" 
 includeOctaveNumber if true, the octave number will be appended to the string, e.g. "C#4" 
 octaveNumForMiddleC if an octave number is being appended, this indicates the number that will be used for middle C's octave 



See alsogetMidiNoteInHertz