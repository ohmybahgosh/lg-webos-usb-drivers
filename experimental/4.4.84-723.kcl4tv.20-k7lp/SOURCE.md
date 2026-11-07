# Drivers for kernel 4.4.84-723.kcl4tv.20 on the K7LP chip (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2021 LCD TVs with the K7LP chip (UP and NANO models) on firmware 03.53.46 (webOS 6).  The kernel has ASIX's older AX88772 driver and usbnet built in, but no Realtek, AX88179, Davicom or Microchip driver
- **Kernel source:** LG Open Source package "webOS 6.0 KLP_1.0" (for 55UP7670PUC and similar), `soc/kernel-1.0.0-711..4.tar.gz`.  That's revision 711 of LG's 4.4 kernel, and the TV runs 723, so these need a tester before anyone relies on them
- **Config:** the TV's own kernel config, read from its firmware.  The only differences from it are the DMA-BUF heap options (`DMABUF_HEAPS*`, `DMABUF_CARVEOUT_HEAP`), which the 711 source doesn't have.  No USB or network option differs
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c), which LG leaves out of this kernel
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `5b85ac1b84c0b9341f9c0bb87c325d27366b565b2d4961d0ec884292581a89c0`
- **Checks:** `vermagic=4.4.84-723.kcl4tv.20 SMP preempt mod_unload ARMv7`.  The kernel has MODVERSIONS and module signing off, and all 95 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4.  The same source as the K6Lp builds
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156 (2.5 gigabit).  For RTL8152 and RTL8153, `test-driver` tries the kernel's own `r8152.ko` above first
- **SHA-256:** `ec89ac2a0da869e2a784bca7c9304dc69a229f9cd8ff3f5673db82ee943e0015`
- **Checks:** `vermagic=4.4.84-723.kcl4tv.20 SMP preempt mod_unload ARMv7`, and all 134 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** `drivers/net/usb/ax88179_178a.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** ASIX AX88179 and AX88178A (gigabit)
- **SHA-256:** `08c91c63048b8efd7315227843bf34db4c11e7ea21966de509b3b9a1034bc725`
- **Checks:** `vermagic=4.4.84-723.kcl4tv.20 SMP preempt mod_unload ARMv7`, and all 48 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `58e26bceaa0f48e5f2703984b526747af7fbf344526e4e7f708e34039229a3ce`
- **Checks:** `vermagic=4.4.84-723.kcl4tv.20 SMP preempt mod_unload ARMv7`, and all 45 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `4e2f06b71522a8aac2d3db98e940ea5e66ad3238c46f2e759cc2958b0cce9ae5`
- **Checks:** `vermagic=4.4.84-723.kcl4tv.20 SMP preempt mod_unload ARMv7`, and all 119 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's (the DMA-BUF heap options only).
