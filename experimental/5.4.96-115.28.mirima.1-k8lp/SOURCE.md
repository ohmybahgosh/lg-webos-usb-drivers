# Drivers for kernel 5.4.96-115.28.mirima.1 on the K8Lp chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** TVs with Realtek's K8Lp chip, on firmware 04.53 and 04.54 (webOS 22).  Only for that chip: other chips run the same kernel name with their own config
- **Kernel source:** LG Open Source package "webOS 22 KLP_12.0" (for the 55UQ8000), `repo/kernel-1.0.0-114.tar.gz`, with `CHIP_NAME=k8`.
- **Config:** the one built into the TV's own kernel, taken from LG's firmware for that kernel and chip
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot` so it can sit beside an old built-in `r8152`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `12614a7b59b47a74dc53822436059795ed351a247eba0fcb34587c419d3352db`
- **Checks:** `vermagic=5.4.96-115.28.mirima.1 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 127 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a` driver (drivers/net/usb/ax88179_178a.c), which LG leaves out of this kernel
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `29db46149c50823ea1810d3955d20c94f195bd3471b9ad4244c44030ed84d11e`
- **Checks:** `vermagic=5.4.96-115.28.mirima.1 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 47 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## aqc111.ko

- **Driver:** `drivers/net/usb/aqc111.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `d2eab394d0f5d1d180626ec9c9b1c46cbf549e854f842efefc84fd8ecde4df57`
- **Checks:** `vermagic=5.4.96-115.28.mirima.1 SMP preempt mod_unload aarch64`, and all 50 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `e3c7fd6b754d970201a6b81b7ef1804f66bc92d34daf69ce49b7af40c1d9d22c`
- **Checks:** `vermagic=5.4.96-115.28.mirima.1 SMP preempt mod_unload aarch64`, and all 44 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `b58cf2f43b91754ede3b3fd011238807172b1294311a663134b7d17f44212cca`
- **Checks:** `vermagic=5.4.96-115.28.mirima.1 SMP preempt mod_unload aarch64`, and all 136 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
