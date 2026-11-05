# Drivers for kernel 4.4.84-612.40.jimna.1 on the K6Lp chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build), the way [OCT0PUSCRIME](https://github.com/OCT0PUSCRIME/lg-webos-ax88179-driver) built his webOS 5 ASIX driver
- **TVs:** 2020 TVs with Realtek's K6Lp chip (like the UN7300) on current firmware 04.64 (webOS 5).  Only for the K6Lp chip: K6Hp TVs run the same kernel name
- **Kernel source:** LG Open Source package "webOS 5.0 JKHP 2.0" (for 55UN7310 and similar), `common/kernel-1.0.0-612.21.tar.gz` (612.21.6.jardine.3)
- **Config:** the one built into the TV's own kernel, taken from LG's firmware for that kernel
- **How close the source is:** LG's source is revision 612.21 and this kernel 612.40.  Built with the TV's config, every option in it exists in the source, and 8,349 of the 8,447 symbols a full build of the source exports are in the TV's kernel (the rest are LG's TV tuner code)
- **License:** GPL-2.0, like the kernel they're built from

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of these kernels
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `388d01ae3d8d58ca7eb82e161bd5675e9d9f2be490a02c2f5c86c42be94edd8e`
- **Checks:** `vermagic=4.4.84-612.40.jimna.1 SMP preempt mod_unload ARMv7`, the same flags as LG's own modules for this kernel.  The kernel has MODVERSIONS and module signing off, and all 95 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a` driver (drivers/net/usb/ax88179_178a.c), which LG leaves out of these kernels
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `0e915333f96c755a292fbfe828ed689421661c46096b12ee897121c317631b22`
- **Checks:** `vermagic=4.4.84-612.40.jimna.1 SMP preempt mod_unload ARMv7`, the same flags as LG's own modules for this kernel.  The kernel has MODVERSIONS and module signing off, and all 48 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's (nothing).
