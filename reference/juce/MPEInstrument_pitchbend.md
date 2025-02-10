#### pitchbend()


 virtual void MPEInstrument::pitchbend ( int midiChannel, MPEValue pitchbend ) virtual 
 

Request a pitchbend on the given channel with the given value (in units of MIDI pitchwheel position).Internally, this will determine whether the pitchwheel move is a pernote pitchbend or a master pitchbend (depending on midiChannel), take the correct pernote or master pitchbend range of the affected MPE zone, and apply the resulting pitchbend to the affected note(s) (if any).