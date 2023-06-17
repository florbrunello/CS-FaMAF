#ifndef TRANSPORT_TX
#define TRANSPORT_TX

#include <string.h>
#include <omnetpp.h>
#include "feedbackPkt_m.h"
using namespace omnetpp;

class TransportTx: public cSimpleModule {
private:
    cQueue buffer;
    cOutVector bufferSizeVector;
    cOutVector packetDropVector;
    cMessage* msg;
    cMessage *endServiceEvent;
    simtime_t serviceTime;
    int delay;
    int numFeedbacks;

public:
protected:
    virtual void initialize() override;
    virtual void handleMessage(cMessage *msg) override;

};

Define_Module(TransportTx);

void TransportTx::initialize() {
    buffer.setName("buffer");
    endServiceEvent = new cMessage("endService");
    delay=0;
    numFeedbacks = 0;

}

void TransportTx:: handleMessage(cMessage * msg) {
    //Es un feedback packet
    if (msg->getKind()==2){
        FeedbackPkt* feedbackPkt = (FeedbackPkt*)msg;

        int remainingBuffer= feedbackPkt->getRemainingBuffer();

        numFeedbacks ++;
        //Bajo la tasa de transmisión por cada feedback recibido.
        delay = 0.01 * numFeedbacks;


        delete(msg);
    }
    else {

        // if msg is signaling an endServiceEvent
        if (msg == endServiceEvent) {
            // if packet in buffer, send next one
            if (!buffer.isEmpty()) {
                // dequeue packet
                cPacket * pkt = (cPacket*)buffer.pop();
                // send packet
                send(pkt, "toOut$o");
                // start new service
                serviceTime = pkt->getDuration();
                scheduleAt(simTime() + serviceTime + delay, endServiceEvent);
            }
        } else {

            //Chequeo que el paquete no sature el buffer
            if(buffer.getLength() >= par("bufferSize").doubleValue()){
                delete msg;
                this->bubble("packet dropped");
                packetDropVector.record(1);
            }
            else {
                // enqueue the packet
                buffer.insert(msg);
                bufferSizeVector.record(buffer.getLength());
                // if the server is idle
                if (!endServiceEvent->isScheduled()) {
                    // start the service now
                    scheduleAt(simTime() + delay, endServiceEvent);
                }
            }

        }
    }

}




#endif
