# Drivers for kernel 5.4.268-966.8.4.okapi.pine.1 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  If your TV runs this kernel, please try one and report back: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

LG's LM21A-family chips have no USB network drivers at all, not even `usbnet`.  Realtek's driver doesn't need `usbnet`, so `r8152_oot` and `r8152` work on their own.  Drivers that do need it (ASIX AX88179, Davicom, Aquantia) come with this kernel's own `usbnet.ko`, which LG-USB-2-ETH0 loads first.  The older ASIX `asix` driver and `lan78xx` also need the kernel's PHY library, which it leaves out too, so they aren't here.

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2023 LG LCD TVs with the LM21ANN chip (UR73 to UR81 series), on webOS 24 firmware 23.25.  Only that chip runs this kernel name.
- **Kernel source:** LG Open Source package "webOS 24 LMANN_ReNew" (for the 50UR80006LJ), `code/BSP_open_source_okapi_v4_1_part.tar.gz`, kernel 5.4.268 with LG's `-966` patches.  Its config differs from the TV's only in compiler settings.
- **Config:** the one built into the TV's own kernel, from LG's firmware for that kernel
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `eceadb6d19630fa9682a7766817a8c8432e9656c14a2c696e7d4b881b2c4328c`
- **Checks:** `vermagic=5.4.268-966.8.4.okapi.pine.1 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 130 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `77617409da691d863895b7d1bb83020aa1147cefc213ccf713338028fdd415a6`
- **Checks:** `vermagic=5.4.268-966.8.4.okapi.pine.1 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 108 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## usbnet.ko

- **Driver:** the kernel's own `usbnet` (drivers/net/usb/usbnet.c), the core the drivers below are built on.  This kernel leaves it out, so LG-USB-2-ETH0 loads this one first, checked against its pinned SHA-256, before any of them
- **Adapters:** none by itself
- **SHA-256:** `04a8ed503133e48008fe6885793473762f1e5b4dd5aeb68fe7d3f6137315ecfd`
- **Checks:** `vermagic=5.4.268-966.8.4.okapi.pine.1 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 103 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a`, built on the `usbnet` above
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `1416ca98f96b12b66f3c9b9ec857a8e687a7becab8219557891f700205b879f2`
- **Checks:** `vermagic=5.4.268-966.8.4.okapi.pine.1 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and of the 46 symbols it imports, 21 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** the kernel's own `dm9601`, built on the `usbnet` above
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `cd1f50be9afdf5ae1637ec17b6430f30e3927cb971c44052b92445fe7783baae`
- **Checks:** `vermagic=5.4.268-966.8.4.okapi.pine.1 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and of the 42 symbols it imports, 21 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## aqc111.ko

- **Driver:** the kernel's own `aqc111`, built on the `usbnet` above
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `6ad4beb8d6131bcaf80c5b3d0b5bc6e7c6b3c7aa0be4cb0b08f358d22f98acff`
- **Checks:** `vermagic=5.4.268-966.8.4.okapi.pine.1 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and of the 48 symbols it imports, 18 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
