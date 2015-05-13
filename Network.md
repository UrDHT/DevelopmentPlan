# Network Component

The Network component provides inter-Node communication and communication with clients (if they are supported). The methods that are exposed to the network may vary between implementations but the default REST API is described here.
The ideal is that UrDHT based DHTs, implemented in different languages will be inter-operable utilizing a common network protocol

## Internal API

The Network Module provides the following procedures to other modules:

```
Seek(remote,id): sends a seek request for a given id to the remote node
```

```
GetPeers(remote): sends a request for the peerlist of a given remote node
```

```
Notify(remote,origin): sends a notify message to the remote node, informing it of origin
```

## Internal Dependencies

The Network Module depends on the following methods from the DHT Logic and Database Modules

DHT Logic:
- seek(id)
- getPeers()
- getNotified(origin)
- DoIOwn(id)

Database:
- put(id, value)
- get(id)

Traditionally, DHTs have the following functions for an api:  lookup(key), get(key), put(key,val), and maybe delete.
Lookup is often recursive, but it's easier to handle interative lookups, so we've create seek to help us with that


## External REST API

The REST API is broken into two sections:
- a client API suitable for use both by Servers and in client applications (even in the browser!)
- a Peer only API that should only be used by other Nodes

```
HTTP GET NODEURI/client/get/id

checks the database of the Node and returns the value if found.

{
	recordFound:True,
	record:"value"
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
