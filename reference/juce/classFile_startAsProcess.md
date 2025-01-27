#### startAsProcess()


 bool File::startAsProcess ( const String & parameters = String() ) const 
 

Launches the file as a process.if the file is executable, this will run it.if it's a document of some kind, it will launch the document with its default viewer application.if it's a folder, it will be opened in Explorer, Finder, or equivalent.See alsorevealToUser