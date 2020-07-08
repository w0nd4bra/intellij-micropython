"""ubluetooth — low-level Bluetooth

This module provides an interface to a Bluetooth controller on a board. Currently this supports
Bluetooth Low Energy (BLE) in Central, Peripheral, Broadcaster, and Observer roles, and a device may operate in multiple
roles concurrently.
This API is intended to match the low-level Bluetooth protocol and provide building-blocks for higher-level abstractions
such as specific device types.
"""

from typing import overload, Optional, Any, List


class BLE:
    def __init__(self) -> None:
        """
        Returns the singleton BLE object.
        """
        ...

    def active(self, active: Optional[bool]) -> bool:
        """
        Optionally changes the active state of the BLE radio, and returns the current state.
        The radio must be made active before using any other methods on this class.

        :param active: Active state.
        :type active: bool

        :return: Current state.
        :rtype: bool
        """
        ...

    @overload
    def config(self, param: str) -> Any:
        """
        Get configuration values of the BLE interface.
        To get a value the parameter name should be quoted as a string, and just one parameter is queried at a time.

        Currently supported values are:

            'mac':
                Returns the device MAC address. If a device has a fixed address (e.g. PYBD) then it will be returned.
                Otherwise (e.g. ESP32) a random address will be generated when the BLE interface is made active.
                Note: on some ports, accessing this value requires that the interface is active
                (so that the MAC address can be queried from the controller).

            'gap_name':
                Get the GAP device name used by service 0x1800, characteristic 0x2a00.

            'rxbuf':
                Get the size in bytes of the internal buffer used to store incoming events.
                This buffer is global to the entire BLE driver and so handles incoming data for all events,
                including all characteristics. Increasing this allows better handling of bursty incoming data
                (for example scan results) and the ability for a central role to receive larger characteristic values.


        :param param: Name of the parameter.
        :type param: str

        :return: Configuration value of the given parameter.
        :rtype: Any
        """
        ...

    @overload
    def config(self, **kwargs: Any) -> None:
        """
        Set configuration values of the BLE interface.

        Currently supported values are:

            'mac':
                Set the device MAC address.
                Note: on some ports, accessing this value requires that the interface is active
                (so that the MAC address can be queried from the controller).

            'gap_name':
                Set the GAP device name used by service 0x1800, characteristic 0x2a00.
                This can be set at any time and changed multiple times.

            'rxbuf':
                Set the size in bytes of the internal buffer used to store incoming events.
                This buffer is global to the entire BLE driver and so handles incoming data for all events,
                including all characteristics. Increasing this allows better handling of bursty incoming data
                (for example scan results) and the ability for a central role to receive larger characteristic values.

        :param kwargs: Value of the supported parameter.
        :type kwargs: Any
        """
        ...

    def irq(self, handler: Any) -> None:
        """
        :param handler: Handler.
        :type handler: Any
        """
        ...

    def gap_advertise(self, interval_us: int, adv_data: Any = None, resp_data: Any = None,
                      connectable: bool = True) -> None:
        """
        Starts advertising at the specified interval (in microseconds).
        This interval will be rounded down to the nearest 625us. To stop advertising, set interval_us to None.
        adv_data and resp_data can be any type that implements the buffer protocol (e.g. bytes, bytearray, str).
        adv_data is included in all broadcasts, and resp_data is send in reply to an active scan.

        Note: if adv_data (or resp_data) is None, then the data passed to the previous call to gap_advertise
        will be re-used. This allows a broadcaster to resume advertising with just gap_advertise(interval_us).
        To clear the advertising payload pass an empty bytes, i.e. b''.

        :param interval_us: Specified interval.
        :param adv_data: adv_data
        :param resp_data: resp_data
        :param connectable: connectable

        :type interval_us:  int
        :type adv_data: Any
        :type resp_data: Any
        :type connectable: bool
        """
        ...

    def gap_scan(self, duration_ms: int, interval_us: Optional[int], window_us: Optional[int]) -> None:
        """
        Run a scan operation lasting for the specified duration (in milliseconds).
        To scan indefinitely, set duration_ms to 0.
        To stop scanning, set duration_ms to None.

        Use interval_us and window_us to optionally configure the duty cycle.
        The scanner will run for window_us microseconds every interval_us microseconds for a total of duration_ms milliseconds.
        The default interval and window are 1.28 seconds and 11.25 milliseconds respectively (background scanning).

        For each scan result the _IRQ_SCAN_RESULT event will be raised, with event data (addr_type, addr, adv_type, rssi, adv_data).
        adv_type values correspond to the Bluetooth Specification:

            0x00 - ADV_IND - connectable and scannable undirected advertising
            0x01 - ADV_DIRECT_IND - connectable directed advertising
            0x02 - ADV_SCAN_IND - scannable undirected advertising
            0x03 - ADV_NONCONN_IND - non-connectable undirected advertising
            0x04 - SCAN_RSP - scan response

        When scanning is stopped (either due to the duration finishing or when explicitly stopped), the _IRQ_SCAN_DONE event will be raised.

        :param duration_ms: Duration of the scan operation.
        :param interval_us: interval_us
        :param window_us: window_us

        :type duration_ms: int
        :type interval_us: int
        :type window_us: int
        """
        ...

    def gatts_register_services(self, services_definition: List) -> None:
        """
        Configures the peripheral with the specified services, replacing any existing services.
        services_definition is a list of services, where each service is a two-element tuple containing a UUID and
        a list of characteristics.

        Each characteristic is a two-or-three-element tuple containing a UUID, a flags value, and optionally a list of descriptors.
        Each descriptor is a two-element tuple containing a UUID and a flags value.
        The flags are a bitwise-OR combination of the ubluetooth.FLAG_READ, ubluetooth.FLAG_WRITE and
        ubluetooth.FLAG_NOTIFY values defined below.

        The return value is a list (one element per service) of tuples (each element is a value handle).
        Characteristics and descriptor handles are flattened into the same tuple, in the order that they are defined.

        :param services_definition: List of services.
        :type services_definition: List
        """
        ...

    def gatts_read(self, value_handle: Any) -> Any:
        """
        Reads the local value for this handle (which has either been written by gatts_write or by a remote central).

        :param value_handle: Handle to read.
        :type value_handle: Any

        :return: Local value for the given handle.
        :rtype: Any
        """
        ...

    def gatts_write(self, value_handle: Any, data: Any) -> None:
        """
        Writes the local value for this handle, which can be read by a central.

        :param value_handle: Handle to write.
        :param data: Handle data.

        :type value_handle: Any
        :type data: Any
        """
        ...

    def gatts_notify(self, conn_handle: Any, value_handle: Any, data: Optional[Any]) -> None:
        """
        Notifies a connected central that this value has changed and that it should issue a read of the current
        value from this peripheral.

        If data is specified, then the that value is sent to the central as part of the notification,
        avoiding the need for a separate read request.
        Note that this will not update the local value stored.

        :param conn_handle: conn_handle
        :param value_handle: value_handle
        :param data: Data.

        :type conn_handle: Any
        :type value_handle: Any
        :type data: Any
        """
        ...

    def gatts_set_buffer(self, value_handle: Any, length: bytes, append: bool = False) -> None:
        """
        Sets the internal buffer size for a value in bytes. This will limit the largest possible write that can be received.
        The default is 20.
        Setting append to True will make all remote writes append to, rather than replace, the current value.
        At most len bytes can be buffered in this way. When you use gatts_read, the value will be cleared after reading.
        This feature is useful when implementing something like the Nordic UART Service.

        :param value_handle: value_handle
        :param length: Buffer size.
        :param append: Set to True will make the remote writes append to the current value, False will replace.

        :type value_handle: Any
        :type length: bytes
        :type append: bool
        """
        ...

    def gap_connect(self, addr_type: Any, addr: Any, scan_duration_ms: int =2000) -> None:
        """
        Connect to a peripheral.
        On success, the _IRQ_PERIPHERAL_CONNECT event will be raised.

        :param addr_type: addr_type
        :param addr: addr
        :param scan_duration_ms: Scan duration.

        :type addr_type: Any
        :type addr: Any
        :type scan_duration_ms: int
        """
        ...

    def gap_disconnect(self, conn_handle: Any) -> bool:
        """
        Disconnect the specified connection handle.
        On success, the _IRQ_PERIPHERAL_DISCONNECT event will be raised.
        Returns False if the connection handle wasn’t connected, and True otherwise.

        :param conn_handle: Connection handle.
        :type conn_handle: Any

        :return: Returns False if the connection handle wasn’t connected, and True otherwise.
        :rtype: bool
        """
        ...

    def gattc_discover_services(self, conn_handle: Any, uuid: Optional[UUID]) -> None:
        """
        Query a connected peripheral for its services.
        Optionally specify a service uuid to query for that service only.
        For each service discovered, the _IRQ_GATTC_SERVICE_RESULT event will be raised,
        followed by _IRQ_GATTC_SERVICE_DONE on completion.

        :param conn_handle: Connection handle.
        :param uuid: UUID object.

        :type conn_handle: Any
        :type uuid: UUID
        """
        ...

    def gattc_discover_characteristics(self, conn_handle: Any, start_handle: Any, end_handle: Any, uuid: Optional[UUID]) -> None:
        """
        Query a connected peripheral for characteristics in the specified range.
        Optionally specify a characteristic uuid to query for that characteristic only.
        You can use start_handle=1, end_handle=0xffff to search for a characteristic in any service.
        For each characteristic discovered, the _IRQ_GATTC_CHARACTERISTIC_RESULT event will be raised,
        followed by _IRQ_GATTC_CHARACTERISTIC_DONE on completion.

        :param conn_handle: Connection handle.
        :param start_handle: start_handle
        :param end_handle: end_handle
        :param uuid: UUID object.

        :type conn_handle: Any
        :type start_handle: Any
        :type end_handle: Any
        :type uuid: UUID

        """
        ...

    def gattc_discover_descriptors(self, conn_handle: Any, start_handle: Any, end_handle: Any) -> None:
        """
        Query a connected peripheral for descriptors in the specified range.
        For each descriptor discovered, the _IRQ_GATTC_DESCRIPTOR_RESULT event will be raised,
        followed by _IRQ_GATTC_DESCRIPTOR_DONE on completion.

        :param conn_handle: Connection handle.
        :param start_handle: start_handle
        :param end_handle: end_handle

        :type conn_handle: Any
        :type start_handle: Any
        :type end_handle: Any
        """
        ...

    def gattc_read(self, conn_handle: Any, value_handle: Any) -> None:
        """
        Issue a remote read to a connected peripheral for the specified characteristic or descriptor handle.
        When a value is available, the _IRQ_GATTC_READ_RESULT event will be raised. Additionally,
        the _IRQ_GATTC_READ_DONE will be raised.

        :param conn_handle: Connection handle.
        :param value_handle: value_handle

        :type conn_handle: Any
        :type value_handle: Any
        """
        ...

    def gattc_write(self, conn_handle: Any, value_handle:Any , data: Any, mode: int = 0) -> None:
        """
        Issue a remote write to a connected peripheral for the specified characteristic or descriptor handle.
        The argument mode specifies the write behaviour, with the currently supported values being:

        mode=0  (default) is a write-without-response:
                the write will be sent to the remote peripheral but no confirmation will be returned,
                and no event will be raised.

        mode=1  is a write-with-response:
                the remote peripheral is requested to send a response/acknowledgement that it received the data.

        If a response is received from the remote peripheral the _IRQ_GATTC_WRITE_DONE event will be raised.

        :param conn_handle: Connection handle.
        :param value_handle: value_handle
        :param data: Data.
        :param mode: Write-without-response mode.

        :type conn_handle: Any
        :type value_handle: Any
        :type data: Any
        :type mode: int
        """
        ...


class UUID:

    @overload
    def __init__(self, value: int) -> None:
        """
        Creates a UUID instance with the specified 16-bit integer (e.g. 0x2908) value.
        """
        ...

    @overload
    def __init__(self, value: str) -> None:
        """
        Creates a UUID instance with the specified 128-bit UUID string (e.g. '6E400001-B5A3-F393-E0A9-E50E24DCCA9E') value.
        """
        ...


FLAG_READ: Any
FLAG_WRITE: Any
FLAG_NOTIFY: Any
