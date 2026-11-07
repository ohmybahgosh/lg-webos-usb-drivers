# Drivers for kernel 4.4.84-899.kcl4tv.19 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  If your TV runs this kernel, please try one and report back: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

LG's LM21A-family chips have no USB network drivers at all, not even `usbnet`.  Realtek's driver doesn't need `usbnet`, so `r8152_oot` and `r8152` work on their own.  Drivers that do need it (ASIX AX88179, Davicom) come with this kernel's own `usbnet.ko`, which LG-USB-2-ETH0 loads first.  The older ASIX `asix` driver and `lan78xx` also need the kernel's PHY library, which it leaves out too, and Aquantia's `aqc111` is newer than kernel 4.4, so they aren't here.

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2021 LG LCD TVs with the LM21U chip, on webOS 6 firmware 03.41.  Only that chip runs this kernel name.
- **Kernel source:** LG Open Source package "webOS 6.0 LMUA_1.0" (for the 50UP8000PUA), `common/bsp_open3.tar.gz`, kernel 4.4.84 with LG's `-899` patches.  That source is older than the TV's kernel: its Kconfig turns off `CPU_SW_DOMAIN_PAN` on MStar platforms, while the TV's kernel has it on (and exports `arm_copy_from_user`, which only exists with it).  So that one dependency was dropped to build with the TV's value.  Otherwise the config differs from the TV's only in `MFB_GC`, a framebuffer option no kernel header uses.
- **Config:** the one built into the TV's own kernel, from LG's firmware for that kernel
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `3aa2dcf4715215506c4074b5a818e102d3323a1c03b41d8c0042465cd9600afd`
- **Checks:** `vermagic=4.4.84-899.kcl4tv.19 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and all 129 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `1f4c77b119d249c4d8df9c05ead4c33a4fcac38dee8569eb6353d079163adc3f`
- **Checks:** `vermagic=4.4.84-899.kcl4tv.19 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and all 94 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## usbnet.ko

- **Driver:** the kernel's own `usbnet` (drivers/net/usb/usbnet.c), the core the drivers below are built on.  This kernel leaves it out, so LG-USB-2-ETH0 loads this one first, checked against its pinned SHA-256, before any of them
- **Adapters:** none by itself
- **SHA-256:** `8503c66e503726533ed39814ce81aa8f54a54836838c1843a1f9aa50572f3eaf`
- **Checks:** `vermagic=4.4.84-899.kcl4tv.19 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and all 99 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a`, built on the `usbnet` above
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `90427709e3b3c0768f1efe0f6b9035dfa8c678d5d9037cc6b9636fd250bd0aeb`
- **Checks:** `vermagic=4.4.84-899.kcl4tv.19 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and of the 47 symbols it imports, 20 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** the kernel's own `dm9601`, built on the `usbnet` above
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `bf7c15f0a0692e84fe1f4c88b473995240b556dc60c00d6d9093a84c546e16d1`
- **Checks:** `vermagic=4.4.84-899.kcl4tv.19 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and of the 43 symbols it imports, 20 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
