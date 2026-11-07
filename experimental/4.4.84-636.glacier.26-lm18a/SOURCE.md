# Drivers for kernel 4.4.84-636.glacier.26 on the LM18A chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2018 UK62 to UK69 4K LCDs with the LM18A chip, on firmware 05.30.10 to 05.50.70 (webOS 4.0).  The kernel has no USB network driver at all, not even `usbnet`, so the ASIX and Davicom drivers come with a `usbnet.ko` the script loads first.  There's no Microchip LAN78xx build: this kernel leaves out the PHY library it needs.  webOS 4.0 TVs can be rooted with [faultmanager-autoroot](https://github.com/throwaway96/faultmanager-autoroot)
- **Kernel source:** LG Open Source package "webOS 4.0 GLMA MR_2.0" (for 43UK6300PLB and similar), `GLMA-r3232/kernel_glma_MR_c4cc66f0.tgz`: the 4.4.84 kernel for the LM18A chip, revision 636
- **Config:** the firmware's kernel has no built-in config, so this is the release `.config` that ships in LG's source tree for the same kernel revision (636).  The TV's own modules have the same vermagic, and every symbol the drivers import is exported by the TV's kernel image, read from its firmware
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `423aeba6c26282b701736341180a99f5e04b584244729f0b5a7c314792d5b456`
- **Checks:** `vermagic=4.4.84-636.glacier.26 SMP preempt mod_unload ARMv7`.  The kernel has MODVERSIONS and module signing off,, and all 96 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4.  The same source as the other 4.4 builds
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156 (2.5 gigabit).  For RTL8152 and RTL8153, `test-driver` tries the kernel's own `r8152.ko` above first
- **SHA-256:** `99c81dd48fb3feb3cc0d289a28e3d606dc8631106fcc00c3fb141117d3507321`
- **Checks:** `vermagic=4.4.84-636.glacier.26 SMP preempt mod_unload ARMv7`,, and all 130 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## usbnet.ko

- **Driver:** `drivers/net/usb/usbnet.c` from the same LG kernel source, built as a module: the core the ASIX and Davicom drivers need, which this kernel leaves out.  The script loads it first
- **Adapters:** none on its own
- **SHA-256:** `7374f9c280858f21e24d23c46a28991ee92fbfe6a9b20b4c7dc2121ce0040d43`
- **Checks:** `vermagic=4.4.84-636.glacier.26 SMP preempt mod_unload ARMv7`,, and all 101 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** `drivers/net/usb/ax88179_178a.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** ASIX AX88179 and AX88178A (gigabit)
- **SHA-256:** `4bef243a4dc461521ba69a17706b4994e2ffa0de543f3b8d386bdcb8452008a6`
- **Checks:** `vermagic=4.4.84-636.glacier.26 SMP preempt mod_unload ARMv7`,, and all 48 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `23c57483a3ebb10e9a6723f9333a0c69964036d17eb2c4c07744ac792a12cbd0`
- **Checks:** `vermagic=4.4.84-636.glacier.26 SMP preempt mod_unload ARMv7`,, and all 44 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from LG's release config (not at all).
