# Drivers for kernel 4.4.84-417.gld4tv.7 on the K5LP chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2019 UM7000 to UM7800 LCDs and LG's 2019 projectors with the K5LP chip, on firmware 05.00.02 to 05.00.15 (webOS 4.5).  The kernel has ASIX's older AX88772 driver and usbnet built in, but no Realtek, AX88179, Davicom or Microchip driver.  webOS 4.5 TVs can be rooted with [faultmanager-autoroot](https://github.com/throwaway96/faultmanager-autoroot)
- **Kernel source:** LG Open Source package "webOS 4.5 IKLP_4.0" (for 43UM7300PPA and similar), `IKLP-r3247/common/RTK_Kernel_linux.zip`: Realtek's 4.4.84 kernel for the K5LP chip
- **Config:** the TV's own kernel config, read from its firmware.  The build config matches it exactly
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `5b31f38ec14ecdb581a58ca0ad8f5a93647219058eae33e6cb9cf546074e59da`
- **Checks:** `vermagic=4.4.84-417.gld4tv.7 SMP preempt mod_unload ARMv7`.  The kernel has MODVERSIONS and module signing off, and all 95 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4.  The same source as the other 4.4 builds
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156 (2.5 gigabit).  For RTL8152 and RTL8153, `test-driver` tries the kernel's own `r8152.ko` above first
- **SHA-256:** `f00752a9ac4d6f0f32f4eb2bde34c4204178af7cf76207c5d4d79a8bd8bb593e`
- **Checks:** `vermagic=4.4.84-417.gld4tv.7 SMP preempt mod_unload ARMv7`, and all 134 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** `drivers/net/usb/ax88179_178a.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** ASIX AX88179 and AX88178A (gigabit)
- **SHA-256:** `5ee303ec7ce71100ad7529720792d0807789a464e68bf17184b99eb643642f39`
- **Checks:** `vermagic=4.4.84-417.gld4tv.7 SMP preempt mod_unload ARMv7`, and all 48 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `355b6be0802984379e76de956baa551e57c5979e76dcdfe0245d57ebf8929400`
- **Checks:** `vermagic=4.4.84-417.gld4tv.7 SMP preempt mod_unload ARMv7`, and all 45 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `166c0bdd895cfeee9e46cdb24e65ec869a431d1c8a265e8dd926537ccb7eb948`
- **Checks:** `vermagic=4.4.84-417.gld4tv.7 SMP preempt mod_unload ARMv7`, and all 119 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's (not at all).
