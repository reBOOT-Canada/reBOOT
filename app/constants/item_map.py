'''
ITEM_MAP is a dict of format:
{
    'legacy item description': {
        'category': 'category a',
        'device_type': 'device type a'
    }
}
'''
ITEM_MAP = {
    '': {'category': '', 'device_type': ''},
    'access point': {   'category': 'NETWORK', 'device_type': 'access point'},
    'access point (wireless)': {   'category': 'NETWORK',
                                   'device_type': 'access point'},
    'access point - wireless': {   'category': 'NETWORK',
                                   'device_type': 'access point'},
    'audio streamer': {   'category': 'AUDIO', 'device_type': 'streamer'},
    'base station (wireless)': {   'category': 'NETWORK',
                                   'device_type': 'access point'},
    'battery (li-ion)': {   'category': 'BATTERY', 'device_type': 'li-ion'},
    'battery (ni-mh)': {   'category': 'BATTERY', 'device_type': 'ni-mh'},
    'battery (power bank)': {   'category': 'BATTERY',
                                'device_type': 'power bank'},
    'battery (ups)': {   'category': 'BATTERY', 'device_type': 'ups'},
    'battery (vrla)': {   'category': 'BATTERY', 'device_type': 'vrla'},
    'battery - ups': {   'category': 'BATTERY', 'device_type': 'ups'},
    'bookshelf stereo': {   'category': 'AUDIO', 'device_type': 'stereo'},
    'boombox': {   'category': 'AUDIO', 'device_type': 'boombox'},
    'broadband router': {   'category': 'NETWORK', 'device_type': 'router'},
    'cable lock': {   'category': 'PERIPHERAL', 'device_type': 'cable lock'},
    'camcorder': {   'category': 'CAMERA', 'device_type': 'video'},
    'camera': {   'category': 'CAMERA', 'device_type': 'camera'},
    'camera (cctv)': {   'category': 'CAMERA', 'device_type': 'cctv'},
    'camera (digital)': {   'category': 'CAMERA', 'device_type': 'digital'},
    'camera (film)': {   'category': 'CAMERA', 'device_type': 'film'},
    'camera (video)': {   'category': 'CAMERA', 'device_type': 'video'},
    'camera (wi-fi)': {   'category': 'CAMERA', 'device_type': 'wifi camera'},
    'camera - cctv': {   'category': 'CAMERA', 'device_type': 'cctv'},
    'camera - digital': {   'category': 'CAMERA', 'device_type': 'digital'},
    'camera - film': {   'category': 'CAMERA', 'device_type': 'film'},
    'camera - video': {   'category': 'CAMERA', 'device_type': 'video'},
    'cell phone': {   'category': 'PHONE', 'device_type': 'cell phone'},
    'cellphone': {   'category': 'PHONE', 'device_type': 'cell phone'},
    'charging cradle': {   'category': 'PERIPHERAL',
                           'device_type': 'charging cradle'},
    'compuer - tower': {   'category': 'COMPUTER', 'device_type': 'tower'},
    'computer': {   'category': 'COMPUTER', 'device_type': 'computer'},
    'computer (all-in-one)': {   'category': 'COMPUTER',
                                 'device_type': 'all in one'},
    'computer (desktop)': {   'category': 'COMPUTER', 'device_type': 'desktop'},
    'computer (laptop)': {   'category': 'COMPUTER', 'device_type': 'laptop'},
    'computer (pocket pc)': {   'category': 'COMPUTER',
                                'device_type': 'pocket pc'},
    'computer (server)': {   'category': 'COMPUTER', 'device_type': 'server'},
    'computer (tablet)': {   'category': 'TABLET', 'device_type': 'tablet'},
    'computer (thin client)': {   'category': 'COMPUTER',
                                  'device_type': 'thin client'},
    'computer (tower)': {   'category': 'COMPUTER', 'device_type': 'tower'},
    'computer (workstation)': {   'category': 'COMPUTER',
                                  'device_type': 'computer'},
    'computer - all-in-one': {   'category': 'COMPUTER',
                                 'device_type': 'all in one'},
    'computer - complete': {   'category': 'COMPUTER', 'device_type': 'desktop'},
    'computer - desktop': {   'category': 'COMPUTER', 'device_type': 'desktop'},
    'computer - laptop': {   'category': 'COMPUTER', 'device_type': 'laptop'},
    'computer - server': {   'category': 'COMPUTER', 'device_type': 'server'},
    'computer - sff': {   'category': 'COMPUTER', 'device_type': 'sff'},
    'computer - ssf': {   'category': 'COMPUTER', 'device_type': 'ssf'},
    'computer - tablet': {   'category': 'TABLET', 'device_type': 'tablet'},
    'computer - thin client': {   'category': 'COMPUTER',
                                  'device_type': 'thin client'},
    'computer - tower': {   'category': 'COMPUTER', 'device_type': 'tower'},
    'computer - usff': {   'category': 'COMPUTER', 'device_type': 'ussf'},
    'computer - workstation': {   'category': 'COMPUTER',
                                  'device_type': 'desktop'},
    'computer case': {   'category': 'PERIPHERAL',
                         'device_type': 'computer case'},
    'controller card': {   'category': 'COMPONENT',
                           'device_type': 'controller card'},
    'copier (digital)': {   'category': 'PRINTER', 'device_type': 'digital'},
    'copier (personal)': {   'category': 'PRINTER', 'device_type': 'copier'},
    'copier - digital': {   'category': 'PRINTER', 'device_type': 'copier'},
    'docking station': {   'category': 'PERIPHERAL',
                           'device_type': 'docking station'},
    'e-reader': {   'category': 'TABLET', 'device_type': 'e-reader'},
    'earphones': {   'category': 'AUDIO', 'device_type': 'earphones'},
    'earphones (wireless)': {   'category': 'AUDIO', 'device_type': 'earphones'},
    'ereader': {   'category': 'TABLET', 'device_type': 'e-reader'},
    'ethernet adapter': {   'category': 'COMPONENT', 'device_type': 'nic'},
    'ethernet adaptor': {   'category': 'NETWORK', 'device_type': 'ethernet'},
    'fax imaging film': {   'category': 'PRINTER',
                            'device_type': 'fax imaging film'},
    'fax machine': {   'category': 'PRINTER', 'device_type': 'fax machine'},
    'firewall appliance': {   'category': 'NETWORK', 'device_type': 'firewall'},
    'firewall/router': {   'category': 'NETWORK',
                           'device_type': 'security appliance'},
    'flash drive (usb)': {   'category': 'STORAGE', 'device_type': 'usb'},
    'floppy drive': {   'category': 'STORAGE', 'device_type': 'floppy drive'},
    'gateway': {   'category': 'NETWORK', 'device_type': 'gateway'},
    'gps unit': {   'category': 'SMALL_ELECTRIC_NON_IT',
                    'device_type': 'small electric non-IT'},
    'graphics card': {   'category': 'COMPONENT', 'device_type': 'graphic card'},
    'graphics processor': {   'category': 'COMPONENT',
                              'device_type': 'graphic card'},
    'graphics tablet': {   'category': 'TABLET', 'device_type': 'graphics'},
    'hard drive': {   'category': 'STORAGE', 'device_type': 'hard drive'},
    'hard drive (ata)': {   'category': 'STORAGE', 'device_type': 'hd ata'},
    'hard drive (external)': {   'category': 'STORAGE',
                                 'device_type': 'hd external'},
    'hard drive (fcal)': {   'category': 'STORAGE', 'device_type': 'hd fcal'},
    'hard drive (ide)': {   'category': 'STORAGE', 'device_type': 'hd ide'},
    'hard drive (pata)': {   'category': 'STORAGE', 'device_type': 'hd pata'},
    'hard drive (sas)': {   'category': 'STORAGE', 'device_type': 'hd sas'},
    'hard drive (sata)': {   'category': 'STORAGE', 'device_type': 'hd sata'},
    'hard drive (scsi)': {   'category': 'STORAGE', 'device_type': 'hd scsi'},
    'hard drive (ssd)': {   'category': 'STORAGE', 'device_type': 'hd ssd'},
    'hard drive - ata': {   'category': 'STORAGE', 'device_type': 'hd ata'},
    'hard drive - external': {   'category': 'STORAGE',
                                 'device_type': 'external'},
    'hard drive - ide': {   'category': 'STORAGE', 'device_type': 'hd ide'},
    'hard drive - sas': {   'category': 'STORAGE', 'device_type': 'hd sas'},
    'hard drive - sata': {   'category': 'STORAGE', 'device_type': 'hd sata'},
    'hard drive - scsi': {   'category': 'STORAGE', 'device_type': 'hd scsi'},
    'hard drive - ssd': {   'category': 'STORAGE', 'device_type': 'hd ssd'},
    'hard drive enclosure': {   'category': 'STORAGE',
                                'device_type': 'hard drive enclosure'},
    'hard drives': {   'category': 'STORAGE', 'device_type': 'hard drive'},
    'hdd': {   'category': 'STORAGE', 'device_type': 'hd'},
    'hdd (sata)': {   'category': 'STORAGE', 'device_type': 'hd sata'},
    'headphones': {   'category': 'PERIPHERAL', 'device_type': 'headphones'},
    'headphones (bt)': {   'category': 'PERIPHERAL', 'device_type': 'headphones'},
    'headphones (wireless)': {   'category': 'PERIPHERAL',
                                 'device_type': 'headphones'},
    'headset': {   'category': 'PERIPHERAL', 'device_type': 'headset'},
    'headset (bluetooth)': {   'category': 'PERIPHERAL',
                               'device_type': 'headset'},
    'headset (bt)': {   'category': 'PERIPHERAL', 'device_type': 'headset'},
    'headset (wireless)': {   'category': 'PERIPHERAL', 'device_type': 'headset'},
    'home theatre (2.1)': {   'category': 'VIDEO', 'device_type': 'home theater'},
    'home theatre (5.1)': {   'category': 'VIDEO', 'device_type': 'home theater'},
    'home theatre system': {   'category': 'VIDEO',
                               'device_type': 'home theater'},
    'hub (ethernet)': {   'category': 'NETWORK', 'device_type': 'ethernet'},
    'hub (rackmount)': {   'category': 'NETWORK', 'device_type': 'hub'},
    'ink cartridge': {   'category': 'PRINTER', 'device_type': 'ink'},
    'ink cartridge (new)': {   'category': 'PRINTER', 'device_type': 'ink new'},
    'keyboard': {   'category': 'PERIPHERAL', 'device_type': 'keyboard'},
    'keyboard (bluetooth)': {   'category': 'PERIPHERAL',
                                'device_type': 'keyboard'},
    'keyboard (bt)': {   'category': 'PERIPHERAL', 'device_type': 'keyboard'},
    'keyboard (ps/2)': {   'category': 'PERIPHERAL', 'device_type': 'keyboard'},
    'keyboard (rf)': {   'category': 'PERIPHERAL', 'device_type': 'keyboard'},
    'keyboard (usb)': {   'category': 'PERIPHERAL', 'device_type': 'keyboard'},
    'keyboard (wireless)': {   'category': 'PERIPHERAL',
                               'device_type': 'keyboard'},
    'keypad': {   'category': 'PERIPHERAL', 'device_type': 'keypad'},
    'laptop': {   'category': 'COMPUTER', 'device_type': 'laptop'},
    'laptop bag': {   'category': 'PERIPHERAL', 'device_type': 'laptop bag'},
    'lock': {   'category': 'PERIPHERAL', 'device_type': 'lock'},
    'ltv - lcd': {   'category': 'MONITOR', 'device_type': 'lcd'},
    'm isc cables': {   'category': 'CABLES', 'device_type': 'cable'},
    'media player': {   'category': 'VIDEO', 'device_type': 'media player'},
    'media streamer': {   'category': 'VIDEO', 'device_type': 'streamer'},
    'misc cables': {   'category': 'CABLES', 'device_type': 'misc'},
    'misc cords/cables': {   'category': 'CABLES', 'device_type': 'misc'},
    'misc dispose': {   'category': 'DISPOSE', 'device_type': 'dispose'},
    'misc scarp': {   'category': 'RECYCLE', 'device_type': 'misc'},
    'misc small electronics': {   'category': 'SMALL_ELECTRIC_NON_IT',
                                  'device_type': 'misc small electronics'},
    'misc software': {   'category': 'SOFTWARE', 'device_type': 'software'},
    'misc. cords/cables': {   'category': 'CABLES', 'device_type': 'misc'},
    'misc. electronics': {   'category': 'SMALL_ELECTRIC_NON_IT',
                             'device_type': 'misc small electronics'},
    'misc. small electronics': {   'category': 'SMALL_ELECTRIC_NON_IT',
                                   'device_type': 'misc small electronics'},
    'miscellaneous': {   'category': 'ASSORTED', 'device_type': 'misc'},
    'modem': {   'category': 'NETWORK', 'device_type': 'modem'},
    'modem (cable)': {   'category': 'NETWORK', 'device_type': 'cable'},
    'modem (dsl)': {   'category': 'NETWORK', 'device_type': 'modem'},
    'modem (telephony)': {   'category': 'NETWORK', 'device_type': 'modem'},
    'modem - broadband': {   'category': 'NETWORK', 'device_type': 'router'},
    'modem - cable': {   'category': 'NETWORK', 'device_type': 'cable'},
    'modem - dsl': {   'category': 'NETWORK', 'device_type': 'modem'},
    'modem/router': {   'category': 'NETWORK', 'device_type': 'modem'},
    'monetary donation': {   'category': 'CASH DONATION',
                             'device_type': 'cash donation'},
    'monitor': {   'category': 'MONITOR', 'device_type': 'monitor'},
    'monitor (crt)': {   'category': 'MONITOR', 'device_type': 'crt'},
    'monitor (lcd)': {   'category': 'MONITOR', 'device_type': 'lcd'},
    'monitor (touchscreen)': {   'category': 'MONITOR',
                                 'device_type': 'touchscreen'},
    'monitor - crt': {   'category': 'MONITOR', 'device_type': 'crt'},
    'monitor - flat': {   'category': 'MONITOR', 'device_type': 'flat screen'},
    'monitor - lcd': {   'category': 'MONITOR', 'device_type': 'lcd'},
    'monitor - led': {   'category': 'MONITOR', 'device_type': 'led'},
    'monitor - plasma': {   'category': 'MONITOR', 'device_type': 'plasma'},
    'monitor stand': {   'category': 'PERIPHERAL',
                         'device_type': 'stand/mount/frame enclosure'},
    'motherboard': {   'category': 'COMPONENT', 'device_type': 'motherboard'},
    'mouse': {   'category': 'PERIPHERAL', 'device_type': 'mouse'},
    'mouse (bluetooth)': {   'category': 'PERIPHERAL', 'device_type': 'mouse'},
    'mouse (bt)': {   'category': 'PERIPHERAL', 'device_type': 'mouse'},
    'mouse (ps/2)': {   'category': 'PERIPHERAL', 'device_type': 'mouse'},
    'mouse (rf)': {   'category': 'PERIPHERAL', 'device_type': 'mouse'},
    'mouse (usb)': {   'category': 'PERIPHERAL', 'device_type': 'mouse'},
    'mouse (wireless)': {   'category': 'PERIPHERAL', 'device_type': 'mouse'},
    'multimedia projector': {   'category': 'VIDEO', 'device_type': 'tv plasma'},
    'network adapter': {   'category': 'COMPONENT', 'device_type': 'nic'},
    'network adapter (bluetooth)': {   'category': 'PERIPHERAL',
                                       'device_type': 'bluetooth adapter'},
    'network adapter (cardbus)': {   'category': 'PERIPHERAL',
                                     'device_type': 'CardBus card'},
    'network adapter (expresscard)': {   'category': 'PERIPHERAL',
                                         'device_type': 'usb adapter'},
    'network adapter (hspa)': {   'category': 'PERIPHERAL',
                                  'device_type': 'hspa adapter'},
    'network adapter (pci)': {   'category': 'NETWORK',
                                 'device_type': 'pci adapter'},
    'network adapter (pcmcia)': {   'category': 'PERIPHERAL',
                                    'device_type': 'pcmcia card'},
    'network adapter (usb)': {   'category': 'PERIPHERAL',
                                 'device_type': 'wifi adapter'},
    'network adapter (wi-fi)': {   'category': 'NETWORK',
                                   'device_type': 'wifi adapter'},
    'network adapter (wifi)': {   'category': 'PERIPHERAL',
                                  'device_type': 'wifi adapter'},
    'network adapter - wireless': {   'category': 'PERIPHERAL',
                                      'device_type': 'wifi adapter'},
    'no value': {   'category': 'DISPOSE', 'device_type': 'dispose'},
    'notebook adapter': {   'category': 'POWER_SUPPLY', 'device_type': 'charger'},
    'notebook adaptor': {   'category': 'POWER_SUPPLY', 'device_type': 'charger'},
    'optical drive': {   'category': 'STORAGE', 'device_type': 'optical drive'},
    'pci adapter': {   'category': 'COMPONENT', 'device_type': 'pci adapter'},
    'perinter - inkjet': {   'category': 'PRINTER', 'device_type': 'ink jet'},
    'phone handset': {   'category': 'PHONE', 'device_type': 'handset'},
    'photo copier +50lbs': {   'category': 'PRINTER', 'device_type': 'copier'},
    'port replicator': {   'category': 'PERIPHERAL',
                           'device_type': 'port replicator'},
    'power adapter': {   'category': 'POWER_SUPPLY', 'device_type': 'charger'},
    'power adaptor': {   'category': 'POWER_SUPPLY', 'device_type': 'charger'},
    'power distribution unit': {   'category': 'POWER_SUPPLY',
                                   'device_type': 'power supply unit'},
    'power supply module': {   'category': 'COMPONENT',
                               'device_type': 'power supply module'},
    'power supply unit': {   'category': 'POWER_SUPPLY',
                             'device_type': 'power supply unit'},
    'power tap': {   'category': 'POWER_SUPPLY', 'device_type': 'power tap'},
    'print server': {   'category': 'PRINTER', 'device_type': 'print server'},
    'print server - wireless': {   'category': 'PRINTER',
                                   'device_type': 'print server'},
    'printer': {   'category': 'PRINTER', 'device_type': 'printer'},
    'printer (all-in-one)': {   'category': 'PRINTER', 'device_type': 'mfp'},
    'printer (impact)': {   'category': 'PRINTER', 'device_type': 'impact'},
    'printer (inkjet)': {   'category': 'PRINTER', 'device_type': 'ink jet'},
    'printer (label maker)': {   'category': 'PRINTER',
                                 'device_type': 'label maker'},
    'printer (laser)': {   'category': 'PRINTER', 'device_type': 'laser'},
    'printer (multifunction)': {   'category': 'PRINTER', 'device_type': 'mfp'},
    'printer (plotter)': {   'category': 'PRINTER', 'device_type': 'plotter'},
    'printer (thermal)': {   'category': 'PRINTER', 'device_type': 'thermal'},
    'printer - all-in-one': {   'category': 'PRINTER', 'device_type': 'mfp'},
    'printer - dot matirx': {   'category': 'PRINTER',
                                'device_type': 'dot matrix'},
    'printer - dot matrix': {   'category': 'PRINTER',
                                'device_type': 'dot matrix'},
    'printer - impact': {   'category': 'PRINTER', 'device_type': 'impact'},
    'printer - ink': {   'category': 'PRINTER', 'device_type': 'ink'},
    'printer - ink jet': {   'category': 'PRINTER', 'device_type': 'ink jet'},
    'printer - inkjet': {   'category': 'PRINTER', 'device_type': 'ink jet'},
    'printer - label maker': {   'category': 'PRINTER',
                                 'device_type': 'label maker'},
    'printer - laser': {   'category': 'PRINTER', 'device_type': 'laser'},
    'printer - multifunction': {   'category': 'PRINTER', 'device_type': 'mfp'},
    'printer - multifuntion': {   'category': 'PRINTER', 'device_type': 'mfp'},
    'printer - plotter': {   'category': 'PRINTER', 'device_type': 'plotter'},
    'printer - thermal': {   'category': 'PRINTER', 'device_type': 'thermal'},
    'printer -laser': {   'category': 'PRINTER', 'device_type': 'laser'},
    'projector (dlp)': {   'category': 'VIDEO', 'device_type': 'tv plasma'},
    'projector (lcd)': {   'category': 'VIDEO', 'device_type': 'lcd projector'},
    'projector (led)': {   'category': 'VIDEO', 'device_type': 'tv plasma'},
    'psu': {   'category': 'POWER_SUPPLY', 'device_type': 'power supply unit'},
    'ram (per chip)': {   'category': 'STORAGE', 'device_type': 'RAM'},
    'ram chip': {   'category': 'STORAGE', 'device_type': 'RAM'},
    'ram per chip': {   'category': 'STORAGE', 'device_type': 'RAM'},
    'receiver': {   'category': 'AUDIO', 'device_type': 'receiver'},
    'receiver (bt)': {   'category': 'AUDIO', 'device_type': 'receiver'},
    'receiver (catv)': {   'category': 'VIDEO', 'device_type': 'catv receiver'},
    'receiver (hdtv)': {   'category': 'VIDEO', 'device_type': 'hdtv'},
    'receiver (rf)': {   'category': 'AUDIO', 'device_type': 'receiver'},
    'remote control': {   'category': 'VIDEO', 'device_type': 'remote control'},
    'replicator port': {   'category': 'PERIPHERAL',
                           'device_type': 'port replicator'},
    'router': {   'category': 'NETWORK', 'device_type': 'router'},
    'router (broadband)': {   'category': 'NETWORK', 'device_type': 'router'},
    'router (integrated)': {   'category': 'NETWORK', 'device_type': 'router'},
    'router (isr)': {   'category': 'NETWORK', 'device_type': 'router'},
    'router (vpn)': {   'category': 'NETWORK', 'device_type': 'router'},
    'router - broadband': {   'category': 'NETWORK', 'device_type': 'router'},
    'router - network': {   'category': 'NETWORK', 'device_type': 'router'},
    'router/ap': {   'category': 'NETWORK', 'device_type': 'access point'},
    'router/nas': {   'category': 'STORAGE', 'device_type': 'NAS'},
    'scanner': {   'category': 'PRINTER', 'device_type': 'scanner'},
    'security appliance': {   'category': 'NETWORK',
                              'device_type': 'security appliance'},
    'server': {   'category': 'COMPUTER', 'device_type': 'server'},
    'server (rackmount)': {   'category': 'COMPUTER', 'device_type': 'server'},
    'shredder': {   'category': 'SMALL_ELECTRIC_NON_IT',
                    'device_type': 'shredder'},
    'smartphone': {   'category': 'PHONE', 'device_type': 'smartphone'},
    'software': {   'category': 'SOFTWARE', 'device_type': 'software'},
    'solid state drive (sata)': {   'category': 'STORAGE',
                                    'device_type': 'hd ss sata'},
    'sound card': {   'category': 'COMPONENT', 'device_type': 'sound card'},
    'soundbar': {   'category': 'AUDIO', 'device_type': 'soundbar'},
    'speaker': {   'category': 'AUDIO', 'device_type': 'speaker'},
    'speaker (bluetooth)': {   'category': 'AUDIO', 'device_type': 'speaker'},
    'speaker (bookshelf)': {   'category': 'AUDIO', 'device_type': 'speaker'},
    'speaker (hi-fi)': {   'category': 'AUDIO', 'device_type': 'speaker'},
    'speaker (smart)': {   'category': 'AUDIO', 'device_type': 'speaker'},
    'speaker (wireless)': {   'category': 'AUDIO', 'device_type': 'speakers'},
    'speaker dock': {   'category': 'AUDIO', 'device_type': 'speaker dock'},
    'speakers': {   'category': 'AUDIO', 'device_type': 'speakers'},
    'speakers (2.0)': {   'category': 'AUDIO', 'device_type': 'speakers'},
    'speakers (2.1)': {   'category': 'AUDIO', 'device_type': 'speakers'},
    'speakers (5.1)': {   'category': 'AUDIO', 'device_type': 'speakers'},
    'speakers (hi-fi)': {   'category': 'AUDIO', 'device_type': 'hi-fi'},
    'stereo (bookshelf)': {   'category': 'AUDIO', 'device_type': 'speaker'},
    'storage (flash)': {   'category': 'STORAGE', 'device_type': 'flash'},
    'storage (nas)': {   'category': 'STORAGE', 'device_type': 'nas'},
    'storage (raid)': {   'category': 'STORAGE', 'device_type': 'raid'},
    'storage (usb)': {   'category': 'STORAGE', 'device_type': 'usb'},
    'storage array': {   'category': 'STORAGE', 'device_type': 'array'},
    'subwoofer': {   'category': 'AUDIO', 'device_type': 'subwoofer'},
    'surge protector': {   'category': 'POWER_SUPPLY',
                           'device_type': 'surge protector'},
    'switch': {   'category': 'NETWORK', 'device_type': 'switch'},
    'switch (desktop)': {   'category': 'NETWORK', 'device_type': 'switch'},
    'switch (ethernet)': {   'category': 'NETWORK', 'device_type': 'ethernet'},
    'switch (gigabit)': {   'category': 'NETWORK', 'device_type': 'switch'},
    'switch (kvm)': {   'category': 'PERIPHERAL', 'device_type': 'kvm switch'},
    'switch (network)': {   'category': 'NETWORK', 'device_type': 'switch'},
    'switch (rackmount)': {   'category': 'NETWORK', 'device_type': 'switch'},
    'switch (vpn)': {   'category': 'NETWORK', 'device_type': 'switch'},
    'switch (wemo)': {   'category': 'NETWORK', 'device_type': 'switch'},
    'switch - desktop': {   'category': 'NETWORK', 'device_type': 'switch'},
    'switch - kvm': {   'category': 'PERIPHERAL', 'device_type': 'kvm switch'},
    'switch - rack mount': {   'category': 'NETWORK', 'device_type': 'switch'},
    'switch - rackmount': {   'category': 'NETWORK', 'device_type': 'switch'},
    'tape drive': {   'category': 'STORAGE', 'device_type': 'tape drive'},
    'telephone': {   'category': 'PHONE', 'device_type': 'telephone'},
    'telephone (business)': {   'category': 'PHONE', 'device_type': 'business'},
    'telephone (conference)': {   'category': 'PHONE',
                                  'device_type': 'conference'},
    'telephone (cordless)': {   'category': 'PHONE', 'device_type': 'cordless'},
    'telephone (voip)': {   'category': 'PHONE', 'device_type': 'voip'},
    'telephone - business': {   'category': 'PHONE', 'device_type': 'business'},
    'telephone - conference': {   'category': 'PHONE',
                                  'device_type': 'conference'},
    'telephone - cordless': {   'category': 'PHONE', 'device_type': 'cordless'},
    'telephone - voip': {   'category': 'PHONE', 'device_type': 'voip'},
    'telephone kit': {   'category': 'PHONE', 'device_type': 'kit'},
    'telephone receiver': {   'category': 'PHONE', 'device_type': 'receiver'},
    'terminal - thin client': {   'category': 'COMPUTER',
                                  'device_type': 'thin client'},
    'toner': {   'category': 'PRINTER', 'device_type': 'toner new'},
    'toner (new)': {   'category': 'PRINTER', 'device_type': 'toner new'},
    'toner (used)': {   'category': 'PRINTER', 'device_type': 'toner'},
    'toner / ink cartridge': {   'category': 'PRINTER',
                                 'device_type': 'toner new'},
    'toner/ink cartridge': {   'category': 'PRINTER', 'device_type': 'toner new'},
    'tower computer': {   'category': 'COMPUTER', 'device_type': 'tower'},
    'tv': {   'category': 'VIDEO', 'device_type': 'tv'},
    'tv  - plasma': {   'category': 'VIDEO', 'device_type': 'tv plasma'},
    'tv (crt)': {   'category': 'VIDEO', 'device_type': 'crt'},
    'tv (dlp)': {   'category': 'VIDEO', 'device_type': 'tv'},
    'tv (lcd)': {   'category': 'VIDEO', 'device_type': 'lcd'},
    'tv (led)': {   'category': 'VIDEO', 'device_type': 'led'},
    'tv (plasma)': {   'category': 'VIDEO', 'device_type': 'tv plasma'},
    'tv - crt': {   'category': 'VIDEO', 'device_type': 'tv crt'},
    'tv - lcd': {   'category': 'VIDEO', 'device_type': 'tv lcd'},
    'tv - led': {   'category': 'VIDEO', 'device_type': 'tv led'},
    'tv - plasma': {   'category': 'VIDEO', 'device_type': 'tv plasma'},
    'tv - rear projection': {   'category': 'VIDEO',
                                'device_type': 'tv projection'},
    'tv stand': {   'category': 'VIDEO',
                    'device_type': 'stand/mount/frame enclosure'},
    'ups': {   'category': 'POWER_SUPPLY', 'device_type': 'ups'},
    'usb drive': {   'category': 'STORAGE', 'device_type': 'usb'},
    'various': {   'category': 'ASSORTED', 'device_type': 'various'},
    'video card': {   'category': 'COMPONENT', 'device_type': 'video card'},
    'webcam': {   'category': 'PERIPHERAL', 'device_type': 'webcam'},
    'wireless adapter - usb': {   'category': 'PERIPHERAL',
                                  'device_type': 'wifi adapter'},
    'workstation': {   'category': 'COMPUTER', 'device_type': 'desktop'}}