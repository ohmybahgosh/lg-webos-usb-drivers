# Drivers for kernel 5.4.268-294.24.papikonda.2 on the K8Hp chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** TVs with Realtek's K8Hp chip, on webOS 25 firmware 33.31.  Only for that chip: other chips run the same kernel name with their own config
- **Kernel source:** LG Open Source package "webOS25 WH ReNew" (for the OLED65B4), `soc_HP/kernel-294.ptl4tv.2.tar.gz`, with `CHIP_NAME=k8`.  LG's `drivers/rtk_kdriver` tree is a separate package, so empty folders stand in for it: none of the options it defines are used by a kernel header.  This source has no `arch/arm64/mach-k8`, so its Kconfig was made from the TV's own config with `kconfig-stub.py`, keeping every K8 option with the TV's value (some, like `REALTEK_SCHED_LOG` and `REALTEK_MEMORY_MANAGEMENT`, change kernel headers).
- **Config:** the one built into the TV's own kernel, taken from LG's firmware for that kernel and chip
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot` so it can sit beside an old built-in `r8152`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source)
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156
- **SHA-256:** `6b771e9b1abe20dabff4278a0ce290f788d8498a9b39a4d954fc43fcf5570730`
- **Checks:** `vermagic=5.4.268-294.24.papikonda.2 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 127 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## aqc111.ko

- **Driver:** `drivers/net/usb/aqc111.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `3f453ed44878450fc3958842d9113317de25e1b48f8032fe82a4f14bf2d015ef`
- **Checks:** `vermagic=5.4.268-294.24.papikonda.2 SMP preempt mod_unload aarch64`, and all 50 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `99d211281c84260bd21990b95650f03223d08f2a12c173a2e4c864b63f44c2e0`
- **Checks:** `vermagic=5.4.268-294.24.papikonda.2 SMP preempt mod_unload aarch64`, and all 44 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `307cb2d8792dbf6d6ad6e1e0694973b3f96a68608687a648bbd84b6e4c7e2dd3`
- **Checks:** `vermagic=5.4.268-294.24.papikonda.2 SMP preempt mod_unload aarch64`, and all 137 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
