# lg-webos-usb-drivers

A mirror of the USB Ethernet driver modules that [LG-USB-2-ETH0](https://github.com/ohmybahgosh/LG-USB-2-ETH0)'s `get-driver` offers for rooted LG webOS TVs, so they stay available if an original repository goes away.

Everything in `drivers/` is copied byte for byte from its author's repository at a fixed commit, and each folder's `SOURCE.md` says who built it, where it came from and what it's for.  Credit and thanks go to those authors.  `experimental/` holds drivers this project built itself, waiting for testers (see [below](#experimental-waiting-for-testers)).

`get-driver` downloads from the author's repository first and only falls back to this mirror if that fails.  Either way, it keeps the file only if its SHA-256 matches the one pinned in the script, so this mirror can't hand out a different file.

| Kernel (`uname -r`) | Module | TVs | Adapters | Built by |
|---|---|---|---|---|
| `5.4.268-329.ptl4tv.5` | [`r8152_oot.ko`](drivers/5.4.268-329.ptl4tv.5) | 2022 C2, 2024 C4 (webOS 25) | Realtek RTL8152, RTL8153, RTL8156 | [DonZoomik](https://github.com/DonZoomik/webos-r8152) |
| `5.4.268-294.17.paparoa.pine.2` | [`r8152.ko`](drivers/5.4.268-294.17.paparoa.pine.2) | 2024 QNED and OLED, K25lp / Paparoa (webOS 25) | Realtek RTL8152, RTL8153 | [mbenitez343](https://github.com/mbenitez343/lg-webos-2024-ethernet-fix) |
| `4.4.84-612.jcl4tv.40` | [`ax88179_178a.ko`](drivers/4.4.84-612.jcl4tv.40) | 2020 UN7300 (webOS 5) | ASIX AX88179, AX88178A | [OCT0PUSCRIME](https://github.com/OCT0PUSCRIME/lg-webos-ax88179-driver) |
| `5.4.268-294.24.papikonda.2` | [`ax88179_178a.ko`](drivers/5.4.268-294.24.papikonda.2) | 2025 B5 (webOS 25) | ASIX AX88179, AX88178A | [dd3git](https://github.com/dd3git/lg-webos-ax88179-driver) |
| `4.4.84`, K5Lp chip | [`r8152.ko`, `ax88179_178a.ko`](drivers/k5lp-4.4.84) | TVs with the Realtek K5Lp chip | Realtek RTL8152, RTL8153; ASIX AX88179, AX88178A | [throwaway96](https://github.com/throwaway96/webos-kernel-drivers) |

`SHA256SUMS` lists every module's checksum.

## Experimental: waiting for testers

These are built from LG's own kernel source with [LG-USB-2-ETH0's driver build](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md), the way DonZoomik built his.  Each one passed the build's checks (exact `vermagic`, every imported symbol exported by the TV's kernel), but **none has run on a TV yet**, so `get-driver` doesn't offer them.  If your TV runs one of these kernels, please [try it](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one) and report back.

| Kernel (`uname -r`) | Module | TVs | Adapters |
|---|---|---|---|
| `5.4.268-329.ptl4tv.2` | [`r8152_oot.ko`](experimental/5.4.268-329.ptl4tv.2) | 2022 to 2025 OLEDs on firmware 33.20 to 33.23 | Realtek RTL8152, RTL8153, RTL8156 |
| `5.4.268-320` | [`r8152_oot.ko`](experimental/5.4.268-320) | OLEDs on webOS 23 firmware 23.20 to 23.25 | Realtek RTL8152, RTL8153, RTL8156 |
| `5.4.96-307` | [`r8152_oot.ko`](experimental/5.4.96-307) | 2022 and 2023 OLEDs on firmware 03.31, 03.33 and 13.30 | Realtek RTL8152, RTL8153, RTL8156 |
| `5.4.268-294.24.papikonda.2`, K24 chip only | [`r8152_oot.ko`](experimental/5.4.268-294.24.papikonda.2-k24) | 2024 and 2025 TVs with the K24 chip, like the B4 | Realtek RTL8152, RTL8153, RTL8156 |
| `4.4.84-612.40.jimna.1`, K6Lp chip only | [`r8152.ko`, `ax88179_178a.ko`](experimental/4.4.84-612.40.jimna.1-k6lp) | 2020 TVs with the K6Lp chip (like the UN7300) on firmware 04.64 | Realtek RTL8152, RTL8153; ASIX AX88179, AX88178A |
| `4.4.84-612.21.6.jardine.2`, K6Lp chip only | [`r8152.ko`, `ax88179_178a.ko`](experimental/4.4.84-612.21.6.jardine.2-k6lp) | 2020 TVs with the K6Lp chip on firmware 03.21 | Realtek RTL8152, RTL8153; ASIX AX88179, AX88178A |
| `5.4.268-294.24.papikonda.2`, k24n chip only | [`r8152_oot.ko`](experimental/5.4.268-294.24.papikonda.2-k24n) | TVs with Realtek's K24N chip (like the 2025 B5), webOS 25 firmware 33.31 | Realtek RTL8152, RTL8153 and RTL8156 |
| `5.4.268-294.24.papikonda.2`, k25lp chip only | [`r8152_oot.ko`](experimental/5.4.268-294.24.papikonda.2-k25lp) | TVs with Realtek's K25Lp chip, webOS 25 firmware 33.31 | Realtek RTL8152, RTL8153 and RTL8156 |
| `5.4.268-294.24.papikonda.2`, k8hp chip only | [`r8152_oot.ko`](experimental/5.4.268-294.24.papikonda.2-k8hp) | TVs with Realtek's K8Hp chip, webOS 25 firmware 33.31 | Realtek RTL8152, RTL8153 and RTL8156 |
| `5.4.268-294.24.papikonda.2`, k8hpp chip only | [`r8152_oot.ko`](experimental/5.4.268-294.24.papikonda.2-k8hpp) | TVs with Realtek's K8Hpp chip, webOS 25 firmware 33.31 | Realtek RTL8152, RTL8153 and RTL8156 |
| `5.4.268-294.24.papikonda.2`, k8lpn chip only | [`r8152_oot.ko`](experimental/5.4.268-294.24.papikonda.2-k8lpn) | TVs with Realtek's K8LpN chip, webOS 25 firmware 33.31 | Realtek RTL8152, RTL8153 and RTL8156 |
| `5.4.268-294.24.papikonda.2`, k8lpn2 chip only | [`r8152_oot.ko`](experimental/5.4.268-294.24.papikonda.2-k8lpn2) | TVs with Realtek's K8LpN2 chip, webOS 25 firmware 33.31 | Realtek RTL8152, RTL8153 and RTL8156 |
| `5.4.268-294.ptl4tv.24`, k24n chip only | [`r8152_oot.ko`](experimental/5.4.268-294.ptl4tv.24-k24n) | TVs with Realtek's K24N chip (like the 2025 B5), webOS 25 firmware 33.30 | Realtek RTL8152, RTL8153 and RTL8156 |
| `5.4.268-294.ptl4tv.24`, k25lp chip only | [`r8152_oot.ko`, `ax88179_178a.ko`](experimental/5.4.268-294.ptl4tv.24-k25lp) | TVs with Realtek's K25Lp chip, webOS 25 firmware 33.30 | Realtek RTL8152, RTL8153 and RTL8156; ASIX AX88179 and AX88178A |
| `5.4.96-115.30.mole.2`, k8hp chip only | [`r8152_oot.ko`, `ax88179_178a.ko`](experimental/5.4.96-115.30.mole.2-k8hp) | TVs with Realtek's K8Hp chip, firmware 04.60 (webOS 22) | Realtek RTL8152, RTL8153 and RTL8156; ASIX AX88179 and AX88178A |
| `5.4.96-115.30.mole.2`, k8lp chip only | [`r8152_oot.ko`, `ax88179_178a.ko`](experimental/5.4.96-115.30.mole.2-k8lp) | TVs with Realtek's K8Lp chip, firmware 04.60 (webOS 22) | Realtek RTL8152, RTL8153 and RTL8156; ASIX AX88179 and AX88178A |
| `5.4.96-115.30.mole.2`, k8ap chip only | [`r8152_oot.ko`, `ax88179_178a.ko`](experimental/5.4.96-115.30.mole.2-k8ap) | TVs with Realtek's K8Ap chip, firmware 04.60 (webOS 22) | Realtek RTL8152, RTL8153 and RTL8156; ASIX AX88179 and AX88178A |
| `5.4.96-115.28.mirima.1`, k8hp chip only | [`r8152_oot.ko`, `ax88179_178a.ko`](experimental/5.4.96-115.28.mirima.1-k8hp) | TVs with Realtek's K8Hp chip, firmware 04.53 and 04.54 (webOS 22) | Realtek RTL8152, RTL8153 and RTL8156; ASIX AX88179 and AX88178A |
| `5.4.96-115.28.mirima.1`, k8lp chip only | [`r8152_oot.ko`, `ax88179_178a.ko`](experimental/5.4.96-115.28.mirima.1-k8lp) | TVs with Realtek's K8Lp chip, firmware 04.53 and 04.54 (webOS 22) | Realtek RTL8152, RTL8153 and RTL8156; ASIX AX88179 and AX88178A |
| `5.4.96-115.28.mirima.1`, k8ap chip only | [`r8152_oot.ko`, `ax88179_178a.ko`](experimental/5.4.96-115.28.mirima.1-k8ap) | TVs with Realtek's K8Ap chip, firmware 04.53 and 04.54 (webOS 22) | Realtek RTL8152, RTL8153 and RTL8156; ASIX AX88179 and AX88178A |

`experimental/SHA256SUMS` lists their checksums.

## Using one

You don't need to download anything from here by hand.  On the TV:

```sh
sh LG-USB-2-ETH0.sh get-driver
```

It only offers a module built for your exact kernel, and only when an adapter it supports is plugged in.  Or use the Faster driver switch in the LG-USB-2-ETH0 TV app.

## Licenses

These are Linux kernel driver modules, licensed under GPL-2.0 like the drivers they're built from.  Each folder notes where its source is.  If you built one of these and want it changed or removed, [open an issue](https://github.com/ohmybahgosh/lg-webos-usb-drivers/issues).
