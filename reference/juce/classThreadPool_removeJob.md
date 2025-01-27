#### removeJob()


 bool ThreadPool::removeJob ( ThreadPoolJob \* job, 
 
 bool interruptIfRunning, 
 int timeOutMilliseconds ) 

Tries to remove a job from the pool.If the job isn't yet running, this will simply remove it. If it is running, it will wait for it to finish.If the timeout period expires before the job finishes running, then the job will be left in the pool and this will return false. It returns true if the job is successfully stopped and removed.Parameters

 job the job to remove 
 
 interruptIfRunning if true, then if the job is currently busy, its ThreadPoolJob::signalJobShouldExit() method will be called to try to interrupt it. If false, then if the job will be allowed to run until it stops normally (or the timeout expires) 
 timeOutMilliseconds the length of time this method should wait for the job to finish before giving up and returning false