#ifndef NET
#define NET

#include <string.h>
#include <omnetpp.h>
#include <packet_m.h>

using namespace omnetpp;

class Net: public cSimpleModule {
private:
    int netSize;
    int *netHops;
    cQueue buffer;
public:
    Net();
    virtual ~Net();
protected:
    virtual void initialize();
    virtual void finish();
    virtual void handleMessage(cMessage *msg);
};

Define_Module(Net);

#endif /* NET */

Net::Net() {
}

Net::~Net() {
}

void Net::initialize() {
    /* When the nodes are initialized, they send a "hello" packet which travels 
    through the whole network in clockwise direction, until it reaches itself again.
    This way, we can calculate the length of the ring network. */
    Packet *pkt = new Packet("hello",this->getParentModule()->getIndex());
    pkt->setSource(this->getParentModule()->getIndex());
    pkt->setDestination(this->getParentModule()->getIndex());

    // netSize is initialized to -1, so we can check if it has been calculated or not yet.
    netSize = -1;

    // Forward package to next node
    send(pkt, "toLnk$o", 0);
}

void Net::finish() {
}

void Net::handleMessage(cMessage *msg) {

    // All msg (events) on net are packets
    Packet *pkt = (Packet *) msg;

    std::string packetName = pkt->getName();

    if (packetName == "hello") {
        // If the hello packet has reached its source, we have the length of the network in HopCount
        if (pkt->getDestination() == this->getParentModule()->getIndex()) {
            netSize = pkt->getHopCount() + 1;
            delete(msg);
        } else {
            /* If not, we forward the packet to the next node and send an echo packet in 
            counterclockwise direction. This way, we send information of the distance between
            the source of the hello packet and the current node. */
            int hops = pkt->getHopCount();
            hops++;
            pkt->setHopCount(hops);

            Packet *pktf = new Packet("echo",this->getParentModule()->getIndex());
            pktf->setSource(this->getParentModule()->getIndex());
            pktf->setDestination(pkt->getSource());
            pktf->setHopCount(hops);

            // Forward "hello" packet
            send(pkt, "toLnk$o", 0);
            // Send "echo" packet
            send(pktf, "toLnk$o", 1);
        }
    }

    else if (packetName == "echo") {
        /* If the echo packet has reached its destination, we have the distance between the source 
        of the hello packet and node 'x'. */
        if (pkt->getDestination() == this->getParentModule()->getIndex()) {
            buffer.insert(msg);
            // Once the buffer size is equal to the network size-1 (i.e we recieved all the echo packets),
            // we have all the information we need to store the values of the distance to every node.
            if (netSize-1 == buffer.getLength()) {
                netHops = new int[netSize];

                Packet* pktAux = nullptr;

                for (int i = 0; i < netSize-1; i++) {
                    pktAux = dynamic_cast<Packet*>(buffer.pop());
                    netHops[pktAux->getSource()] = pktAux->getHopCount();
                }
                // this->bubble("Terminó la carga de datos");
            }
        } else {
            if (msg->arrivedOn("toLnk$i", 0)) {
                send(msg, "toLnk$o", 1);
            } else {
                send(msg, "toLnk$o", 0);
            }
        }
    }

    else {
        // Data packets
        if (pkt->getDestination() == this->getParentModule()->getIndex()) {
            pkt->setHopCount(pkt->getHopCount()+1);
            send(msg, "toApp$o");
        }
        // If not, forward the packet to some else... to who?
        else {
            // If the pkt arrived from App, it means we have to decide where to send it.
            if (msg->arrivedOn("toApp$i")) {
                    if (netHops[pkt->getDestination()] <= netSize/2){
                        send(msg, "toLnk$o", 0);
                    } else {
                        send(msg, "toLnk$o", 1);
                    }
            }
            // If the pkt arrived from Lnk, it means we have to forward it to the next node.
            else if (msg->arrivedOn("toLnk$i", 0)) {
                pkt->setHopCount(pkt->getHopCount()+1);
                send(msg, "toLnk$o", 1);

            } else {
                pkt->setHopCount(pkt->getHopCount()+1);
                send(msg, "toLnk$o", 0);

            }
        }
    }
}
