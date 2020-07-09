function Decoder(bytes, port) {

  // byte 0,1 are for co2. No need of signed, and range of sensor is 400-8192.
  var co2 = (bytes[0] << 8) | bytes[1];
  // byte 2,3 are for VOC. range 0-1187de
  var voc = (bytes[2] << 8) | bytes[3];

    var photo_res = bytes[4];

    var soilMoisturePlantOne = bytes[5];
    var soilMoisturePlantTwo = bytes[6];
    var soilMoisturePlantThree = bytes[7];
    
    var waterLevelPlantOne = bytes[8];
    var waterLevelPlantTwo = bytes[9];
    var waterLevelPlantThree = bytes[10];

    // byte 0 temp from dht
    var dht_temp = bytes[11];
    // byte 1 RH from dht
    var dht_RH = bytes[12];
  

    return {
        co2: co2,
        voc: voc,
        photo_res: (photo_res * 16),
        soilMoisturePlantOne: (soilMoisturePlantOne * 16),
        soilMoisturePlantTwo: (soilMoisturePlantTwo * 16),
        soilMoisturePlantThree: (soilMoisturePlantThree * 16),
        waterLevelPlantOne: (waterLevelPlantOne * 16),
        waterLevelPlantTwo: (waterLevelPlantTwo * 16),
        waterLevelPlantThree: (waterLevelPlantThree * 16),
        dht_temp: (dht_temp) / (256 / 125) - 40,
        dht_RH: dht_RH / (256 / 100),
    };
}
