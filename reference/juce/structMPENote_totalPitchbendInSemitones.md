#### totalPitchbendInSemitones


 double MPENote::totalPitchbendInSemitones 
 

Current effective pitchbend of the note in units of semitones, relative to initialNote.You should use this to compute the actual effective pitch of the note. This value is computed and set by an MPEInstrument to the sum of the pernote pitchbend value (stored in MPEValue::pitchbend) and the master pitchbend of the MPE zone, weighted with the pernote pitchbend range and master pitchbend range of the zone, respectively.See alsogetFrequencyInHertz