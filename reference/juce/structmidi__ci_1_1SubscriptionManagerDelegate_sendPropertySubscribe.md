#### sendPropertySubscribe()


 virtual std::optional< RequestKey > midi\_ci::SubscriptionManagerDelegate::sendPropertySubscribe ( MUID m, const PropertySubscriptionHeader & header, std::function< void(const PropertyExchangeResult &)> onResult ) pure virtual 
 

Called when the manager wants to send an update.