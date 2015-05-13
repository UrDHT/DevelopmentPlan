# What is UrDHT?

UrDHT is an abstract implementation of a DHT that allows programmers to have a strong base for implementing DHTs in Decentralized systems.

UrDHT is not meant to be usable alone (it may include a simple DHT implementation), but is intended to be forked and converted into many more useful DHTs. 

It should take minimal effort to implement any existing DHTs (Chord, Kademlia, CAN ect) using UrDHT and more usefully should allow for the easy design and implementation of novel DHTs.

Development IRC Chat can be found at #UrDHT on irc.freenode.org

WebClient: https://kiwiirc.com/client/irc.freenode.net/UrDHT

# How is UrDHT organized?

UrDHT is composed of three major abstract modules which are meant to be easily replaceable

- Network Component
	- The Network component manages connections with other Nodes and clients.
	- Replacement of this component will change the network protocols used by the DHT
	- Default implementation will utilize a http-rest interface

- Database Component
	- The database controls how values on the DHT are stored.
	- For the purposes of our design this is the least important module
	- Initial implementation will utilize a simple flat-file database. 
	- This is intended to be replaced on a per-use-case basis
	- Ideally Nodes in the same network could utilize different databases

- DHT Logic Component
	- The DHT logic component will be the primary focus
	- This is where interesting stuff happens
	- It will implement the basic DHT functions
	- Design will leverage a metric space abstraction for DHTs
	- Default implementation will utilize a finite euclidean plane use DGVH approximation for peer selection



# If you want to help development:

- Pick a Bug or TODO issue (make one if you see the need)
- checkout a new feature branch (of fork if you don't have repo access)
- implement feature or fix bug
- write a new test to test your feature or bug (testing methods will vary from project to project and language to language)
- Use Github to open a pull request
- Wait for a few days while we argue about your patch


- Initial Publions
	- The project itself
	- VHash
	- Mathematical formulation of DHTs