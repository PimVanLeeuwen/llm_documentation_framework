#### getCurrentModuleInstanceHandle()


 static void \*JUCE\_CALLTYPE Process::getCurrentModuleInstanceHandle ( ) staticnoexcept 
 

WINDOWS ONLY This returns the HINSTANCE of the current module.The return type is a void\* to avoid being dependent on windows.h just cast it to a HINSTANCE to use it.In a normal JUCE application, this will be automatically set to the module handle of the executable.If you've built a DLL and plan to use any JUCE messaging or windowing classes, you'll need to make sure you call the setCurrentModuleInstanceHandle() to provide the correct module handle in your DllMain() function, because the system relies on the correct instance handle when opening windows.