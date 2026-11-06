# Drivers for kernel 5.4.96-132.40.nameri.pine.1 on the K8Hp chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** TVs with Realtek's K8Hp chip, on firmware 13.30 (webOS 23).  Only for that chip: other chips run the same kernel name with their own config
- **Kernel source:** LG Open Source package "webOS 23 KHP+ 5.0" (for the 65QNED80ARA), `chipset/bsp/kernel-nbr4tv.39_2.tar.gz_00` to `_02` (kernel-1.0.0-nbr4tv.39, the 132 kernels' source), with `CHIP_NAME=k8`.
- **Config:** the one built into the TV's own kernel, taken from LG's firmware for that kernel and chip
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot` so it can sit beside an old built-in `r8152`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `1025328c8e302b29d18e5c10f1e207bdb61a76267223057c67f647eb4653d82b`
- **Checks:** `vermagic=5.4.96-132.40.nameri.pine.1 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 127 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a` driver (drivers/net/usb/ax88179_178a.c), which LG leaves out of this kernel
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `403e0e6de1cda42d6bea552178e07a063eb0360957adc76fc2163e038b02b68f`
- **Checks:** `vermagic=5.4.96-132.40.nameri.pine.1 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 47 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## aqc111.ko

- **Driver:** `drivers/net/usb/aqc111.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `d947f13c31cb71a7aa839ba140c388ac337f4d674ef619bad4a89754ee7e0ac7`
- **Checks:** `vermagic=5.4.96-132.40.nameri.pine.1 SMP preempt mod_unload aarch64`, and all 50 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `43ae2d91aabcfe31d3ac3c0b5e2a10a77c39da52ff700f363572786db68b5492`
- **Checks:** `vermagic=5.4.96-132.40.nameri.pine.1 SMP preempt mod_unload aarch64`, and all 44 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `4728e0d519081d4f2615fc96b2cc2f7b0ce10ac9bc6fa24fb0bb71efa29bea04`
- **Checks:** `vermagic=5.4.96-132.40.nameri.pine.1 SMP preempt mod_unload aarch64`, and all 136 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
