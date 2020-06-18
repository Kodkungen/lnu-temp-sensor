function Decoder(bytes, port) {
    // Decode an uplink message from a buffer
    // (array) of bytes to an object of fields.

    // byte 7 temp from dht
    var dth_temp = bytes[1];
    // byte 8 RH from dht
    var dth_RH = bytes[2];

    return {
        dth_temp: (dth_temp) / (256 / 125) - 40,
        dth_RH: dth_RH / (256 / 100)
    }
}