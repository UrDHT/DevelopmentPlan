# Network Component

The Network component provides inter-Node communication and communication with clients (if they are supported). The methods that are exposed to the network may vary between implementations but the default REST API is described here.
The ideal is that UrDHT based DHTs, implemented in different languages will be inter-operable utilizing a common network protocol

## REST API

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
