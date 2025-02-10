#### signalJobShouldExit()


 void ThreadPoolJob::signalJobShouldExit ( ) 
 

Calling this will cause the shouldExit() method to return true, and the job should (if it's been implemented correctly) stop as soon as possible.See alsoshouldExit()