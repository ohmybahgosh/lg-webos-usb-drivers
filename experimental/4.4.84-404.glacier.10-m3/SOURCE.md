# Drivers for kernel 4.4.84-404.glacier.10 on the M3 chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2018 LK61 and other small LK HD LCDs with the M3 chip, on firmware 05.30.11 to 05.50.70 (webOS 4.0).  The kernel has no USB network driver at all, not even `usbnet`, so the ASIX and Davicom drivers come with a `usbnet.ko` the script loads first.  There's no Microchip LAN78xx build: this kernel leaves out the PHY library it needs.  webOS 4.0 TVs can be rooted with [faultmanager-autoroot](https://github.com/throwaway96/faultmanager-autoroot)
- **Kernel source:** LG Open Source package "webOS 4.0 GM" (for 43LK6100PLB and similar), `GM-r3232/kernel_gm_MR_5e35927.tgz`: the 4.4.84 kernel for the M3 chip, revision 404
- **Config:** the firmware's kernel has no built-in config, so this is the release `.config` that ships in LG's source tree for the same kernel revision (404).  The TV's own modules have the same vermagic, and every symbol the drivers import is exported by the TV's kernel image, read from its firmware
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `c775213b1db67281e2ea09c9b87b1d0cd5da7835169f2760eea307981d35864f`
- **Checks:** `vermagic=4.4.84-404.glacier.10 SMP preempt mod_unload ARMv7`.  The kernel has MODVERSIONS and module signing off,, and all 96 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4.  The same source as the other 4.4 builds
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156 (2.5 gigabit).  For RTL8152 and RTL8153, `test-driver` tries the kernel's own `r8152.ko` above first
- **SHA-256:** `a90c12ad4046093f55341891b1df75da0c142fb4ecd77aa9d2d0efb258aceee7`
- **Checks:** `vermagic=4.4.84-404.glacier.10 SMP preempt mod_unload ARMv7`,, and all 130 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## usbnet.ko

- **Driver:** `drivers/net/usb/usbnet.c` from the same LG kernel source, built as a module: the core the ASIX and Davicom drivers need, which this kernel leaves out.  The script loads it first
- **Adapters:** none on its own
- **SHA-256:** `d66e396794044fd673925ce0516c0b14e8fdd15ef9ffe2b66e5fef05cf72e99c`
- **Checks:** `vermagic=4.4.84-404.glacier.10 SMP preempt mod_unload ARMv7`,, and all 101 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** `drivers/net/usb/ax88179_178a.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** ASIX AX88179 and AX88178A (gigabit)
- **SHA-256:** `1f1e36c8a86cea8ba2dbbb01bb5e57c6766cd8ea3abfb59369a62575cc856219`
- **Checks:** `vermagic=4.4.84-404.glacier.10 SMP preempt mod_unload ARMv7`,, and all 48 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `3b3181fab35cd8a441eb598f28a328dec43821c406249adf705b9d587b973a1d`
- **Checks:** `vermagic=4.4.84-404.glacier.10 SMP preempt mod_unload ARMv7`,, and all 44 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from LG's release config (not at all).
