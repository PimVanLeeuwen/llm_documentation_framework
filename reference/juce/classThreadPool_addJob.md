#### addJob() [3/3]


 void ThreadPool::addJob ( std::function< void()> job ) 
 

Adds a lambda function to be called as a job.This will create an internal ThreadPoolJob object to encapsulate and call the lambda.