#### pitchbend


 MPEValue MPENote::pitchbend { MPEValue::centreValue() } 
 

Current pernote pitchbend of the note (in units of MIDI pitchwheel position).This dimension can be modulated while the note sounds.Note: This value is not aware of the currently used pitchbend range, or an additional master pitchbend that may be simultaneously applied. To compute the actual effective pitchbend of an MPENote, you should probably use the member totalPitchbendInSemitones instead.See alsototalPitchbendInSemitones, getFrequencyInHertz