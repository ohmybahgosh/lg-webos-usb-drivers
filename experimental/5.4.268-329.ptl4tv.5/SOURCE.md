# Drivers for kernel 5.4.268-329.ptl4tv.5 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer them.  If your TV runs this kernel, please try one and report back: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

This kernel's Realtek driver is DonZoomik's, known to work: it's in [`drivers/5.4.268-329.ptl4tv.5`](../../drivers/5.4.268-329.ptl4tv.5).  These are for chips the kernel has no driver for at all.

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build)
- **TVs:** 2022 to 2025 OLEDs on webOS 25 firmware 33.30 and 33.31, like the C2, C3, C4 and G4.  The O24, O24N and O22N3 chips' configs for it are identical; others with LG's own chips run the same kernel name too.
- **Kernel source:** LG Open Source package "webOS25 WG ReNew" for the OLED65C2 (`linux-and-kdriver_paluma-5`), the same source as this folder's neighbour `5.4.268-329.ptl4tv.2`
- **Config:** the one built into the TV's own kernel, from LG's firmware for the OLED65G4 (O24), identical to the O24N's and O22N3's
- **License:** GPL-2.0, like the kernel and drivers they're built from

## aqc111.ko

- **Driver:** `drivers/net/usb/aqc111.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Aquantia AQC111U and AQC112 (5G and 2.5G), and the ASIX, TRENDnet and QNAP adapters built on them
- **SHA-256:** `f0ae71e08989869d421ed95805a4289882dabcbddcfe5be9e385a4251f55538e`
- **Checks:** `vermagic=5.4.268-329.ptl4tv.5 SMP preempt mod_unload aarch64`, and all 50 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## dm9601.ko

- **Driver:** `drivers/net/usb/dm9601.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Davicom DM9601 and the 100 Mbit adapters built on it
- **SHA-256:** `96d1aa4303097d31b900334363cff4712473efad7a37946ec2365c0a5d0c4f98`
- **Checks:** `vermagic=5.4.268-329.ptl4tv.5 SMP preempt mod_unload aarch64`, and all 43 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

## lan78xx.ko

- **Driver:** `drivers/net/usb/lan78xx.c` from the same LG kernel source, built as a module, since this kernel leaves it out
- **Adapters:** Microchip LAN7800 and LAN7850
- **SHA-256:** `24ef5be91a809b1e7f80c7ab5a90aac2d5e910fed1a92820b5891445addc8627`
- **Checks:** `vermagic=5.4.268-329.ptl4tv.5 SMP preempt mod_unload aarch64`, and all 138 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked, so it needs a tester.

`build-*` files are from the build: each module's info, the symbols it imports, and how the build config differs from the TV's.
