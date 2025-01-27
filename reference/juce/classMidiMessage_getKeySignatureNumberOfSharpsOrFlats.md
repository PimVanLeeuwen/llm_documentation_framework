#### getKeySignatureNumberOfSharpsOrFlats()


 int MidiMessage::getKeySignatureNumberOfSharpsOrFlats ( ) const noexcept 
 

Returns the key from a keysignature metaevent.This method must only be called if isKeySignatureMetaEvent() is true. A positive number here indicates the number of sharps in the key signature, and a negative number indicates a number of flats. So e.g. 3 = F# + C# + G#, 2 = Bb + EbSee alsoisKeySignatureMetaEvent, isKeySignatureMajorKey