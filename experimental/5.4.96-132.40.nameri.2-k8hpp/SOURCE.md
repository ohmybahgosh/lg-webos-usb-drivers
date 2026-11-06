# Drivers for kernel 5.4.96-132.40.nameri.2 on the K8Hpp chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** TVs with Realtek's K8Hpp chip, on firmware 03.31 (webOS 23).  Only for that chip: other chips run the same kernel name with their own config
- **Kernel source:** LG Open Source package "webOS 23 KHP+ 5.0" (for the 65QNED80ARA), `chipset/bsp/kernel-nbr4tv.39_2.tar.gz_00` to `_02` (kernel-1.0.0-nbr4tv.39, the 132 kernels' source), with `CHIP_NAME=k8`.
- **Config:** the one built into the TV's own kernel, taken from LG's firmware for that kernel and chip
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot` so it can sit beside an old built-in `r8152`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `154147119ccf6f431e93581c7f9f15b635fc62603b2cfd1f69a4dde53a836112`
- **Checks:** `vermagic=5.4.96-132.40.nameri.2 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 127 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a` driver (drivers/net/usb/ax88179_178a.c), which LG leaves out of this kernel
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `ceeeea4cac5d9e3301fe9bcf88ca4b22c6c52a908d7cabe1d9f74d14e528bde7`
- **Checks:** `vermagic=5.4.96-132.40.nameri.2 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 47 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## aqc111.ko

- **Driver:** `drivers/net/usb/aqc111.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `e75b6d423ba9c5526c015a20a256c15e4cb4a1e0af4fc9874855816c8004aef0`
- **Checks:** `vermagic=5.4.96-132.40.nameri.2 SMP preempt mod_unload aarch64`, and all 50 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `8443e4d3eaf9c6bf671841539c8db06d0ece2d9359fa29f6f76c2a41ff77e4d1`
- **Checks:** `vermagic=5.4.96-132.40.nameri.2 SMP preempt mod_unload aarch64`, and all 44 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `7215f6d6278851c20c9d09dfb55345fecaf8121f96643edb46539813b9d791ad`
- **Checks:** `vermagic=5.4.96-132.40.nameri.2 SMP preempt mod_unload aarch64`, and all 136 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
