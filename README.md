# What is UrDHT?

UrDHT is an abstract implementation of a DHT that allows programmers to have a strong base for implementing DHTs in Decentralized systems.

UrDHT alone is not meant to be usable alone (it may include a simple DHT implementation), but is intended to be forked and converted into many more usefull DHTs. 

It should take minimal effort to implement any existing DHTs (Chord, Kademlia, CAN ect) using UrDHT and more usefully should allow for the easy design and implementation of novel DHTs.


#How is UrDHT organized?

UrDHT is composed of three major abstract modules which are meant to be easily replaceable

- Network Component
	- The Network component manages connections with other Nodes and clients.
	- Replacement of this component will change the network protocols used by the DHT
	- Default implementation will utilize a http-rest interface

- Database Component
	- The database controls how values on the DHT are stored.
	- For the purposes of our design this is the least important module
	- Initial implementation will utilize a simple flatfile database. 
	- This is intended to be replaced on a per-use-case basis
	- Ideally Nodes in the same network could utilize different databases

- DHT Logic Component
	- The DHT logic component will be the primary focus
	- It will implement the basic DHT functions
	- Design will leverage a metric space abstraction for DHTs
	- Default implementation will utilize a finite euclidean plane use DGVH approximation for peer selection

## Network Component

The Network component provides inter-Node communication and communication with clients (if they are supported). The methods that are exposed to the network may vary between implementations but the default REST API is described here.
The ideal is that UrDHT based DHTs, implemented in different languages will be inter-operable utilizing a common network protocol

### REST API

The rest API is broken into two sections:
- a client API suitable for use both by Servers and in client applications (even in the browser!)
- a Peer only API that should only be used by other Nodes

```
HTTP GET NODEURI/client/get/id

checks the database of the Node and returns the value if found.

{
	recordFound:True,
	record = "value"
}


```

```
HTTP POST NODEURI/client/store/id

reads in posted value and stores is locally at a given id

returns code 200 on success and an error code on failure (code 403 is most common)


```

```
HTTP GET NODEURI/client/seek/id
OR
HTTP GET NODEURI/peer/seek/id

Asks the node to provide a peer closer to the given record

{
	IOwnThis:False,
	peer:"PEERURI"
}

The IOwnThis value is True when the responding node is responsible for the id
This allows clients to iteratively look up servers



```

```
HTTP GET NODEURI/peer/getPeers

Returns a node's list of peers. Useful for join and maintenance

{
	[ "PeerURI","PEERURI",...]
	
}


```

```
HTTP POST NODEURI/peer/notify

Post the node information of the sending node

Notifies a remote node that a given node exists
It is up to the remote node to decide what to do with that information


```
