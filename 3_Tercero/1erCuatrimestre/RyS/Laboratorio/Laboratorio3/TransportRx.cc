#ifndef TRANSPORT_RX
#define TRANSPORT_RX

#include <string.h>
#include <omnetpp.h>
#include "feedbackPkt_m.h"

class Queue;

using namespace omnetpp;

class TransportRx: public cSimpleModule {

public:
    TransportRx():queue(queue){}
private:
    cQueue buffer;
    cMessage *endServiceEvent;
    simtime_t serviceTime;
    //Mide cantidad de paquetes en buffer
    cOutVector bufferSizeVector;
    //Mide cantidad de packetes descartados por buffer saturado
    cOutVector packetDropVector;
    Queue * queue;
protected:
    virtual void initialize();
    virtual void handleMessage(cMessage *msg) override;
};

Define_Module(TransportRx);

void TransportRx::initialize() {
    buffer.setName("buffer");
    endServiceEvent = new cMessage("endService");

}
void TransportRx::handleMessage(cMessage *msg){

    // if msg is signaling an endServiceEvent
    if (msg == endServiceEvent) {
        // if packet in buffer, send next one
        if (!buffer.isEmpty()) {
            // dequeue packet
            cPacket * pkt = (cPacket*)buffer.pop();
            // send packet
            send(pkt, "toApp");
            // start new service
            serviceTime = pkt->getDuration();
            scheduleAt(simTime() + serviceTime, endServiceEvent);
        }

    } else { // if msg is a data packet
                  //Chequeo que el paquete no sature el buffer
            if(buffer.getLength() >= par("bufferSize").doubleValue()){
                delete msg;
                this->bubble("packet dropped");
                packetDropVector.record(1);

                //Envío feedback
                FeedbackPkt * feedbackPkt = new FeedbackPkt();
                feedbackPkt->setByteLength(20);
                feedbackPkt->setKind(2);
                feedbackPkt->setRemainingBuffer(par("bufferSize").doubleValue() - buffer.getLength());

                send(feedbackPkt,"toOut$o");

            }

            else {
                // enqueue the packet
                buffer.insert(msg);
                bufferSizeVector.record(buffer.getLength());
                // if the server is idle
                if (!endServiceEvent->isScheduled()) {
                    // start the service now
                    scheduleAt(simTime() + 0, endServiceEvent);
                }
            }
        }
    }


#endif
