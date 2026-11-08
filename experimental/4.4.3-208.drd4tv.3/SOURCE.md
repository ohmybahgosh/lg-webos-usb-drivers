# Drivers for kernel 4.4.3-208.drd4tv.3 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  `test-driver` (or Test a new driver in the LG-USB-2-ETH0 app) tries one: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2017 UJ63, UJ67 and UJ70 4K LCDs with the K3LP chip (a Realtek RTD289x), on firmware 06.10.70 and 06.10.75 (webOS 3.5).  The kernel already has `usbnet` and ASIX's older AX88772 driver built in, so AX88772 adapters work with no download; it has no Realtek, AX88179, Davicom or Microchip driver.  webOS 3.5 TVs can be rooted with [RootMyTV](https://rootmy.tv) on older firmware, or [faultmanager-autoroot](https://github.com/throwaway96/faultmanager-autoroot)
- **Kernel source:** LG Open Source package "webOS 3.5 DKLP3" (for 43UJ634Y-TD and similar), `DKLP3-r3185/open_source_KP/GPL2.0/kernel_DKLP3_MRM.tar.gz` (Linux 4.4.3), with `kdriver_DKLP3_MRM.tar.gz` unpacked as `drivers/rtk_kdriver` as its README says.  One change for today's compilers: `-fno-PIE` added to the Makefile's C flags, as later 4.4 kernels do
- **Config:** the TV's own kernel config, read from its firmware.  The build config matches it exactly
- **License:** GPL-2.0, like the kernel and drivers they're built from

## r8152.ko

- **Driver:** the kernel's own `r8152` driver (drivers/net/usb/r8152.c) from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Realtek RTL8152 and RTL8153 (gigabit), not RTL8156
- **SHA-256:** `ebd2bfb6af3e0cad297c1e12c25332850a00b422441cae35deac73d439f8d7be`
- **Checks:** `vermagic=4.4.3-208.drd4tv.3 SMP preempt mod_unload ARMv7`, and all 95 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## r8152_oot.ko

- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot`, with [`r8152-4.4.patch`](../source/r8152-4.4.patch) for kernel 4.4.  The same source as the other 4.4 builds
- **Adapters:** Realtek RTL8152, RTL8153 and RTL8156 (2.5 gigabit).  For RTL8152 and RTL8153, `test-driver` tries the kernel's own `r8152.ko` above first
- **SHA-256:** `d4fd0ba8929b1b61550b2618b3ed885d434f38ef2e076811f7f2d1e2fde49815`
- **Checks:** `vermagic=4.4.3-208.drd4tv.3 SMP preempt mod_unload ARMv7`, and all 134 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## ax88179_178a.ko

- **Driver:** `drivers/net/usb/ax88179_178a.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** ASIX AX88179 and AX88178A (gigabit)
- **SHA-256:** `352bacb1a20a3de1931e5d40c790eb86d1875463df03ad57956377fc8ab6d28c`
- **Checks:** `vermagic=4.4.3-208.drd4tv.3 SMP preempt mod_unload ARMv7`, and all 48 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `235c18e00870f39e572879146be3fd3c4011d9b0701c1fc358b70c5decb9fcdf`
- **Checks:** `vermagic=4.4.3-208.drd4tv.3 SMP preempt mod_unload ARMv7`, and all 45 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `d266c9c4220428bb30fa470fab7726c1bce701fdfff7e4ec3cbca8bb426529e6`
- **Checks:** `vermagic=4.4.3-208.drd4tv.3 SMP preempt mod_unload ARMv7`, and all 119 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's (not at all).
