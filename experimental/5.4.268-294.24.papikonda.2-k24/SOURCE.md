# r8152_oot.ko for kernel 5.4.268-294.24.papikonda.2 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer it.  If your TV runs this kernel, please try it and report back: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build), the way [DonZoomik](https://github.com/DonZoomik/webos-r8152) built his
- **SHA-256:** `cd06aaa0cd54da1de85e1e70568f2521aa539e3fc7695e85361c4524cb758da6`
- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot` so it can sit beside an old built-in `r8152`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source), from [DonZoomik/webos-r8152](https://github.com/DonZoomik/webos-r8152) at commit `1ea8e98a24ef7443c590024d48947fee22d29cf1`
- **TVs:** 2024 and 2025 TVs with Realtek's K24 chip, on firmware 33.31 (webOS 25), like the B4.  Only for the K24 chip: other chips run the same kernel name with a different config
- **Adapters:** Realtek RTL8152, RTL8153, RTL8156 and OEM versions of them
- **Kernel source:** LG Open Source package "webOS25 WH ReNew" for the OLED65B4 (`soc_HP/kernel-294.ptl4tv.2.tar.gz`), with `CHIP_NAME=k24`
- **Config:** the one built into the TV's own kernel, from LG firmware for that kernel
- **Checks:** `vermagic=5.4.268-294.24.papikonda.2 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 127 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked: DonZoomik's offsets are for LG's own chips, so this one needs a tester.
- **License:** GPL-2.0, like the driver it's built from

`build-modinfo.txt`, `build-imports.txt` and `build-config-differences.txt` are from the build: the module's info, the symbols it imports, and how the build config differs from the TV's (only options the source adds or the TV has from LG's private code).

## aqc111.ko

- **Driver:** `drivers/net/usb/aqc111.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `3959879213f72638e546da73dffc50678700238912a56f33d5112cbfeb198daf`
- **Checks:** `vermagic=5.4.268-294.24.papikonda.2 SMP preempt mod_unload aarch64`, and all 50 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `d682e31c6b36b29bd80dca2a65a3af88cbc0ac61d2c97f32d72af44cd306f121`
- **Checks:** `vermagic=5.4.268-294.24.papikonda.2 SMP preempt mod_unload aarch64`, and all 44 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `adc995220f60b5dc3102e0f91f2aa8f3860d807ebe3c6506971ec16257f9903b`
- **Checks:** `vermagic=5.4.268-294.24.papikonda.2 SMP preempt mod_unload aarch64`, and all 137 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.
