# Target Manager CLI User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Target_Manager_CLI-Users_Guide/network-configuration-for-targets.html

# Network Configuration for Targets

## Introduction

The PlayStation® system software uses a peer-to-peer file transfer mechanism which enables files to be copied to any number of Target DevKits and TestKits at the same time.

Targets involved in the transfer are arranged in a 'chain' where every Target sends each chunk of data received on to the next Target immediately without having to wait for the data to be written to storage.

This enables
faster copying of software to multiple PlayStation®5 DevKits and TestKits via a network. This includes package installations, system software updates and general-purpose file transfers via prospero-ctrl and Target Manager.

## Network Configuration

Ideally all the Targets contained in a chain will be on the same subnet and connected to the same switch.

Target Manager Server organizes the chain automatically in ascending order starting with the Target whose IPv4 address is closest to 0.0.0.0 and ending with the Target whose IP address is closest to 255.255.255.255. The optimal network topology looks like the following image:

Care should be taken to avoid bottlenecks in the network traffic flow, such as network traffic having to flow along the same physical cable multiple times in order to complete the chain. For example:

In the example above the copy from Target #1 (10.0.0.5) to Target #2 (10.0.0.6) has
to travel over the wire connecting Switch 1 to Switch 2 (colored red in the diagram
above), as does the copy from Target #2 (10.0.0.6) to Target #3 (1.0.0.7)
and
the copy from Target #3 (10.0.0.7) to Target #4 (10.0.0.8), meaning that each copy
can only use 1/3 the total bandwidth of the wire.

This can be resolved by changing the IP addresses of the two red Targets so that they change their place in the chain order.