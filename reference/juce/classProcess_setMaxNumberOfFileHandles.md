#### setMaxNumberOfFileHandles()


 static bool Process::setMaxNumberOfFileHandles ( int maxNumberOfFiles ) staticnoexcept 
 

UNIX ONLY Attempts to use setrlimit to change the maximum number of file handles that the app can open.Pass 0 or less as the parameter to mean 'infinite'. Returns true if it succeeds.