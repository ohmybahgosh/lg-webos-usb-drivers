# Drivers for kernel 5.4.268-223.29.okapi.5 on the K24 chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** TVs with Realtek's K24 chip, on firmware 23.22 and 23.23 (webOS 24).  Only for that chip: other chips run the same kernel name with their own config
- **Kernel source:** LG hasn't published source for the 223 kernels on 5.4.268 (its webOS 24 packages hold 223 on 5.4.96), so these are built from the nearest 5.4.268 source: LG Open Source package "webOS25 WH ReNew" (for the OLED65B4), `soc_HP/kernel-294.ptl4tv.2.tar.gz`, with `CHIP_NAME=k24`.  Built with the TV's config, none of the options the source lacks is used by a kernel header.  The source turns on one more that a header uses, `GENERIC_IRQ_IPI`, which only changes interrupt descriptors these drivers never touch.  LG's `drivers/rtk_kdriver` tree is a separate package, so empty folders stand in for it: none of the options it defines are used by a kernel header.
- **Config:** the one built into the TV's own kernel, taken from LG's firmware for that kernel and chip
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot` so it can sit beside an old built-in `r8152`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `512583cb47eaa2aba21f11425a181753688941e4f1d91f8733172e07483a721c`
- **Checks:** `vermagic=5.4.268-223.29.okapi.5 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 127 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a` driver (drivers/net/usb/ax88179_178a.c), which LG leaves out of this kernel
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `f9d78b081979c205f604113253bede1519e79fb044e7464a4bb71bdc7cd2ddcf`
- **Checks:** `vermagic=5.4.268-223.29.okapi.5 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 47 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## aqc111.ko

- **Driver:** `drivers/net/usb/aqc111.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `2ba31f797bce60a9ea495491d0f56b82296ebce9074168d801302c99dce97b6a`
- **Checks:** `vermagic=5.4.268-223.29.okapi.5 SMP preempt mod_unload aarch64`, and all 50 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `5adfbb427ac0917f5b3e92e07014a7c09a3247108d09a996c20fe809363e112d`
- **Checks:** `vermagic=5.4.268-223.29.okapi.5 SMP preempt mod_unload aarch64`, and all 44 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `1d4df8cbef10eeedca9751cd11d3b93e7d7d9cf3988a1d228ef17269b0184d78`
- **Checks:** `vermagic=5.4.268-223.29.okapi.5 SMP preempt mod_unload aarch64`, and all 137 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
