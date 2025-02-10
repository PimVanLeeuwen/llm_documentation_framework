#### start() [2/2]


 bool ChildProcess::start ( const StringArray & arguments, 
 
 int streamFlags = wantStdOutwantStdErr ) 

Attempts to launch a child process command.The first argument should be the name of the executable file, followed by any other arguments that are needed. If the process has already been launched, this will launch it again. If a problem occurs, the method will return false. The streamFlags is a combinations of values to indicate which of the child's output streams should be read and returned by readProcessOutput().