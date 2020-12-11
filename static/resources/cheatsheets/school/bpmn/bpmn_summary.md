# BPMN Summary

## Events

* Start event (thin circle)
* In-between event (double thin circle)
  * Incoming and outgoing events
* Final event (thick circle)

### Types

* Time-based
* Error-based
* Condition-based
* Signal-based
* Escalation-based
* Event-connecting
* Terminating

## Activities

Representation:	Rounded rectangle

### Task

Representation:	Thin line

One simple unsplitable process and can be more exactly specified with following types.

* Send
* Receive
* Manual
* User
* Script
* Service
* Business Rule

Loops and Multi-activities indicate that an activity has to be performed multiple times. The main difference between serial multi-activities, parallel multi-activities and loops is that in the multi-activities you're already aware of the amount of times the process has to be done.

### Subprocess

Representation:	Thin line with plus sign in rectangle under text

Used to represent a bigger more complex process in a simple concise way.

### Call Activity

Representation:	Thick line

 Globally defined subprocess.

## Sequence flow

Sequence flow is indicated with directional arrows.

## Gateways

Representation:	Diamond

Used to split or join sequence flows.

### Exclusive

Representation:	X or empty

Splits path into one of two possible resulting flows.

### Parallel

Representation:	Plus sign

Splits path into all possible resulting flows and all resulting flows have to be completed before moving on to any activity after the merging of the flows.

### Inclusive

Representation:	Thick circle

Splits path into at all possible resulting flows and at least one (or more) of those flows has to be completed before moving on to any activity after the merging of the flows.

### Event-based

Representation:	Rhombus in double-circle

Waits for one of the possible events to be true and chooses to follow that flow.

### Event-based exclusive

Representation:	Rhombus in circle

Same as simple event-based gateway but it starts a sequence flow.

### Event-based parallel

Representation:	Hollow plus sign in circle

Starts a sequence flow once both following events have happened.

### Komplex

Representation:	Asterisk

Allows the definition of new gateways that aren't defined yet.

## Data

Inserted into an activity with a dashed directional arrow. Connected to activities with message flow arrows.

* Data Objects
  * Not Persistent and can be destroyed after process is completed.
  * Input and output (represented by full or only bordered arrows in top-left)
  * List dat object (represented by  three vertical lines at bottom of document)
* Data Storage
  * Persistent after process completed
* Messages 
  * Can only be used on message flows and show with more preciseness what data is transferred.

## Pools & Lanes

Can tell you who is responsible for actions. Pools can be organizations or roles and lanes aren't clearly defined. Lanes can also contain more pools.

Pools can be defined as black boxes if you're not responsible or know what goes on inside of it. Only message flows can interact with external pools. 

## Other Resources

[Graphical representation](http://www.bpmb.de/images/BPMN2_0_Poster_EN.pdf)

[bpmn.io](http://bpmn.io)

## Acknowledgements

Writer:		d20cay

Modified:	2020-08-22