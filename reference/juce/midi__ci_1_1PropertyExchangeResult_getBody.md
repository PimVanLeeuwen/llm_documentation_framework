#### getBody()


 Span< const std::byte > midi\_ci::PropertyExchangeResult::getBody ( ) const 
 

When getKind returns 'full', this is the message payload.Note that this is not stored internally; if you need to keep this data around and reference it in the future, you should copy it into a vector or some other suitable container.