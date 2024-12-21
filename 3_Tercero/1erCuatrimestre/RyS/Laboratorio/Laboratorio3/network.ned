simple Generator
{
    parameters:
        volatile double generationInterval; // sec 
        volatile int packetByteSize;
        @display("i=block/source");
    gates:
        output out;
}

simple Queue
{
    parameters:
        volatile double bufferSize;
        volatile double serviceTime;
        @display("i=block/queue;q=buffer");
    gates:
        input in;
        output out;
}

simple Sink
{
    parameters:
        @display("i=block/sink");
    gates:
        input in;
}

simple TransportTx
{
    parameters:
        double bufferSize;
        @display("i=block/queue;q=buffer");
    gates:
        input toApp;
        inout toOut;
}


simple TransportRx
{
    parameters:
        double bufferSize;
        @display("i=block/queue;q=buffer");
    gates:
        output toApp;
        inout toOut;
}

module NodeTx
{
    parameters:
        @display("i=block/routing");
    gates:
        input in;
        output out;
    submodules:
        gen: Generator {
            parameters:
                @display("p=102,49");
        }
        transtx: TransportTx {
            @display("p=102,196");
        }
    connections:
        in --> transtx.toOut$i;
        gen.out --> transtx.toApp;
        transtx.toOut$o --> out;
}


module NodeRx
{
    parameters:
        @display("i=block/routing;bgb=206,271");
    gates:
        input in;
        output out;
    submodules:
        sink: Sink {
            parameters:
                @display("p=106,52");
        }
        transrx: TransportRx {
            @display("p=106,201");
        }
    connections:
        in --> transrx.toOut$i;
        transrx.toApp --> {  datarate = 0.5Mbps; } --> sink.in;
        transrx.toOut$o --> out;

}


network Network
{
    @display("bgl=100;bgb=400,273"); // 
    submodules:
        nodeTx: NodeTx {
            @display("p=31,217");
        }
        nodeRx: NodeRx {
            @display("p=326,217");
        }
        queue0: Queue {
            @display("p=181,109");
        }
        queue1: Queue {
            @display("p=181,217");
        }


    connections:
        nodeTx.out --> {  datarate = 1Mbps; delay = 100us; } --> queue0.in;
        queue0.out --> {  datarate = 1Mbps; delay = 100us; } --> nodeRx.in;
        nodeRx.out --> {  datarate = 1Mbps; delay = 100us; } --> queue1.in;
        queue1.out --> {  datarate = 1Mbps; delay = 100us; } --> nodeTx.in;

}


