# Drivers for kernel 4.4.84-612.jcl4tv.40 on the K6Lp chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build), the way [OCT0PUSCRIME](https://github.com/OCT0PUSCRIME/lg-webos-ax88179-driver) built his webOS 5 ASIX driver for this kernel
- **TVs:** the 2020 UN7300 (55UN7300PUF) on webOS 5, where OCT0PUSCRIME's ASIX driver works ([discussion #3](https://github.com/ohmybahgosh/LG-USB-2-ETH0/discussions/3)).  The kernel has no Realtek driver
- **Kernel source:** LG Open Source package "webOS 5.0 JKHP 2.0" (for 55UN7310 and similar), `common/kernel-1.0.0-612.21.tar.gz` (612.21.6.jardine.3)
- **Config:** this kernel's firmware isn't in the archive, so there's no TV config to read.  Like OCT0PUSCRIME's working ASIX module, these are built with the source's own K6Lp config and his version suffix, and checked against a full build of it: every symbol they import is exported
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `90bb0e88c56b405e730af673c9309a215eaea6ce4ce888fbd3c71285f9e47717`
- **Checks:** `vermagic=4.4.84-612.jcl4tv.40 SMP preempt mod_unload ARMv7`, the same as OCT0PUSCRIME's working module.  The kernel has MODVERSIONS and module signing off, and all 95 symbols it imports are exported.  USB struct offsets: not checked, so it needs a tester.

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4 (three small back-ports, and no 64-bit ioctl path on this 32-bit kernel).  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156 (2.5 gigabit).  For RTL8152 and RTL8153, `test-driver` tries the kernel's own `r8152.ko` above first
- **SHA-256:** `8df6d54ced5d6486449310efe16dfa5e89ad28cbd6d1e479c442b15174d665d3`
- **Checks:** `vermagic=4.4.84-612.jcl4tv.40 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and all 134 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `ac05a0fbce0e34836879125214d967dbf5b4cddd1c686e16dbdf6a7b369fb247`
- **Checks:** `vermagic=4.4.84-612.jcl4tv.40 SMP preempt mod_unload ARMv7`, and all 45 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `7b62bcea300537121ce8a6c8f12d547e27841eb80d81876eb45e9e43e105aef7`
- **Checks:** `vermagic=4.4.84-612.jcl4tv.40 SMP preempt mod_unload ARMv7`, and all 119 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the source's (nothing).
