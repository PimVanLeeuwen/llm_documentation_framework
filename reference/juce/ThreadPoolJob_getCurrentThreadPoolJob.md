#### getCurrentThreadPoolJob()


 static ThreadPoolJob \* ThreadPoolJob::getCurrentThreadPoolJob ( ) static 
 

If the calling thread is being invoked inside a runJob() method, this will return the ThreadPoolJob that it belongs to.