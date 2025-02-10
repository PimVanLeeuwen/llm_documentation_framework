#### shouldExit()


 bool ThreadPoolJob::shouldExit ( ) const noexcept 
 

Returns true if something is trying to interrupt this job and make it stop.Your runJob() method must call this whenever it gets a chance, and if it ever returns true, the runJob() method must return immediately.See alsosignalJobShouldExit()