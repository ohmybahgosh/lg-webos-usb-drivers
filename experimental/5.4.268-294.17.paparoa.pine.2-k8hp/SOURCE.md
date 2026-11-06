# Drivers for kernel 5.4.268-294.17.paparoa.pine.2 on the K8Hp chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** TVs with Realtek's K8Hp chip, on firmware 33.22 and 33.23 (webOS 25).  Only for that chip: other chips run the same kernel name with their own config
- **Kernel source:** LG Open Source package "webOS25 WH ReNew" (for the OLED65B4), `soc_HP/kernel-294.ptl4tv.2.tar.gz`, with `CHIP_NAME=k8`: the same 294 kernel line, a later revision.  Built with the TV's config, none of the options the source lacks is used by a kernel header.  LG's `drivers/rtk_kdriver` tree is a separate package, so empty folders stand in for it: none of the options it defines are used by a kernel header.  This source has no `arch/arm64/mach-k8`, so its Kconfig was made with `kconfig-stub.py` from a webOS 25 K8 TV's config.  That declares the K8 options (some, like `REALTEK_SCHED_LOG` and `REALTEK_MEMORY_MANAGEMENT`, change kernel headers), and the build keeps this TV's value for each.
- **Config:** the one built into the TV's own kernel, taken from LG's firmware for that kernel and chip
- **Already offered on this kernel:** `get-driver` has mbenitez343's tested `r8152` for RTL8152 and RTL8153 adapters, so `test-driver` offers this `r8152_oot` only for adapters that one doesn't cover, like the 2.5 gigabit RTL8156
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot` so it can sit beside an old built-in `r8152`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `17f217cefd9cb059e8def04ec855fe6856338761eedd13753357ef893615d899`
- **Checks:** `vermagic=5.4.268-294.17.paparoa.pine.2 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 127 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** the kernel's own `ax88179_178a` driver (drivers/net/usb/ax88179_178a.c), which LG leaves out of this kernel
- **Adapters:** ASIX AX88179 and AX88178A
- **SHA-256:** `30b0d9a6327d6d3b8b878c4ac5ec82834710797215a4445753351d1adf26ebee`
- **Checks:** `vermagic=5.4.268-294.17.paparoa.pine.2 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 47 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
