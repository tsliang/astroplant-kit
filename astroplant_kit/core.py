import astroplant_client
from kit import Kit
import config

if __name__ == "__main__":
    #sensor_manager = SensorManager()
    #sensor_manager.add_sensor(astroplant_sensor_library.sensors.mock.Mock)

    conf = config.read_config()
    api_client = astroplant_client.Client(conf["api"]["root"], conf["websockets"]["url"])
    api_client.authenticate(conf["auth"]["serial"], conf["auth"]["secret"])

    kit = Kit(api_client)
    kit.run()
