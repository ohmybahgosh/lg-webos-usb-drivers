# Drivers for kernel 5.4.96-934.16.1.mirima.1 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  If your TV runs this kernel, please try one and report back: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

LG's LM21A-family chips have no USB network drivers at all, not even `usbnet`.  Realtek's driver doesn't need `usbnet`, so these two work on their own.  Drivers that do need it (ASIX, `cdc_ncm`, `cdc_ether`) aren't here yet.

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2022 LG LCD TVs with the LM21AN chip (UQ70 to UQ90 series, like the 75UQ9000PUD and 70UQ8000AUB), on firmware 04.54 (webOS 22).  Only that chip runs this kernel name.
- **Kernel source:** LG Open Source package "webOS 22 LMAN 12.0" (for the 50UQ80006LB), `soc/BSP_open_source_maria.tar.gz`, kernel 5.4.96 with LG's `-934.mlt4tv` patches.  Its config differs from the TV's only in compiler settings.
- **Config:** the one built into the TV's own kernel, from LG's firmware for that kernel
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `fc28abb1bc27b03fd332c384b2e037bd7f897d5779fe4976c02decf593f9882a`
- **Checks:** `vermagic=5.4.96-934.16.1.mirima.1 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 130 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `b7d038d7ffd13ae02ce09ce1f0fe8225c63b13cbab33df1d3e7980dd9ec8ec39`
- **Checks:** `vermagic=5.4.96-934.16.1.mirima.1 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 108 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
