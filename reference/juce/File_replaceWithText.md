#### replaceWithText()


 bool File::replaceWithText ( const String & textToWrite, 
 
 bool asUnicode = false, 
 bool writeUnicodeHeaderBytes = false, 
 const char \* lineEndings = "\r\n" ) const 

Replaces this file's contents with a given text string.This will delete the file and replace it with the given text.A nice feature of this method is that it's safe instead of deleting the file first and then rewriting it, it creates a new temporary file, writes the text to that, and then moves the new file to replace the existing file. This means that if the power gets pulled out or something crashes, you're a lot less likely to end up with an empty file..For an explanation of the parameters here, see the appendText() method.Returns true if the operation succeeds, or false if it fails.See alsoappendText