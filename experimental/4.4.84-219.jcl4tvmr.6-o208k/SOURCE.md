# Drivers for kernel 4.4.84-219.jcl4tvmr.6 on the O208K chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2020 8K LCDs with the O208K chip: the NANO97 and NANO99, and the ZX 8K OLED, on firmware 04.63.20 to 04.64.00 (webOS 5).  The CX runs the same kernel name with Realtek and ASIX built in, but this chip's config has only ASIX's older AX88772 driver and usbnet.  `usbnet` is built in, so no helper module is needed
- **Kernel source:** LG Open Source package "webOS 5.0 JO 2.0" (for OLED65CXGNA and similar), `JO-r3357_SoC/SoC_BSP_webOS_5.0.tar`, `kdriver/kernel/linux-4.4-lg115x.tgz`: LG's own 4.4.84 kernel for its O20 chip family
- **Config:** the TV's own kernel config, read from its firmware.  The only difference from it is `RTL8211F_PHY`, a PHY driver the TV has and the source doesn't.  No USB or network option differs
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which this chip's config leaves out
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `683f671f1160f63b0a8eb227269aee6b9c048f781c24693e106304a69e45da82`
- **Checks:** `vermagic=4.4.84-219.jcl4tvmr.6 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 92 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4.  The same source as the K6Lp and K7LP builds
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156 (2.5 gigabit).  For RTL8152 and RTL8153, `test-driver` tries the kernel's own `r8152.ko` above first
- **SHA-256:** `3c7318f557bbdc3ca92227c539a2242839492fe86efd0188e043f0e0f90d3fb6`
- **Checks:** `vermagic=4.4.84-219.jcl4tvmr.6 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 128 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** `drivers/net/usb/ax88179_178a.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** ASIX AX88179 and AX88178A (gigabit)
- **SHA-256:** `6d9e6ba60d0ceed982f2ab8d2beb26f4dab43ecdb35e52a4f331be4e4df9bfe5`
- **Checks:** `vermagic=4.4.84-219.jcl4tvmr.6 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 44 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `176a606d09f670a3f64ae8588acc74a42835ac6ffb5021214529c1d2060393cb`
- **Checks:** `vermagic=4.4.84-219.jcl4tvmr.6 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 42 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `c0edae429e7ce2120ffc0947e8c00f4b2738d0aa892bf374229e528ff97befc9`
- **Checks:** `vermagic=4.4.84-219.jcl4tvmr.6 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 113 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
