#### getFrequencyInHertz()


 double MPENote::getFrequencyInHertz ( double frequencyOfA = 440.0 ) const noexcept 
 

Returns the current frequency of the note in Hertz.This is the sum of the initialNote and the totalPitchbendInSemitones, converted to Hertz.