import logging
import datetime
import time
import random
from random import randint
import wishful_upis as upis
from wishful_agent.core import wishful_module
from wishful_agent.timer import TimerEventSender

__author__ = "Anatolij Zubow"
__copyright__ = "Copyright (c) 2016, Technische Universität Berlin"
__version__ = "0.1.0"
__email__ = "{zubow}@tkn.tu-berlin.de"

'''
Local test of WiFi component.

sudo ../../../dev/bin/wishful-agent --config config_local.yaml
'''

@wishful_module.build_module
class WifiTestController(wishful_module.ControllerModule):
    def __init__(self):
        super(WifiTestController, self).__init__()
        self.log = logging.getLogger('WifiTestController')

    @wishful_module.on_start()
    def my_start_function(self):
        self.log.info("start wifi test")

        try:
            node = self.localNode
            self.log.info(node)
            device = node.get_device(0)
            self.log.info(device)

            iface = 'wlan6'

            curr_pwr = device.radio.get_tx_power(iface)
            self.log.info('WIFI::get_power %d' % curr_pwr)

            new_pwr = randint(1,17)
            self.log.info('WIFI::set_power to %d' % new_pwr)
            curr_pwr = device.radio.set_tx_power(new_pwr, iface)

            time.sleep(0.5)

            curr_pwr = device.radio.get_tx_power(iface)
            self.log.info('WIFI::get_power %d' % curr_pwr)

        except Exception as e:
            self.log.error("{} Failed, err_msg: {}".format(datetime.datetime.now(), e))

        self.log.info('... done')

    @wishful_module.on_exit()
    def my_stop_function(self):
        self.log.info("stop wifi test")
