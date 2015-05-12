# What is UrDHT?

UrDHT is an abstract implementation of a DHT that allows programmers to have a strong base for implementing DHTs in Decentralized systems.

UrDHT alone is not meant to be usable alone (it may include a simple DHT implementation), but is intended to be forked and converted into many more usefull DHTs. 

It should take minimal effort to implement any existing DHTs (Chord, Kademlia, CAN ect) using UrDHT and more usefully should allow for the easy design and implementation of novel DHTs.


#How is UrDHT organized?

UrDHT is composed of three major abstract modules which are meant to be easily replaceable

- Network Component
	The Network component manages connections with other Nodes and clients.
	Replacement of this component will change the 
	Default implementation is 


- Database Component

- DHT Logic Component