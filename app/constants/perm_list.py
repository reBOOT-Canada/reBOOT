FRONTLINE = [
    'add_donation',
    'change_donation',
    'delete_donation',
    'view_donation',
    'add_donor',
    'change_donor',
    'delete_donor',
    'view_donor',
    'add_item',
    'change_item',
    'delete_item',
    'view_item',
    'add_itemdevice',
    'change_itemdevice',
    'delete_itemdevice',
    'add_itemdevicetype',
    'change_itemdevicetype',
    'delete_itemdevicetype',
]

MANAGEMENT = FRONTLINE + [
    'can_import_historical',
    'can_import_third_party',
    'can_import_website',
    'can_export_data',
    'generate_tax_receipt',
    'update_status_item',
    'update_value_item',
]