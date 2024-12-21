#!/usr/bin/env python
# encoding: utf-8
# Revisión 2019 (a Python 3 y base64): Pablo Ventura
# Revisión 2014 Carlos Bederián
# Revisión 2011 Nicolás Wolovick
# Copyright 2008-2010 Natalia Bidart y Daniel Moisset
# $Id: server.py 656 2013-03-18 23:49:11Z bc $

import optparse
import socket
import base64
from constants import *
import connection

from socket import *  # Incluyo esta librería para las globales AF_INET, etc
import sys
import os


class Server(object):
    """
    El servidor, que crea y atiende el socket en la dirección y puerto
    especificados donde se reciben nuevas conexiones de clientes.
    """

    def __init__(self, addr=DEFAULT_ADDR, port=DEFAULT_PORT,
                 directory=DEFAULT_DIR):

        print("Serving %s on %s:%s." % (directory, addr, port))

        # Crear socket del servidor
        self.s = socket(AF_INET, SOCK_STREAM)

        # Asignar el directorio compartido
        self.directory = directory

        # Configurar y asignar el socket a una dirección y puerto
        self.s.bind((addr, port))

        # Servidor escuchando
        self.s.listen()

    def serve(self):
        """
        Loop principal del servidor. Se acepta una conexión a la vez
        y se espera a que concluya antes de seguir.
        """
        while True:
            # Aceptar una conexión al server
            (self.new_client, client_address) = self.s.accept()

            print("Conectado a %s:%s" % client_address)

            # Crear una Connection para la conexión y
            # atenderla hasta que termine
            self.connection = connection.Connection(
                self.new_client, self.directory)
            self.connection.handle()


def main():
    """Parsea los argumentos y lanza el server"""

    parser = optparse.OptionParser()
    parser.add_option(
        "-p", "--port",
        help="Número de puerto TCP donde escuchar", default=DEFAULT_PORT)
    parser.add_option(
        "-a", "--address",
        help="Dirección donde escuchar", default=DEFAULT_ADDR)
    parser.add_option(
        "-d", "--datadir",
        help="Directorio compartido", default=DEFAULT_DIR)

    options, args = parser.parse_args()
    if len(args) > 0:
        parser.print_help()
        sys.exit(1)
    try:
        port = int(options.port)
    except ValueError:
        sys.stderr.write(
            "Numero de puerto invalido: %s\n" % repr(options.port))
        parser.print_help()
        sys.exit(1)

    server = Server(options.address, port, options.datadir)
    server.serve()


if __name__ == '__main__':
    main()
