import datetime
import struct
import socket
import threading

from loguru import logger

import influxdb


logger.add("zuebrene.log", serialize=True)
logger.add("error.log", level="ERROR")


PROTOCOL_V0 = (
    ("protocol_version", "H"),
    ("client_id", "H"),
    ("sync_freq_Hz", "f"),
    ("primary_current_A", "f"),
    ("temperature1_C", "f"),
    ("temperature2_C", "f"),
    ("temperature3_C", "f"),
    ("temperature4_C", "f"),
    ("temperature5_C", "f"),
    ("temperature6_C", "f"),
    ("pd1_pC", "f"),
    ("pd2_pC", "f"),
)
STRUCT_FMT = "".join((pair[1] for pair in PROTOCOL_V0))

INFLUX_CLIENT = influxdb.InfluxDBClient(database="zuebrene")

INFLUX_CLIENT.create_database("zuebrene")


def decode_data(data):
    data_list = struct.unpack(STRUCT_FMT, data)
    data_dict = {pair[0]: datapoint for pair, datapoint in zip(PROTOCOL_V0, data_list)}
    data_dict["utc_timestamp_s"] = int(
        datetime.datetime.now(datetime.timezone.utc).timestamp()
    )
    return data_dict


def save_data_to_db(data_dict):
    measurement = f"client_{data_dict.pop('client_id')}"
    timestamp_s = int(data_dict.pop("utc_timestamp_s"))
    datapoints = {"measurement": measurement, "time": timestamp_s, "fields": data_dict}
    logger.debug(datapoints)
    success = INFLUX_CLIENT.write_points(
        points=[datapoints], time_precision="s", database="zuebrene"
    )
    return success


def handle_requests(con, addr):
    while True:

        try:
            data = con.recv(2**10)
        except ConnectionResetError:
            break

        if not data:
            break

        data_dict = decode_data(data)
        logger.info(data_dict)
        success = save_data_to_db(data_dict)
        logger.debug(success)
        assert success

        logger.info(data)


if __name__ == "__main__":

    host = "0.0.0.0"
    port = 10000

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))
            s.listen(20)
            logger.debug(f"Accepting 20 Connections...")
            con, addr = s.accept()
            handling_thread = threading.Thread(target=handle_requests, args=(con, addr))
            handling_thread.daemon = True
            handling_thread.start()
