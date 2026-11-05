# Drivers for kernel 5.4.268-223.42.okapi.nmrm.2 on the K24T chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** TVs with Realtek's K24T chip (like the 27LX6T StanbyME), on firmware 23.21 and 23.22 (webOS 24).  Only for that chip: other chips run the same kernel name with their own config
- **Kernel source:** LG hasn't published source for the 223 kernels on 5.4.268 (its webOS 24 packages hold 223 on 5.4.96), so these are built from the nearest 5.4.268 source: LG Open Source package "webOS25 WH ReNew" (for the OLED65B4), `soc_HP/kernel-294.ptl4tv.2.tar.gz`, with `CHIP_NAME=k24`.  Built with the TV's config, none of the options the source lacks is used by a kernel header.  The source turns on one more that a header uses, `GENERIC_IRQ_IPI`, which only changes interrupt descriptors these drivers never touch.  LG's `drivers/rtk_kdriver` tree is a separate package, so empty folders stand in for it: none of the options it defines are used by a kernel header.
- **Config:** the one built into the TV's own kernel, taken from LG's firmware for that kernel and chip
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot` so it can sit beside an old built-in `r8152`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `b4d92c085389e0da84ec8261bd12767c64dde2035ac6c12b7e1dc982224f1ba0`
- **Checks:** `vermagic=5.4.268-223.42.okapi.nmrm.2 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 127 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a` driver (drivers/net/usb/ax88179_178a.c), which LG leaves out of this kernel
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `1f17eb1cf7895edfe1743b14ad38374290cedaa247bad33963cd211035d992c8`
- **Checks:** `vermagic=5.4.268-223.42.okapi.nmrm.2 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 47 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
