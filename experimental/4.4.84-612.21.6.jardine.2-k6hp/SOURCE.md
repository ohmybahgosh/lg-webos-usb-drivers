# Drivers for kernel 4.4.84-612.21.6.jardine.2 on the K6Hp chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build), the way [OCT0PUSCRIME](https://github.com/OCT0PUSCRIME/lg-webos-ax88179-driver) built his webOS 5 ASIX driver
- **TVs:** 2020 TVs with Realtek's K6Hp chip (like the NANO87 and UN8900) on firmware 03.21 (webOS 5).  Its config is the same as the K6Lp one for this kernel, but the kernel image is its own
- **Kernel source:** LG Open Source package "webOS 5.0 JKHP 2.0" (for 55UN7310 and similar), `common/kernel-1.0.0-612.21.tar.gz` (612.21.6.jardine.3)
- **Config:** the one built into the TV's own kernel, taken from LG's firmware for that kernel and chip
- **How close the source is:** as for [the K6Lp build](../4.4.84-612.21.6.jardine.2-k6lp), since the K6Hp config is the same
- **License:** GPL-2.0, like the kernel they're built from

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of these kernels
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `dd36ef69cf25345c225452aa311b8133dccd502990ef0a58fc3851c4920d21d3`
- **Checks:** `vermagic=4.4.84-612.21.6.jardine.2 SMP preempt mod_unload ARMv7`, the same flags as LG's own modules for this kernel.  The kernel has MODVERSIONS and module signing off, and all 95 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4 (three small back-ports, and no 64-bit ioctl path on this 32-bit kernel).  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156 (2.5 gigabit).  For RTL8152 and RTL8153, `test-driver` tries the kernel's own `r8152.ko` above first
- **SHA-256:** `0b05d12230216382f60458f9b4966b135071ae06de4b8f47802b7447274a2f3b`
- **Checks:** `vermagic=4.4.84-612.21.6.jardine.2 SMP preempt mod_unload ARMv7`, the kernel has MODVERSIONS and module signing off, and all 134 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a` driver (drivers/net/usb/ax88179_178a.c), which LG leaves out of these kernels
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `bf0167932f63ec376d64174d8b4fb7698fc07eef95cf1f19ca9acec9252ad2da`
- **Checks:** `vermagic=4.4.84-612.21.6.jardine.2 SMP preempt mod_unload ARMv7`, the same flags as LG's own modules for this kernel.  The kernel has MODVERSIONS and module signing off, and all 48 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's (nothing).
