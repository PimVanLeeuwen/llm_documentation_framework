#### waitForJobToFinish()


 bool ThreadPool::waitForJobToFinish ( const ThreadPoolJob \* job, 
 
 int timeOutMilliseconds ) const 

Waits until a job has finished running and has been removed from the pool.This will wait until the job is no longer in the pool i.e. until its runJob() method returns ThreadPoolJob::jobHasFinished.If the timeout period expires before the job finishes, this will return false; it returns true if the job has finished successfully.