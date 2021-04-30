```
ssh root@95.181.152.85
```

```
The authenticity of host '95.181.152.85 (95.181.152.85)' can't be established.
ECDSA key fingerprint is SHA256:NJjx7DswufzHgw/txokxqB+w7SZDndX1W0EjIeT7n1U.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```

```
Warning: Permanently added '95.181.152.85' (ECDSA) to the list of known hosts.
root@95.181.152.85's password:
```

```
Welcome to Ubuntu 20.04 LTS (GNU/Linux 5.4.0-29-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@pysnippets:~#
```

```
❯ ssh-copy-id root@95.181.152.85
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/exenzi/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
root@95.181.152.85's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'root@95.181.152.85'"
and check to make sure that only the key(s) you wanted were added.
```

```
root@pysnippets:~# useradd -m -G sudo -s /bin/bash www
root@pysnippets:~# passwd www
New password:
Retype new password:
passwd: password updated successfully
```
```
❯ ssh-copy-id www@95.181.152.85
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/exenzi/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
www@95.181.152.85's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'www@95.181.152.85'"
and check to make sure that only the key(s) you wanted were added.


```

```
sudo apt update && sudo apt upgrade -y
```
```
Installing new version of config file /etc/dhcp/dhclient-enter-hooks.d/resolved ...

Configuration file '/etc/systemd/resolved.conf'
 ==> Modified (by you or by a script) since installation.
 ==> Package distributor has shipped an updated version.
   What would you like to do about it ?  Your options are:
    Y or I  : install the package maintainer's version
    N or O  : keep your currently-installed version
      D     : show the differences between the versions
      Z     : start a shell to examine the situation
 The default action is to keep your current version.
*** resolved.conf (Y/I/N/O/D/Z) [default=N] ? Y
```

`sudo apt install git -y`



