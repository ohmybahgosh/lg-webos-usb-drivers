# Drivers for kernel 4.4.84-899.19.koli.1 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  If your TV runs this kernel, please try one and report back: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

LG's LM21A-family chips have no USB network drivers at all, not even `usbnet`.  Realtek's driver doesn't need `usbnet`, so `r8152_oot` and `r8152` work on their own.  Drivers that do need it (ASIX AX88179, Davicom) come with this kernel's own `usbnet.ko`, which LG-USB-2-ETH0 loads first.  The older ASIX `asix` driver and `lan78xx` also need the kernel's PHY library, which it leaves out too, and Aquantia's `aqc111` is newer than kernel 4.4, so they aren't here.

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2021 LG LCD TVs with the LM21A chip (UP and NANO models), on webOS 6 firmware 03.53.  Only that chip runs this kernel name.
- **Kernel source:** LG Open Source package "webOS 6.0 LMUA_1.0" (for the 50UP8000PUA), `common/bsp_open3.tar.gz`, kernel 4.4.84 with LG's `-899` patches.  That source is older than the TV's kernel: its Kconfig turns off `CPU_SW_DOMAIN_PAN` on MStar platforms, while the TV's kernel has it on (and exports `arm_copy_from_user`, which only exists with it).  So that one dependency was dropped to build with the TV's value.  Otherwise the config differs from the TV's only in `MFB_GC`, a framebuffer option no kernel header uses.
- **Config:** the one built into the TV's own kernel, from LG's firmware for that kernel
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `e863bc0c1ae38da9598788f374346e92c1bdea40d725656ebd5e2c12def78f3d`
- **Checks:** `vermagic=4.4.84-899.19.koli.1 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and all 129 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `b96d7c77b32ef351f7aac682379bef30fa4d9f116fb5e3cde90f31d5bb62d94e`
- **Checks:** `vermagic=4.4.84-899.19.koli.1 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and all 94 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## usbnet.ko

- **Driver:** the kernel's own `usbnet` (drivers/net/usb/usbnet.c), the core the drivers below are built on.  This kernel leaves it out, so LG-USB-2-ETH0 loads this one first, checked against its pinned SHA-256, before any of them
- **Adapters:** none by itself
- **SHA-256:** `9674ec86e7e586bcd7dcd911c94d99afbc92293a954009e2cfcaa31e2e265817`
- **Checks:** `vermagic=4.4.84-899.19.koli.1 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and all 99 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a`, built on the `usbnet` above
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `316a5b93461285f2b77cd776af86046a22a70ae3aedb01eec034550ad8dcece5`
- **Checks:** `vermagic=4.4.84-899.19.koli.1 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and of the 47 symbols it imports, 20 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** the kernel's own `dm9601`, built on the `usbnet` above
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `33b082bcd5c20961200939ffcf09492f4211bd30d0dda2fd7871f8e12d3f3106`
- **Checks:** `vermagic=4.4.84-899.19.koli.1 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and of the 43 symbols it imports, 20 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
