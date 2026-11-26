# Test build for LG-USB-2-ETH0 issue #62 (not offered by the script)

A one-off test for [issue #62](https://github.com/ohmybahgosh/LG-USB-2-ETH0/issues/62): download speed with an AX88179 on a TV's USB 2.0 port.  The script doesn't offer it.

- **Kernel:** `4.4.84-612.40.jimna.1`, K6Hp chip (2020 TVs on webOS 5), built the same way as [the regular one](../../4.4.84-612.40.jimna.1-k6hp), with Linux's 2022 RX fix
- **Change:** [`usb2-params.py`](usb2-params.py) adds two module parameters for the adapter's receive settings on USB 2.0, changeable at `/sys/module/ax88179_178a/parameters/` and used from the next link change (unplug and replug the cable):
  - `hs_size`: the bulk-in size.  Each USB transfer is (hs_size + 2) KB, and usbnet keeps about 89 KB of them queued, so a smaller size means more transfers in flight.  Stock: 22 at gigabit, 24 at 100M
  - `hs_timer`: the adapter's aggregation timer.  Stock: 0x320 (800) at gigabit
  - `-1` (the default) keeps the stock value, and the kernel log says which ones are in use (`USB 2.0 bulk-in: ...`)
- **SHA-256:** `5a11026acba8f5062c1f6dbe39cbc1f9c6322e3ad2a4c1af0a77321c20a6acd5`
- **Checks:** `vermagic=4.4.84-612.40.jimna.1 SMP preempt mod_unload ARMv7`, and all 49 symbols it imports are exported by the TV's kernel
- **License:** GPL-2.0, like the kernel it's built from
