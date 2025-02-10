#### setKeyPressForNote()


 void MidiKeyboardComponent::setKeyPressForNote ( const KeyPress & key, 
 
 int midiNoteOffsetFromC ) 

Maps a keypress to a given note.Parameters

 key the key that should trigger the note 
 
 midiNoteOffsetFromC how many semitones above C the triggered note should be. The actual midi note that gets played will be this value + (12 \* the current base octave). To change the base octave, see setKeyPressBaseOctave()