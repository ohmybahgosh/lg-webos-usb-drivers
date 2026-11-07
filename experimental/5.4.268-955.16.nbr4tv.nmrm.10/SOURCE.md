# Drivers for kernel 5.4.268-955.16.nbr4tv.nmrm.10 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  If your TV runs this kernel, please try one and report back: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

LG's LM21A-family chips have no USB network drivers at all, not even `usbnet`.  Realtek's driver doesn't need `usbnet`, so `r8152_oot` and `r8152` work on their own.  Drivers that do need it (ASIX AX88179, Davicom, Aquantia) come with this kernel's own `usbnet.ko`, which LG-USB-2-ETH0 loads first.  The older ASIX `asix` driver and `lan78xx` also need the kernel's PHY library, which it leaves out too, so they aren't here.

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** LG's StanbyME (27ART10AKPL, the 2022 rolling-stand screen) with the LM21UT chip, on webOS 24 firmware 23.22.  Only that chip runs this kernel name.
- **Kernel source:** LG Open Source package "webOS 24 LMANN_ReNew", which LG lists for the 27ART10AKPL too, `code/BSP_open_source_okapi_v4_1_part.tar.gz`, kernel 5.4.268.  That source is LG's `-966` revision and this kernel is `-955.16`, so it's a close match rather than the exact source.  Its config differs from the TV's only in compiler settings and `MTK_DRM_FOR_WEBOS`, a display option no kernel header uses, and every symbol each module uses is in the TV's own kernel.
- **Config:** the one built into the TV's own kernel, from LG's firmware for that kernel
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `fc9679dea933b32addb7c13d581a7cde6b3d176dcb5c4f7e13762d5b15d14cab`
- **Checks:** `vermagic=5.4.268-955.16.nbr4tv.nmrm.10 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 130 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `18500334964272a9e59c34718890a765502c6f1b7bfdd578ad6aa1fb88cdb370`
- **Checks:** `vermagic=5.4.268-955.16.nbr4tv.nmrm.10 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 108 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## usbnet.ko

- **Driver:** the kernel's own `usbnet` (drivers/net/usb/usbnet.c), the core the drivers below are built on.  This kernel leaves it out, so LG-USB-2-ETH0 loads this one first, checked against its pinned SHA-256, before any of them
- **Adapters:** none by itself
- **SHA-256:** `377d40c26e4fdac87ecb1fa8d3bd7bab002f571691f0e5de45e52758dda76c4d`
- **Checks:** `vermagic=5.4.268-955.16.nbr4tv.nmrm.10 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 103 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a`, built on the `usbnet` above
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `fba0553635804a3b018049db64a31407f9c843428d82ef8a8c13befb8f2dab9c`
- **Checks:** `vermagic=5.4.268-955.16.nbr4tv.nmrm.10 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and of the 46 symbols it imports, 21 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** the kernel's own `dm9601`, built on the `usbnet` above
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `7abbe41e5a84d2e7225dc00c6ae0e049842e436f407324caaf53ab666a335d14`
- **Checks:** `vermagic=5.4.268-955.16.nbr4tv.nmrm.10 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and of the 42 symbols it imports, 21 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## aqc111.ko

- **Driver:** the kernel's own `aqc111`, built on the `usbnet` above
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `f0f7fd57031297f28e578e8cbae1e38617a7d77e4d68080101a70e1e30d72a23`
- **Checks:** `vermagic=5.4.268-955.16.nbr4tv.nmrm.10 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and of the 48 symbols it imports, 18 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
