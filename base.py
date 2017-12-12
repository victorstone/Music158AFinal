from OSC import OSCClient, OSCBundle

DEFAULTPORT = 54345
NUM_CAPS_AND_POTS = 4

class PacketManager(object):
    def __init__(self, num_datapoints, port=DEFAULTPORT):
        self.num_datapoints = num_datapoints
        self.data_source = None
        self.client = OSCClient()
        self.client.connect(("localhost", port))

    def add_data_source(self, data_source):
        self.data_source = data_source

    def send_to_max(self):
        bundle = OSCBundle()
        for i in range(NUM_CAPS_AND_POTS):
            bundle.append({'addr': "/d" + str(i) + "/hz", 'args': self.data_source.get_pitch_data(i)})
            bundle.append({'addr': "/d" + str(i) + "/on", 'args': self.data_source.get_cap_data(i)})
        bundle.append({'addr': "/duration", 'args': self.data_source.get_duration_data()})
        bundle.append({'addr': "/mod", 'args': self.data_source.get_mod_data()})
        self.client.send(bundle)


