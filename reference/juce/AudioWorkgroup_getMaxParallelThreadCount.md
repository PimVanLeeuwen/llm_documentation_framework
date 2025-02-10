#### getMaxParallelThreadCount()


 size\_t AudioWorkgroup::getMaxParallelThreadCount ( ) const 
 

Returns the recommended maximum number of parallel threads that should join this workgroup.This recommendation is based on the workgroup attributes and current hardware, but not on system load. On a very busy system, it may be more effective to use fewer parallel threads.