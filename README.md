# lg-webos-usb-drivers

A mirror of the USB Ethernet driver modules that [LG-USB-2-ETH0](https://github.com/ohmybahgosh/LG-USB-2-ETH0)'s `get-driver` offers for rooted LG webOS TVs, so they stay available if an original repository goes away.

Nothing here is built by this project.  Each module is copied byte for byte from its author's repository at a fixed commit, and each folder's `SOURCE.md` says who built it, where it came from and what it's for.  Credit and thanks go to those authors.

`get-driver` downloads from the author's repository first and only falls back to this mirror if that fails.  Either way, it keeps the file only if its SHA-256 matches the one pinned in the script, so this mirror can't hand out a different file.

| Kernel (`uname -r`) | Module | TVs | Adapters | Built by |
|---|---|---|---|---|
| `5.4.268-329.ptl4tv.5` | [`r8152_oot.ko`](drivers/5.4.268-329.ptl4tv.5) | 2022 C2, 2024 C4 (webOS 25) | Realtek RTL8152, RTL8153, RTL8156 | [DonZoomik](https://github.com/DonZoomik/webos-r8152) |
| `5.4.268-294.17.paparoa.pine.2` | [`r8152.ko`](drivers/5.4.268-294.17.paparoa.pine.2) | 2024 QNED and OLED, K25lp / Paparoa (webOS 25) | Realtek RTL8152, RTL8153 | [mbenitez343](https://github.com/mbenitez343/lg-webos-2024-ethernet-fix) |
| `4.4.84-612.jcl4tv.40` | [`ax88179_178a.ko`](drivers/4.4.84-612.jcl4tv.40) | 2020 UN7300 (webOS 5) | ASIX AX88179, AX88178A | [OCT0PUSCRIME](https://github.com/OCT0PUSCRIME/lg-webos-ax88179-driver) |

`SHA256SUMS` lists every module's checksum.

## Using one

You don't need to download anything from here by hand.  On the TV:

```sh
sh LG-USB-2-ETH0.sh get-driver
```

It only offers a module built for your exact kernel, and only when an adapter it supports is plugged in.  Or use the Faster driver switch in the LG-USB-2-ETH0 TV app.

## Licenses

These are Linux kernel driver modules, licensed under GPL-2.0 like the drivers they're built from.  Each folder notes where its source is.  If you built one of these and want it changed or removed, [open an issue](https://github.com/ohmybahgosh/lg-webos-usb-drivers/issues).
