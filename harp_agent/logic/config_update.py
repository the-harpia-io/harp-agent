import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import harp_agent.settings as settings
import yaml
from microservice_template_core.tools.logger import get_logger

logger = get_logger()


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        logger.info(msg=f"Config file was modified - {event.src_path}")

        with open(settings.PATH_TO_MS_CONFIG) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

        self.update_ms_configs(data=data)

    @classmethod
    def update_config_after_start(cls):
        logger.info(msg=f"Config was update after start")

        with open(settings.PATH_TO_MS_CONFIG) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

        MyHandler.update_ms_configs(data=data)

    @classmethod
    def update_ms_configs(cls, data):
        settings.ZABBIX_SYSTEMS.clear()
        settings.ICINGA_SYSTEMS.clear()

        for monitoring_system in data:
            if data[monitoring_system]:
                for system_body in data[monitoring_system]:
                    system_payload = {
                        'url': system_body['url'],
                        'user': system_body['user'],
                        'password': system_body['password']
                    }
                    if monitoring_system == 'zabbix':
                        settings.ZABBIX_SYSTEMS.append(system_payload)

                    if monitoring_system == 'icinga':
                        settings.ICINGA_SYSTEMS.append(system_payload)

        logger.info(msg=f"ZABBIX_SYSTEMS after modification - {settings.ZABBIX_SYSTEMS}")
        logger.info(msg=f"ICINGA_SYSTEMS after modification - {settings.ICINGA_SYSTEMS}")


def update_configuration():
    MyHandler.update_config_after_start()
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=settings.PATH_TO_MS_CONFIG, recursive=False)
    observer.start()

    try:
        while True:
            with open(settings.PATH_TO_MS_CONFIG) as file:
                data = yaml.load(file, Loader=yaml.FullLoader)
            print(data)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    except Exception as err:
        print(err)
    observer.join()
