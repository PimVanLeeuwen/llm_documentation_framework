#### registerCustomMimeTypeForFileExtension()


 static void FileChooser::registerCustomMimeTypeForFileExtension ( const String & mimeType, const String & fileExtension ) static 
 

Associate a particular fileextension to a mimetype.On Android, JUCE needs to convert common file extensions to mimetypes when using wildcard filters in native file chooser dialog boxes. JUCE has an extensive conversion table to convert between the most common filetypes and mimetypes transparently, but some more obscure filetypes may be missing. Use this method to register your own mimetype to file extension conversions. Please contact the JUCE team if you think that a common mimetype/fileextension entry is missing in JUCE's internal tables. Does nothing on other platforms.