# Reading list.


These papers are excellent resources to get started on learning about distributed hash tables and P2P networks in general.
If you are completely new to the subject, I suggest starting with the very first paper listed.
Although a bit dated, it does provide a good deal of history along with the technical data.

# General Info/ Survey Papers

* A survey and comparison of peer-to-peer overlay network schemes - http://zoo.cs.yale.edu/classes/cs426/2012/bib/lua05survey.pdf
* A Survey of Peer-to-Peer Content Distribution Technologies http://www.spinellis.gr/pubs/jrnl/2004-ACMCS-p2p/html/AS04.pdf

# Specific DHTs
In our highly biased opinion Chord and Kademlia are the most important DHT papers.

* Chord http://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf
* Kademlia  http://pdos.csail.mit.edu/~petar/papers/maymounkov-kademlia-lncs.pdf
* CAN http://wortschatz.uni-leipzig.de/~fwitschel/vorlP2P/literatur/CAN.pdf
* Pastry/Tapestry http://www.srhea.net/papers/tapestry_jsac.pdf
* Symphony http://infolab.stanford.edu/~bawa/Pub/symphony.pdf
* Viceroy http://www.cs.cornell.edu/courses/cs6452/2012sp/papers/viceroy.pdf
* ZHT http://datasys.cs.iit.edu/~dongfang/download/2013_IPDPS13_ZHT.pdf
* Coral http://iptps03.cs.berkeley.edu/final-papers/coral.pdf

# Interesting Concept Papers: 
* Small World Routing http://www.cis.upenn.edu/~mkearns/teaching/NetworkedLife/nat00.pdf
* Complex Queries in DHT-based Peer-to-Peer Networks http://www.cs.berkeley.edu/~istoica/papers/2002/pier-iptps02.pdf


##Security
Completely decentralized systems don't have a centralized location or node to attack; it's part of the definition.
DHT security focuses on preventing an adversary wresting control of the network.
The most prominent tool the adversary has is the *Sybil attack*, in which the attacker presents himself as multiple ``legitimate'' enities.  

Informally, the attacker pretends to be multiple individual nodes.
DHTs treat each individual node as equal members, so with enough identities, the attacker will intercept the majority of network traffic.
From there, the adversary can eavesdrop on most of the messages, or skip the eaves and move straight on to the dropping.

* A Survey of DHT Security Techniques http://disi.unitn.it/~montreso/ds/papers/DhtSecuritySurvey.pdf
* The Sybil Attack http://freehaven.net/anonbib/cache/sybil.pdf
