# encoding: utf-8
# Revisión 2019 (a Python 3 y base64): Pablo Ventura
# Copyright 2014 Carlos Bederián
# $Id: connection.py 455 2011-05-01 00:32:09Z carlos $

import socket
from constants import *
import base64
import os


class Connection(object):
    """
    Conexión punto a punto entre el servidor y un cliente.
    Se encarga de satisfacer los pedidos del cliente hasta
    que termina la conexión.
    """

    def __init__(self, socket, directory):
        self.s = socket
        self.dir = directory
        self.connected = True
        self.buffer = ""

    def get_file_listing(self):
        # Busca obtener la lista de archivos que están actualmente disponibles
        result = ""
        list = os.listdir(self.dir)
        result = f"{CODE_OK} {error_messages[CODE_OK]}{EOL}"

        for i in range(0, len(list)):
            result += f"{list[i]}{EOL}"

        result += EOL
        self.s.send(result.encode("ascii"))

    def get_metadata(self, filename):
        filepath = os.path.join(self.dir, filename)

        # Chequeo que el archivo exista
        if not os.path.isfile(filepath):
            message = f"{FILE_NOT_FOUND} {error_messages[FILE_NOT_FOUND]}{EOL}"
            self.s.send(message.encode("ascii"))
        else:
            size = os.path.getsize(filepath)
            message = f"{CODE_OK} {error_messages[CODE_OK]}{EOL}{size}{EOL}"
            self.s.send(message.encode())

    def get_slice(self, filename, offset, size):

        # os.path.join une dos rutas de directorios
        filepath = os.path.join(self.dir, filename)
        fs = int(os.path.getsize(filepath))

        if (not offset.isnumeric()):
            m = f"{INVALID_ARGUMENTS} {error_messages[INVALID_ARGUMENTS]}{EOL}"
            self.s.send(m.encode("ascii"))

        elif (not size.isnumeric()):
            m = f"{INVALID_ARGUMENTS} {error_messages[INVALID_ARGUMENTS]}{EOL}"
            self.s.send(m.encode("ascii"))

        elif not os.path.isfile(filepath):
            m = f"{FILE_NOT_FOUND} {error_messages[FILE_NOT_FOUND]}{EOL}"
            self.s.send(m.encode("ascii"))

        elif int(offset) + int(size) > fs | int(offset) < 0 | int(size) < 0:
            m = f"{BAD_OFFSET} {error_messages[BAD_OFFSET]}{EOL}"
            self.s.send(m.encode("ascii"))

        # Abrimos el archivo en modo data binaria
        else:
            with open(filepath, "rb") as f:
                f.seek(int(offset))
                slice = f.read(int(size))
                base = base64.b64encode(slice)
                m = f"{CODE_OK} {error_messages[CODE_OK]}{EOL}{str(base)}{EOL}"
                self.s.send(m.encode('ascii'))

    def quit(self):
        """
        Busca terminar la conexión.
        """
        m = f"{CODE_OK} {error_messages[CODE_OK]}{EOL}"
        self.s.send(m.encode("ascii"))
        self.connected = False

    def _recv(self):
        """
        Recibe datos y acumula en el buffer interno.
        Para uso privado del server.
        """

        data = self.s.recv(4096).decode("ascii")
        self.buffer += data

        if len(data) == 0:
            self.connected = False

    def read_line(self):
        """
        Espera datos hasta obtener una línea completa delimitada por el
        terminador del protocolo.
        Devuelve una lista con el request, donde cada elemento es una
        parámetro del comando, eliminando el terminador y los espacios
        en blanco al principio y al final. Devuelve una lista vacía en
        caso de error.
        """
        while EOL not in self.buffer and self.connected:
            self._recv()

        """
        La siguiente condición es para rechazar comandos grandes, para
        evitar DoS, pero lo dejamos  comentado ya que si lo dejamos, el
        test de big file no pasa, ya que pasa un comando de aprox 5*2^20 bytes.
        if len(self.buffer) > 4096:
            m = f"{BAD_REQUEST} {error_messages[BAD_REQUEST]}{EOL}"
            self.s.send(m.encode("ascii"))
            return []
        """

        if EOL in self.buffer:
            request, self.buffer = self.buffer.split(EOL, 1)

            if '\n' in request:
                m = f"{BAD_EOL} {error_messages[BAD_EOL]}{EOL}"
                self.s.send(m.encode("ascii"))
                return []

            # request = request.strip()
            return request.split()
        else:
            return []

    def handle(self):
        """
        Atiende eventos de la conexión hasta que termina.
        """
        # Mientras esté establecida la conexión
        while self.connected:
            # Parseo una línea
            data = self.read_line()

            # ante algún error terminal, read_line devuelve una lista vacía
            if (len(data) == 0):
                self.connected = False
                break

            # Verifico si corresponde con un comando
            # (en tal caso llamo a la función)
            match data[0]:
                case "get_file_listing" if len(data) == 1:
                    self.get_file_listing()
                case "get_metadata" if len(data) == 2:
                    self.get_metadata(data[1])
                case "get_slice" if len(data) == 4:
                    self.get_slice(data[1], data[2], data[3])
                case "quit" if len(data) == 1:
                    self.quit()
                # Match con el nombre del comando pero con los argumentos no
                case 'get_file_listing' | 'get_metadata' | 'get_slice':
                    code = INVALID_ARGUMENTS
                    m = f"{code} {error_messages[code]}{EOL}"
                    self.s.send(m.encode("ascii"))
                case 'quit':
                    code = INVALID_ARGUMENTS
                    m = f"{code} {error_messages[code]}{EOL}"
                    self.s.send(m.encode("ascii"))
                # Caso en que hay fallas en el comando en sí
                case _:
                    code = INVALID_COMMAND
                    m = f"{code} {error_messages[code]}{EOL}"
                    self.s.send(m.encode("ascii"))

        self.s.close()
