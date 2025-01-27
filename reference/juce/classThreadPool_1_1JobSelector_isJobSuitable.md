#### isJobSuitable()


 virtual bool ThreadPool::JobSelector::isJobSuitable ( ThreadPoolJob \* job ) pure virtual 
 

Should return true if the specified thread matches your criteria for whatever operation that this object is being used for.Any implementation of this method must be extremely fast and threadsafe!