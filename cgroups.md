# C Groups

 > *We edit the grub config to add cgroup memory and swap accounting to the boot options.*

 - Edit /etc/default/grub and change the default commandline to `GRUB_CMDLINE_LINUX_DEFAULT="quiet cgroup_enable=memory swapaccount=1" `
 - Run `update-grub` in terminal and reboot