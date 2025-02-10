#### getXRunCount()


 int AudioDeviceManager::getXRunCount ( ) const noexcept 
 

Returns the number of under or over runs reported.This method will use the underlying device's native getXRunCount if it supports it. Otherwise it will estimate the number of under/overruns by measuring the time it spent in the audio callback.