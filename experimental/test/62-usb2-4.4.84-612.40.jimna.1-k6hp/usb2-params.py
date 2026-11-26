#!/usr/bin/env python3
"""Test build for #62: module parameters for the USB 2.0 receive settings.
hs_size: the bulk-in size the adapter uses on USB 2.0 (the stock value is 22
at gigabit, 24 at 100M); the transfer is (hs_size + 2) KB, and usbnet keeps
about 89 KB of them queued, so a smaller size means more transfers in flight.
hs_timer: the adapter's aggregation timer on USB 2.0 (stock 0x320 at gigabit).
-1 keeps the stock value."""
import sys
p = sys.argv[1]
s = open(p).read()
a = '#include <linux/mdio.h>\n'
assert s.count(a) == 1
s = s.replace(a, a + '''
static int hs_size = -1;
module_param(hs_size, int, 0644);
MODULE_PARM_DESC(hs_size, "USB 2.0 bulk-in size, transfer is (hs_size + 2) KB (-1: stock)");
static int hs_timer = -1;
module_param(hs_timer, int, 0644);
MODULE_PARM_DESC(hs_timer, "USB 2.0 bulk-in aggregation timer (-1: stock)");
''')
a = '''	ax88179_write_cmd(dev, AX_ACCESS_MAC, AX_RX_BULKIN_QCTRL, 5, 5, tmp);

	dev->rx_urb_size = (1024 * (tmp[3] + 2));
'''
assert s.count(a) == 1
s = s.replace(a, '''	if ((link_sts & AX_USB_HS) && !(link_sts & AX_USB_SS)) {
		if (hs_size >= 0 && hs_size <= 0x30)
			tmp[3] = hs_size;
		if (hs_timer >= 0 && hs_timer <= 0xffff) {
			tmp[1] = hs_timer & 0xff;
			tmp[2] = (hs_timer >> 8) & 0xff;
		}
		netdev_info(dev->net, "USB 2.0 bulk-in: size %u (%u KB transfers), timer 0x%x\\n",
			    tmp[3], tmp[3] + 2, tmp[1] | (tmp[2] << 8));
	}
''' + a)
open(p, 'w').write(s)
print('usb2 params added')
