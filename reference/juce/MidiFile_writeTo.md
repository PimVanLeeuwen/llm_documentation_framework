#### writeTo()


 bool MidiFile::writeTo ( OutputStream & destStream, 
 
 int midiFileType = 1 ) const 

Writes the midi tracks as a standard midi file.The midiFileType value is written as the file's format type, which can be 0, 1 or 2 see the midi file spec for more info about that.Parameters

 destStream the destination stream 
 
 midiFileType the type of midi file 



Returnstrue if the operation succeeded.