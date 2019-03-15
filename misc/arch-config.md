# Arch config

### network

ip link set wlp59s0 up iw wlp59s0 scan

```text
iw wlp59s0 link
Not connect
```

#### wifi-menu

this is the only awesome one

wpa\_supplicant

wifi-menu is a pseudo GUI of netctl netctl requires wpa\_supplicant

### file system

three partition, first starts from sector 2048

| what | size |
| :--- | :--- |
| EFI | 512M |
| linux | 236G |
| swap | 2G |

UEFI requires using EFI

EFI requries FAT 32 bootloader will be installed in EFI I will choose GRUB as bootloader

```text
mkfs.fat -F32 /dev/nvme0nipi
mkfs.ext4 /dev/sdX1
mkswap /dev/sdX2
swapon /dev/sdX2
```

### X

xinit allows a user to manually start an Xory

startx is a front-end for xinit



### dpi

xrandr --dpi 150

then a lot of things can be bigger

### configure

file in \*.d will be treated as its original conf, and parse one by one

/etc/environment ~/.xbindkeys ~/.xinitrc ~/etc/X11/xorg.conf.d

xinput lspci nmcli\(wifi\) wpa\_supplicant udevadm acpi\(a controlller of devices\) asla purseaudio\(purseaudio is a stable agent of asla\) xbacklight\(change the permission of /brightness

cat /sys/moduls

modinfo -p i915 systool -m i915 -av

dmesg

