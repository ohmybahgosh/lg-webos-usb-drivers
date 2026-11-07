# Drivers for kernel 5.4.96-934.16.1.mirima.1 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  If your TV runs this kernel, please try one and report back: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

LG's LM21A-family chips have no USB network drivers at all, not even `usbnet`.  Realtek's driver doesn't need `usbnet`, so `r8152_oot` and `r8152` work on their own.  Drivers that do need it (ASIX AX88179, Davicom, Aquantia) come with this kernel's own `usbnet.ko`, which LG-USB-2-ETH0 loads first.  The older ASIX `asix` driver and `lan78xx` also need the kernel's PHY library, which it leaves out too, so they aren't here.

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

## usbnet.ko

- **Driver:** the kernel's own `usbnet` (drivers/net/usb/usbnet.c), the core the drivers below are built on.  This kernel leaves it out, so LG-USB-2-ETH0 loads this one first, checked against its pinned SHA-256, before any of them
- **Adapters:** none by itself
- **SHA-256:** `a077664216fe73332e924f35238456cf1ead89cd240306d4c2a8867046b177e6`
- **Checks:** `vermagic=5.4.96-934.16.1.mirima.1 SMP preempt mod_unload aarch64`, and all 103 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a`, built on the `usbnet` above
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `8cf34aaa2f8ac689f7ad624e2371cb2d86217cc5c47486db11160b17229df4dc`
- **Checks:** `vermagic=5.4.96-934.16.1.mirima.1 SMP preempt mod_unload aarch64`, and of the 46 symbols it imports, 21 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** the kernel's own `dm9601`, built on the `usbnet` above
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `952d96d5def983324326c5cc4af4966dc4fa245c6de3a65d52e4ef900d5b9818`
- **Checks:** `vermagic=5.4.96-934.16.1.mirima.1 SMP preempt mod_unload aarch64`, and of the 42 symbols it imports, 21 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## aqc111.ko

- **Driver:** the kernel's own `aqc111`, built on the `usbnet` above
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `73b4376746d66a6d3614c5b05e836616b78c5bba19f315c6dce98e4affc0a7dd`
- **Checks:** `vermagic=5.4.96-934.16.1.mirima.1 SMP preempt mod_unload aarch64`, and of the 48 symbols it imports, 18 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
