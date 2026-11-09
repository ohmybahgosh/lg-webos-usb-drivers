# Drivers for kernel 4.4.3-119.drd4tv.6 on the M16P chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).  Asked for in [discussion #4](https://github.com/ohmybahgosh/LG-USB-2-ETH0/discussions/4).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2017 OLEDs like the C7 (OLED65C7T), and UJ7 4K LCDs like the 43UJ750V and 49UJ7800, with the M16P chip (LG1313), on firmware 06.10.65 (webOS 3.5).  The kernel has only `r8152` and `rtl8150` built in, with no `usbnet`, so the ASIX, Davicom and Microchip drivers come with a `usbnet.ko` the script loads first.  Only for the M16P chip: the UJ6200 (M16P LITE) runs a kernel with the same name, but its build wasn't checked.  webOS 3.5 TVs can be rooted with [RootMyTV](https://rootmy.tv) on older firmware, or [faultmanager-autoroot](https://github.com/throwaway96/faultmanager-autoroot)
- **Kernel source:** LG hasn't published this TV's own kernel (its "webOS DMP" package only has `kdriver`, the GPU module and video firmware), so these are built from a sibling: LG Open Source package "webOS 3.5 DKLP3" (for 43UJ634Y-TD and similar), `DKLP3-r3185/open_source_KP/GPL2.0/kernel_DKLP3_MRM.tar.gz`, LG's Linux 4.4.3 `drd4tv` tree with `mach-lg1k` (revision 208, the TV runs 119).  One change for today's compilers: `-fno-PIE` added to the Makefile's C flags, as later 4.4 kernels do
- **Config:** the TV's own kernel config, read from its firmware's kernel image (06.10.65), and the same as the one the tester posted.  This source drops two of its options no kernel header uses (`GPU_INFO`, `MRI_HELPER`) and adds some of its own: of those, only `CMA_RTK_ALLOCATOR` and `CMA_FIRST_POLICY` appear in kernel headers, where they only declare memory allocator functions these drivers don't use.  The `build-*-config-differences.txt` files list them all
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4.  The same source as the other 4.4 builds.  The kernel's own `r8152` is built in but too old for the RTL8153B (it logs `Unknown version 0x6010`) and the RTL8156
- **Adapters:** Realtek RTL8152, RTL8153 (including the RTL8153B) and RTL8156 (2.5 gigabit)
- **SHA-256:** `af80711e8fea081b836281223660b721dd26ba995f5f5e312e133885f7ad2c84`
- **Checks:** `vermagic=4.4.3-119.drd4tv.6 SMP preempt mod_unload ARMv7 p2v8`, and all 132 symbols it imports are exported by the TV's kernel.  Struct offsets: checked against the TV's own kernel image with `abi-check.py` (the size of `struct net_device` and the offsets in 17 network and USB core functions match).  It hasn't run on a TV yet, so it still needs a tester.

## usbnet.ko

- **Driver:** `drivers/net/usb/usbnet.c` from the same LG kernel source, built as a module: the core the ASIX, Davicom and Microchip drivers need, which this kernel leaves out.  The script loads it first
- **Adapters:** none on its own
- **SHA-256:** `83a046f10e739ebde0782973afd24146ba3b5d1052af9c5040bf481446db2d0c`
- **Checks:** `vermagic=4.4.3-119.drd4tv.6 SMP preempt mod_unload ARMv7 p2v8`, and all 99 symbols it imports are exported by the TV's kernel.  Struct offsets: checked against the TV's own kernel image with `abi-check.py` (the size of `struct net_device` and the offsets in 17 network and USB core functions match).  It hasn't run on a TV yet, so it still needs a tester.

## ax88179_178a.ko

- **Driver:** `drivers/net/usb/ax88179_178a.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** ASIX AX88179 and AX88178A (gigabit)
- **SHA-256:** `b37a3e20b9da3a4d072a377f167c6e99273be42da9326eb509ef6ae3c7ace24a`
- **Checks:** `vermagic=4.4.3-119.drd4tv.6 SMP preempt mod_unload ARMv7 p2v8`, and all 48 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  Struct offsets: checked against the TV's own kernel image with `abi-check.py` (the size of `struct net_device` and the offsets in 17 network and USB core functions match).  It hasn't run on a TV yet, so it still needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `a4cac01d3f78868eb2679bdd59b9e872501a335c2b1e26f974f267a33d321e59`
- **Checks:** `vermagic=4.4.3-119.drd4tv.6 SMP preempt mod_unload ARMv7 p2v8`, and all 45 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  Struct offsets: checked against the TV's own kernel image with `abi-check.py` (the size of `struct net_device` and the offsets in 17 network and USB core functions match).  It hasn't run on a TV yet, so it still needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `999f9df3e4246860df241612be4142ae98ff46766784934585f1aa71e31ae86b`
- **Checks:** `vermagic=4.4.3-119.drd4tv.6 SMP preempt mod_unload ARMv7 p2v8`, and all 118 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  Struct offsets: checked against the TV's own kernel image with `abi-check.py` (the size of `struct net_device` and the offsets in 17 network and USB core functions match).  It hasn't run on a TV yet, so it still needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
