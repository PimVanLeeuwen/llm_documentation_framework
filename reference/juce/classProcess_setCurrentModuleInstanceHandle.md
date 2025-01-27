#### setCurrentModuleInstanceHandle()


 static void JUCE\_CALLTYPE Process::setCurrentModuleInstanceHandle ( void \* newHandle ) staticnoexcept 
 

WINDOWS ONLY Sets a new module handle to be used by the library.The parameter type is a void\* to avoid being dependent on windows.h, but it actually expects a HINSTANCE value.See alsogetCurrentModuleInstanceHandle()