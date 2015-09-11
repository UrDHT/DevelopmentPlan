# What is UrDHT?

UrDHT is an abstract implementation of a DHT that allows programmers to have a strong base for implementing DHTs in Decentralized systems.

UrDHT is not meant to be usable alone (it may include a simple DHT implementation), but is intended to be forked and converted into many more useful DHTs.

It should take minimal effort to implement any existing DHTs (Chord, Kademlia, CAN ect) using UrDHT and more usefully should allow for the easy design and implementation of novel DHTs.

UrDHT does not implement the protocol of any particular DHT.  It can, however, implement the *topology.* 

UrDHT's name comes from the Germanic prefix *ur*, meaning proto- or primitive or original.
We wanted to express that UrDHT is the DHT that can be used to build any other DHT.

Development IRC Chat can be found at #UrDHT on irc.freenode.org

WebClient: https://kiwiirc.com/client/irc.freenode.net/UrDHT

# How is UrDHT organized?

UrDHT is composed of three major abstract modules which are meant to be easily replaceable

- [Network Component](./Network.md)
	- The Network component manages connections with other Nodes and clients.
	- Replacement of this component will change the network protocols used by the DHT
	- Default implementation will utilize a http-rest interface

- [Database Component](./Database.md)
	- The database controls how values on the DHT are stored.
	- For the purposes of our design this is the least important module
	- Initial implementation will utilize a simple flat-file database. 
	- This is intended to be replaced on a per-use-case basis
	- Ideally Nodes in the same network could utilize different databases

- [DHT Logic Component](./DHT_Logic.md)
	- The DHT logic component will be the primary focus
	- This is where interesting stuff happens
	- It will implement the basic DHT functions
	- Design will leverage a metric space abstraction for DHTs
	- Default implementation will utilize a finite euclidean plane use DGVH approximation for peer selection
	- This involves mathematical forumulation for distance, midpoint, and closeness, which is a publion in itself.


# If you want to help development:

- Follow the style guide for consistency! [StyleGuide] (./StyleGuide.md)
- Pick a Bug or TODO issue (make one if you see the need)
- checkout a new feature branch (of fork if you don't have repo access)
- implement feature or fix bug
- write a new test to test your feature or bug (testing methods will vary from project to project and language to language)
- Use Github to open a pull request
- Wait for a few days while we argue about your patch


## Initial Publions
	- The project itself
	- VHash
	- Mathematical formulation of DHTs
