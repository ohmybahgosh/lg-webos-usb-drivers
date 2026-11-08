# Drivers for kernel 4.4.3-78.drd4tv.2 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2017 LJ HD and Full HD LCDs with the M2R chip (like the 32LJ590U and 43LJ614V), on firmware 05.80.35, 06.10.55 and 06.10.60 (webOS 3.5).  The kernel has no USB network driver at all, not even `usbnet`, so the ASIX and Davicom drivers come with a `usbnet.ko` the script loads first.  There's no Microchip LAN78xx build: this kernel leaves out the PHY library it needs.  webOS 3.5 TVs can be rooted with [RootMyTV](https://rootmy.tv) on older firmware, or [faultmanager-autoroot](https://github.com/throwaway96/faultmanager-autoroot)
- **Kernel source:** LG Open Source package "webOS 3.5 DMR" (for 43LJ614V-ZA and similar), `DMR-r3185/open_source_MR/GPL2.0/kernel_DMR_MRM.tar.gz` (Linux 4.4.3), with `kdriver_DMR_MRM.tar.gz` unpacked into `drivers`.  One change for today's compilers: `-fno-PIE` added to the Makefile's C flags, as later 4.4 kernels do
- **Config:** the firmware's kernel has no built-in config, so this is `arch/arm/configs/m2r_defconfig` from the same LG source, the only config it ships for this chip.  The TV's own modules (16 of them, like `btmtk_usb.ko`) have the same vermagic, and every symbol the drivers import is exported by the TV's kernel image, read from its firmware
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c) from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `0e29709c60bf63e1aca86cff204390ba271ef9bae6ca766cc373a5fe5034382f`
- **Checks:** `vermagic=4.4.3-78.drd4tv.2 SMP preempt mod_unload ARMv7`.  The kernel has MODVERSIONS and module signing off,, and all 96 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4.  The same source as the other 4.4 builds
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156 (2.5 gigabit).  For RTL8152 and RTL8153, `test-driver` tries the kernel's own `r8152.ko` above first
- **SHA-256:** `98972012d355256d764418d9c54f3b3617a0fe29f52174b82487763c1c7cb939`
- **Checks:** `vermagic=4.4.3-78.drd4tv.2 SMP preempt mod_unload ARMv7`,, and all 130 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## usbnet.ko

- **Driver:** `drivers/net/usb/usbnet.c` from the same LG kernel source, built as a module: the core the ASIX and Davicom drivers need, which this kernel leaves out.  The script loads it first
- **Adapters:** none on its own
- **SHA-256:** `911cdde2d5f1924f8c9c456981cd40a8be45b9f8ce960a1119eba543edef82cf`
- **Checks:** `vermagic=4.4.3-78.drd4tv.2 SMP preempt mod_unload ARMv7`,, and all 101 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** `drivers/net/usb/ax88179_178a.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** ASIX AX88179 and AX88178A (gigabit)
- **SHA-256:** `478c08e5891cd2ae54c18f41e136c7924a8347bed8af65fa9968925b1f6fce48`
- **Checks:** `vermagic=4.4.3-78.drd4tv.2 SMP preempt mod_unload ARMv7`,, and all 48 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `65b67b9efe9a2c5afb5e69a21596c2d970335e59db0cc040edac28d5ea7a372c`
- **Checks:** `vermagic=4.4.3-78.drd4tv.2 SMP preempt mod_unload ARMv7`,, and all 44 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the one above (not at all).
