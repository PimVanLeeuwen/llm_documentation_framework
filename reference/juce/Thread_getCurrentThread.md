#### getCurrentThread()


 static Thread \*JUCE\_CALLTYPE Thread::getCurrentThread ( ) static 
 

Finds the thread object that is currently running.Note that the main UI thread (or other nonJUCE threads) don't have a Thread object associated with them, so this will return nullptr.