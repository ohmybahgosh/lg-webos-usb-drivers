# Drivers for kernel 4.4.84-150.glacier.2 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2018 OLEDs (B8, C8, E8 and others, with the O18 or M16PP chip), 2018 SK NanoCells (M16PP) and some 2018 UK LCDs (M16PP LITE), on firmware 05.10 to 05.50 (webOS 4.0).  The kernel has Realtek's `r8152` and the old `rtl8150` built in, but no `usbnet`, so the ASIX, Davicom and Microchip drivers come with a `usbnet.ko` the script loads first.  webOS 4.0 TVs can be rooted with [faultmanager-autoroot](https://github.com/throwaway96/faultmanager-autoroot)
- **Kernel source:** LG Open Source package "webOS 4.0 GO_3.0" (for OLED55C8GNA and similar), `GO-r3232/SIC_GO_MR.zip`: `kdriver/kernel/linux-4.4-lg115x.tgz`, the 4.4.84 kernel for LG's own chips
- **Config:** the TV's own kernel config, read from its firmware.  The build config matches it exactly.  The O18 and M16PP firmware have the same kernel config, so one build covers both
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4.  The same source as the other 4.4 builds
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156 (2.5 gigabit).  The kernel's own `r8152` is built in and already handles RTL8152 and RTL8153, so this one is for RTL8156
- **SHA-256:** `e50889d81f41dfc4c8a3c36c4d22a27068d1c859aa560ea354ccf50fe6110997`
- **Checks:** `vermagic=4.4.84-150.glacier.2 SMP preempt mod_unload ARMv7`, and all 132 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## usbnet.ko

- **Driver:** `drivers/net/usb/usbnet.c` from the same LG kernel source, built as a module: the core the ASIX, Davicom and Microchip drivers need, which this kernel leaves out.  The script loads it first
- **Adapters:** none on its own
- **SHA-256:** `0b0e23b0484ba216755d95789f2e5836675972d6aadf6d3f246cfb430f3741b2`
- **Checks:** `vermagic=4.4.84-150.glacier.2 SMP preempt mod_unload ARMv7`, and all 99 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** `drivers/net/usb/ax88179_178a.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** ASIX AX88179 and AX88178A (gigabit)
- **SHA-256:** `5e08e1ada063109f903d4564e14988d5219bc6150728688221e14622143043d3`
- **Checks:** `vermagic=4.4.84-150.glacier.2 SMP preempt mod_unload ARMv7`, and all 48 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `276b96fc1f8ae61fab02afa68f2c65278d7397c128173713c9e14826fafcdf15`
- **Checks:** `vermagic=4.4.84-150.glacier.2 SMP preempt mod_unload ARMv7`, and all 45 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `92799ec232f1c0c680978bc95afd788eb021b1872b6ebd492d54ef78b7676639`
- **Checks:** `vermagic=4.4.84-150.glacier.2 SMP preempt mod_unload ARMv7`, and all 118 symbols it imports are exported by the TV's kernel (with `usbnet.ko` above loaded).  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's (not at all).
