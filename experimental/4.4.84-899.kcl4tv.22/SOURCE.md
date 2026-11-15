# Drivers for kernel 4.4.84-899.kcl4tv.22 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  If your TV runs this kernel, please try one and report back: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

LG's LM21A-family chips have no USB network drivers at all, not even `usbnet`.  Realtek's driver doesn't need `usbnet`, so `r8152_oot` and `r8152` work on their own.  Drivers that do need it (ASIX AX88179, Davicom) come with this kernel's own `usbnet.ko`, which LG-USB-2-ETH0 loads first.  The older ASIX `asix` driver and `lan78xx` also need the kernel's PHY library, which it leaves out too, and Aquantia's `aqc111` is newer than kernel 4.4, so they aren't here.

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2021 LG LCD TVs with the LM21A and LM21U chips (UP and NANO models, and the OLED A1 and B1 sold in Japan), on webOS 6 firmware 03.60.96 from November 2026.  Both chips run this kernel name with the same config, so one build serves both.
- **Kernel source:** LG Open Source package "webOS 6.0 LMUA_1.0" (for the 50UP8000PUA), `common/bsp_open3.tar.gz`, kernel 4.4.84 with LG's `-899` patches.  That source is older than the TV's kernel: its Kconfig turns off `CPU_SW_DOMAIN_PAN` on MStar platforms, while the TV's kernel has it on (and exports `arm_copy_from_user`, which only exists with it).  So that one dependency was dropped to build with the TV's value.  Otherwise the config differs from the TV's only in `MFB_GC`, a framebuffer option no kernel header uses.  The TV's config is the same as for `4.4.84-899.kcl4tv.19`.
- **Config:** the one built into the TV's own kernel, from LG's firmware for that kernel
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `8f501b4f463d8dce2a6e99fc8d825062361e9924fde41ca544d4621b76fb2f56`
- **Checks:** `vermagic=4.4.84-899.kcl4tv.22 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and all 129 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `b42d7814fadde20ffc003daf1524f639054166d9556e4cfe3c94485c91cf23d0`
- **Checks:** `vermagic=4.4.84-899.kcl4tv.22 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and all 94 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## usbnet.ko

- **Driver:** the kernel's own `usbnet` (drivers/net/usb/usbnet.c), the core the drivers below are built on.  This kernel leaves it out, so LG-USB-2-ETH0 loads this one first, checked against its pinned SHA-256, before any of them
- **Adapters:** none by itself
- **SHA-256:** `58bd91b60e69458a811e5812b38a5e816faee8f4bfdcdb4be779c6e70d4494bc`
- **Checks:** `vermagic=4.4.84-899.kcl4tv.22 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and all 99 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a`, built on the `usbnet` above
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `48b58ea22f2b60397469ba56162b513891a762d91d17aca6da61c70eada28e85`
- **Checks:** `vermagic=4.4.84-899.kcl4tv.22 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and of the 47 symbols it imports, 20 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** the kernel's own `dm9601`, built on the `usbnet` above
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `38d824f4281dab8966b86406fdab116be768b31efefae8217fbc0207afcda1b7`
- **Checks:** `vermagic=4.4.84-899.kcl4tv.22 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and of the 43 symbols it imports, 20 come from the `usbnet.ko` above and the rest are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
