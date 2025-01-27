#### canHandleFile()


 bool AiffAudioFormat::canHandleFile ( const File & fileToTest ) overridevirtual 
 

Returns true if this the given file can be read by this format.Subclasses shouldn't do too much work here, just check the extension or file type. The base class implementation just checks the file's extension against one of the ones that was registered in the constructor.Reimplemented from AudioFormat.