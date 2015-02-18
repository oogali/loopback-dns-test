#!/usr/bin/env python

import sys
import dns.message
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class LoopbackDNS(DatagramProtocol):
    def datagramReceived(self, data, (host, port)):
        msg = dns.message.from_wire(data)
        # print msg.to_text()

        query = msg.question[0]
        print query

        response = dns.message.make_response(msg)
        response.set_rcode(dns.rcode.NOERROR)

        rrset = dns.rrset.from_text(query.name, 60, dns.rdataclass.IN, dns.rdatatype.A, '127.0.0.1')
        response.answer.append(rrset)

        self.transport.write(response.to_wire(), (host, port))


def main(argv=None):
    reactor.listenUDP(53, LoopbackDNS())
    reactor.run()

    return 0

if __name__ == '__main__':
    sys.exit(main())
