#### createOutputStream()


 std::unique\_ptr< FileOutputStream > File::createOutputStream ( size\_t bufferSize = 0x8000 ) const 
 

Creates a stream to write to this file.Note that this is an old method, and actually it's usually best to avoid it and instead use an RAII pattern with an FileOutputStream directly, e.g.FileOutputStream output (fileToOpen);
 
if (output.openedOk())
{
 output.read etc...
}
FileOutputStreamAn output stream that writes into a local file.Definition juce\_FileOutputStream.h:50
If the file exists, the stream that is returned will be positioned ready for writing at the end of the file. If you want to write to the start of the file, replacing the existing content, then you can do the following:FileOutputStream output (fileToOverwrite);
 
if (output.openedOk())
{
 output.setPosition (0);
 output.truncate();
 ...
}
Returnsa stream that will write to this file (initially positioned at the end of the file), or nullptr if the file can't be opened for some reason 
See alsocreateInputStream, appendData, appendText