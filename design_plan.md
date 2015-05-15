The goal of this document is to describe a software-design that would be viable in multiple OOP languages.

The basic assumptions of this document are the ability to create 3 singleton objects that are able to call each others methods.

Parallel/Concurrent behavoir should be handled by each object for it's own methods.
Any function call should block until a result or error (maybe a timeout) is reached.

The basic form of this approach is:

Singleton Class:
	todo = new Queue
	workers = workerthreads
		def doWork()
			while running:
				method, args, callback = todo.get()
				result = do_method(args)
				callback.put(result)

	def dostuff(ags):
		callback_channel = new Queue ##these could be pooled
		todo_pack = ("dostuff", args, callback_channel)
		todo.put( todo_pack  )
		return todo.get("Block forever")

This way, outside of the worker logic, we will not need to deal with locks or races.