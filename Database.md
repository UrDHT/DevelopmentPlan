# Database Component

The database component provided by default will be rather boring. I should store key-value pairs in memory and attempt to load a flat-file of records on launch and overwrite the file on shutdown.

The Database component exposes:

- Setup() -> called on start, connects/loads database

- Shutdown() -> called on shutdown

- Get(id) -> returns a stored record or Error

- Put(id,val) -> stores val at ID and possibly returns an error

The Database component has no external dependences, this makes it easy to replace.

We should setup a real database in the near future