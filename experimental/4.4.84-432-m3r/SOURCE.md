# Drivers for kernel 4.4.84-432 on the M3R chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2019 LM63 and other small LM HD LCDs with the M3R chip, on the older firmware 04.72.20 and 05.00.03 (webOS 4.5).  The kernel has no USB network driver at all, not even `usbnet`, so the ASIX and Davicom drivers come with a `usbnet.ko` the script loads first.  There's no Microchip LAN78xx build: this kernel leaves out the PHY library it needs.  webOS 4.5 TVs can be rooted with [faultmanager-autoroot](https://github.com/throwaway96/faultmanager-autoroot)
- **Kernel source:** LG Open Source package "webOS 4.5 IMR_5.0" (for 43LM6300PLA and similar), `IMR-r3249/common/gpl_m3r_MR_kernel_v1.zip`: the 4.4.84 kernel for the M3R chip
- **Config:** the TV's own kernel config, read from its firmware.  The build config matches it exactly
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `dcd0600fee1667a4d8c0262b3bf763afe5796657ad45ee0243b2d6ff4c17cfef`
- **Checks:** `vermagic=4.4.84-432 SMP preempt mod_unload ARMv7`.  The kernel has MODVERSIONS and module signing off,, and all 96 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4.  The same source as the other 4.4 builds
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156 (2.5 gigabit).  For RTL8152 and RTL8153, `test-driver` tries the kernel's own `r8152.ko` above first
- **SHA-256:** `6d066211ac18ed7106395b009ae093e70eb731811262410ab632716e39a659fc`
- **Checks:** `vermagic=4.4.84-432 SMP preempt mod_unload ARMv7`,, and all 130 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## usbnet.ko

- **Driver:** `drivers/net/usb/usbnet.c` from the same LG kernel source, built as a module: the core the ASIX and Davicom drivers need, which this kernel leaves out.  The script loads it first
- **Adapters:** none on its own
- **SHA-256:** `491bd1cb111c13930631ebf70d69cbd2cfeec29f9e69fdeb71bf4640f4affbad`
- **Checks:** `vermagic=4.4.84-432 SMP preempt mod_unload ARMv7`,, and all 101 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** `drivers/net/usb/ax88179_178a.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** ASIX AX88179 and AX88178A (gigabit)
- **SHA-256:** `79c377739f891c7a60b3998524de633e7767460ed78fc1e601b3626a24fb870e`
- **Checks:** `vermagic=4.4.84-432 SMP preempt mod_unload ARMv7`,, and all 48 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `b1bbd20f24e3fd29b9c4c05b8a6f0e9672e39beba9ffb52b480166f733f914d9`
- **Checks:** `vermagic=4.4.84-432 SMP preempt mod_unload ARMv7`,, and all 44 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's (not at all).
