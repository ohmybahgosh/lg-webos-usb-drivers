# Drivers for kernel 4.4.84-229.kcl4tv.6 on the E60N chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2021 LCDs with the E60N chip: the NANO96 to NANO99 and the QNED90 to QNED99 Mini LED models, on firmware 03.53.31 and 03.53.45 (webOS 6).  The C1 OLED runs the same kernel name with Realtek and ASIX built in, but this chip's config has only ASIX's older AX88772 driver and usbnet.  `usbnet` is built in, so no helper module is needed
- **Kernel source:** LG Open Source package "webOS 6.0 EN 1.0" (for 65QNED99UPA and similar), `soc/E_webOS_6.0.tgz`, `kdriver/kernel/linux-4.4-lg115x.tgz`: LG's own 4.4.84 kernel for its E60 chip
- **Config:** the TV's own kernel config, read from its firmware.  The only difference from it is exFAT (`EXFAT_FS`, `EXFAT_DEFAULT_IOCHARSET`), which the TV has and the source doesn't.  No USB or network option differs
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which this chip's config leaves out
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `456fd387dd142902b41a49187e1645c2a0dbcbf72695c4a6f7ec50bdad512a27`
- **Checks:** `vermagic=4.4.84-229.kcl4tv.6 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 92 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4.  The same source as the K6Lp and K7LP builds
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156 (2.5 gigabit).  For RTL8152 and RTL8153, `test-driver` tries the kernel's own `r8152.ko` above first
- **SHA-256:** `0f93773025026cf4e1c965d67a7ecb807db95b5d6eb5f2a20b116909bb4634c6`
- **Checks:** `vermagic=4.4.84-229.kcl4tv.6 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 128 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** `drivers/net/usb/ax88179_178a.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** ASIX AX88179 and AX88178A (gigabit)
- **SHA-256:** `ff396d3e0631c14b963aca896ad2a45e326464df95e707026265e36113946aa0`
- **Checks:** `vermagic=4.4.84-229.kcl4tv.6 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 44 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `add3ac9553d3eeb7a9a604e39e54a6fdc6296d746123047bc8246c010a865a0f`
- **Checks:** `vermagic=4.4.84-229.kcl4tv.6 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 42 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `7ed83a1334046625edef87f470aed4036e0567ad9e98e0bf2017a3c774fbe024`
- **Checks:** `vermagic=4.4.84-229.kcl4tv.6 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 113 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
