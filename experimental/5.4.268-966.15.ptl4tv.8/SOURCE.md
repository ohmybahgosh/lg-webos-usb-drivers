# Drivers for kernel 5.4.268-966.15.ptl4tv.8 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  If your TV runs this kernel, please try one and report back: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

LG's LM21A-family chips have no USB network drivers at all, not even `usbnet`.  Realtek's driver doesn't need `usbnet`, so `r8152_oot` and `r8152` work on their own.  Drivers that do need it (ASIX AX88179, Davicom, Aquantia) come with this kernel's own `usbnet.ko`, which LG-USB-2-ETH0 loads first.  The older ASIX `asix` driver and `lan78xx` also need the kernel's PHY library, which it leaves out too, so they aren't here.

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2023 LG LCD TVs with the LM21ANN chip (UR73 to UR81 series), on webOS 25 firmware 33.22.  Only that chip runs this kernel name.
- **Kernel source:** LG Open Source package "webOS25 WA_ReNew" (for the 50UR80006LJ), `BSP_open_source_PINE25/kernel`, kernel 5.4.268 with LG's `-966` patches.  Its config differs from the TV's only in compiler settings.
- **Config:** the one built into the TV's own kernel, from LG's firmware for that kernel
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `82b96ceafa0c85576b16b50ba29723dffae808cbd9cc58b1cd4beef97ffae358`
- **Checks:** `vermagic=5.4.268-966.15.ptl4tv.8 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 130 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `9ca46a97bd884a58d46dd069bd44b4ffa3bc32cd68b864600fc77d2bc210a4e8`
- **Checks:** `vermagic=5.4.268-966.15.ptl4tv.8 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 108 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## usbnet.ko

- **Driver:** the kernel's own `usbnet` (drivers/net/usb/usbnet.c), the core the drivers below are built on.  This kernel leaves it out, so LG-USB-2-ETH0 loads this one first, checked against its pinned SHA-256, before any of them
- **Adapters:** none by itself
- **SHA-256:** `6c03c12c83626aa08537e9e4c1ebeef272bb4f2beafc839500db18be15b764f2`
- **Checks:** `vermagic=5.4.268-966.15.ptl4tv.8 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 103 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a`, built on the `usbnet` above
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `c63941580f9c983ccb792e48f9c56cfd23c02106401e00b25d35eed336d5b2a8`
- **Checks:** `vermagic=5.4.268-966.15.ptl4tv.8 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and of the 46 symbols it imports, 21 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** the kernel's own `dm9601`, built on the `usbnet` above
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `f5b592e7fc77efa8ada66f93ac78be35a54bc4ffc481b73eb6a5e3fc5c839f42`
- **Checks:** `vermagic=5.4.268-966.15.ptl4tv.8 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and of the 42 symbols it imports, 21 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## aqc111.ko

- **Driver:** the kernel's own `aqc111`, built on the `usbnet` above
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `1bc3cf524723f6445578ed52288a1b83af3b094b4030f77b33f6e03e4ed29f67`
- **Checks:** `vermagic=5.4.268-966.15.ptl4tv.8 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and of the 48 symbols it imports, 18 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
