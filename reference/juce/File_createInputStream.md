#### createInputStream()


 std::unique\_ptr< FileInputStream > File::createInputStream ( ) const 
 

Creates a stream to read from this file.Note that this is an old method, and actually it's usually best to avoid it and instead use an RAII pattern with an FileInputStream directly, e.g.FileInputStream input (fileToOpen);
 
if (input.openedOk())
{
 input.read (etc...
}
FileInputStreamAn input stream that reads from a local file.Definition juce\_FileInputStream.h:50
Returnsa stream that will read from this file (initially positioned at the start of the file), or nullptr if the file can't be opened for some reason 
See alsocreateOutputStream, loadFileAsData