# Drivers for kernel 5.4.96-223.obr4tv.29 on the K24 chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** TVs with Realtek's K24 chip, on firmware 23.20 (webOS 24).  Only for that chip: other chips run the same kernel name with their own config
- **Kernel source:** LG Open Source package "webOS 24 K 2.0" (for the 55QNED85T3C), `code/K_kernel-223_2.tar.gz` (kernel-223.obr4tv.4), with `CHIP_NAME=k24`.
- **Config:** the one built into the TV's own kernel, taken from LG's firmware for that kernel and chip
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot` so it can sit beside an old built-in `r8152`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `952c2545a8a688981d16ed9f7865721d9a92e30b1d7e8a90f198eb46a4983c89`
- **Checks:** `vermagic=5.4.96-223.obr4tv.29 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 127 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a` driver (drivers/net/usb/ax88179_178a.c), which LG leaves out of this kernel
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `22a568c650178e9d8812dc65c4a7e8dc88c6311591fa2fbce8c368534d9ed6b6`
- **Checks:** `vermagic=5.4.96-223.obr4tv.29 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 47 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## aqc111.ko

- **Driver:** `drivers/net/usb/aqc111.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `69d383bff92f0658d48e559784bf188841879605194f8a8e5bd0c144ed44ce41`
- **Checks:** `vermagic=5.4.96-223.obr4tv.29 SMP preempt mod_unload aarch64`, and all 50 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `d6fadeb8edb4c32a68293dcd96e17585927668fa0d1dfe398a5a200c249c9380`
- **Checks:** `vermagic=5.4.96-223.obr4tv.29 SMP preempt mod_unload aarch64`, and all 44 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `0e82f33bda11df7a4398daaa2d8ff2dac12dafb9fba46f7b63b56519b81e2d6f`
- **Checks:** `vermagic=5.4.96-223.obr4tv.29 SMP preempt mod_unload aarch64`, and all 136 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
