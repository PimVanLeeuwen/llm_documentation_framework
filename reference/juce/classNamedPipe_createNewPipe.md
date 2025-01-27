#### createNewPipe()


 bool NamedPipe::createNewPipe ( const String & pipeName, 
 
 bool mustNotExist = false ) 

Tries to create a new pipe.Returns true if it succeeds. If mustNotExist is true then it will fail if a pipe is already open with the same name.