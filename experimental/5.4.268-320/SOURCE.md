# r8152_oot.ko for kernel 5.4.268-320 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer it.  If your TV runs this kernel, please try it and report back: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build), the way [DonZoomik](https://github.com/DonZoomik/webos-r8152) built his
- **SHA-256:** `952bb6b87b7889d4f6d197133d86ed16630d79c1c56c2f96ad89a51f4c4028f0`
- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot` so it can sit beside an old built-in `r8152`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source), from [DonZoomik/webos-r8152](https://github.com/DonZoomik/webos-r8152) at commit `1ea8e98a24ef7443c590024d48947fee22d29cf1`
- **TVs:** 2022 to 2024 OLEDs with LG's o22-family chips, on webOS 24 firmware 23.20 to 23.25
- **Adapters:** Realtek RTL8152, RTL8153, RTL8156 and OEM versions of them
- **Kernel source:** LG Open Source package "webOS25 WG ReNew" for the OLED65C2 (`linux-and-kdriver_paluma-5`, kernel revision 324)
- **Config:** the one built into the TV's own kernel, from LG firmware for that kernel
- **Checks:** `vermagic=5.4.268-320 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 128 symbols it imports are exported by the TV's kernel.  USB struct offsets: checked against the offsets DonZoomik measured on a real TV.
- **License:** GPL-2.0, like the driver it's built from

`build-modinfo.txt`, `build-imports.txt` and `build-config-differences.txt` are from the build: the module's info, the symbols it imports, and how the build config differs from the TV's (only options the source adds or the TV has from LG's private code).

## aqc111.ko

- **Driver:** `drivers/net/usb/aqc111.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `7ee11e7e65bc83f6f2958b60356ed5dd731624a7ebedecdc419491b868086784`
- **Checks:** `vermagic=5.4.268-320 SMP preempt mod_unload aarch64`, and all 50 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `19e568d8ca266bac2b9a75f8ac9ae6b9ff72f87eaf45b4b337bb655ce83b6a16`
- **Checks:** `vermagic=5.4.268-320 SMP preempt mod_unload aarch64`, and all 43 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `6deb8bac8a564a083f703653aa192e094ca1d561c40301ac750dc8dc512871cd`
- **Checks:** `vermagic=5.4.268-320 SMP preempt mod_unload aarch64`, and all 138 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.
