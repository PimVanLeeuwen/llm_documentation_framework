#### runJob()


 virtual JobStatus ThreadPoolJob::runJob ( ) pure virtual 
 

Performs the actual work that this job needs to do.Your subclass must implement this method, in which is does its work.If the code in this method takes a significant time to run, it must repeatedly check the shouldExit() method to see if something is trying to interrupt the job. If shouldExit() ever returns true, the runJob() method must return immediately.If this method returns jobHasFinished, then the job will be removed from the pool immediately. If it returns jobNeedsRunningAgain, then the job will be left in the pool and will get a chance to run again as soon as a thread is free.See alsoshouldExit()