#### getPluginHasMainInput()


 virtual bool VST3ClientExtensions::getPluginHasMainInput ( ) const virtual 
 

This function will be called to check whether the first input bus should be designated as "kMain" or "kAux".Return true if the first bus should be kMain, or false if the bus should be kAux.All other input buses will always be designated kAux.