#### removeAllJobs()


 bool ThreadPool::removeAllJobs ( bool interruptRunningJobs, 
 
 int timeOutMilliseconds, 
 JobSelector \* selectedJobsToRemove = nullptr ) 

Tries to remove all jobs from the pool.Parameters

 interruptRunningJobs if true, then all running jobs will have their ThreadPoolJob::signalJobShouldExit() methods called to try to interrupt them 
 
 timeOutMilliseconds the length of time this method should wait for all the jobs to finish before giving up and returning false 
 selectedJobsToRemove if this is not a nullptr, the JobSelector object is asked to decide which jobs should be removed. If it is a nullptr, all jobs are removed 



Returnstrue if all jobs are successfully stopped and removed; false if the timeout period expires while waiting for one or more jobs to stop