Package dependency solver
======
#### This program can parse \*.Packages files from repositories and solve dependencies<br/>


You can get \*.Packages from
---
1. [http://ports.ubuntu.com/dists/{dist}/{repo}/binary-{arch}/Packages.gz](http://ports.ubuntu.com/dists/{dist}/{repo}/binary-{arch}/Packages.gz)
    , where
    + `{dist}` is Ubuntu distribution, e.g., devel, precise, saucy, ...<br/>
    + `{repo` is the repository, i.e., main, restricted, universe or multiverse.<br/>
    + `{arch}` is the architecture, e.g., armhf.

    [Example](ports.ubuntu.com/dists/devel/main/binary-armhf/Packages.gz)
2. [http://ftp.debian.org/debian/dists/{dist}/{repo}/binary-{arch}/Packages.gz](http://ftp.debian.org/debian/dists/{dist}/{repo}/binary-{arch}/Packages.gz)
    , where
    + `{dist}` is Debian distribution, e.g.,    jessie, wheezy, sid, ...<br/>
    + `{repo}` is the repository, i.e., main, contrib or non-free.<br/>
    + `{arch}` is the architecture, e.g., i386.
    
    [Example](http://ftp.debian.org/debian/dists/jessie/main/binary-i386/Packages.gz)
3. [http://ppa.launchpad.net/{user}/ppa/ubuntu/dists/{dist}/{repo}/binary-{arch}/Packages.gz](http://ppa.launchpad.net/{user}/ppa/ubuntu/dists/{dist}/main/binary-{arch}/Packages.gz)
    , where
    + `{user}` is Launchpad user name or team name
    + `{dist}` is Ubuntu distribution, e.g., trusty, utopic, vivid
    + `{repo}` is the repository, i.e., main.
    + `{arch}` is the architecture, e.g., amd64.
    
    [Example](http://ppa.launchpad.net/deluge-team/ppa/ubuntu/dists/trusty/main/binary-amd64/Packages.gz)
4. Other repositories

How to use
---
+ You should convert \*.Packages file to json, using `convert.py`

    Usage: `convert.py [-r] I O`<br/>
        `I` **I**nput \*.Packages file<br/>
        `O` **O**utput json file<br/>
        `-r` Generate **r**eadable json *(much bigger)*
+ You can use `info.py` to get all information about package.
    
    Usage: `info.py D`<br/>
        `D` Packages **d**ata in json format
+ You can use `solve.py` to solve dependencies.
    
    Usage: `solve.py [-V] D`<br/>
        `D` Packages **d**ata in json format<br/>
        `-V` Ignore **v**ersions

Download packages data
---
[https://db.tt/PQaGrPc5](https://db.tt/PQaGrPc5) 366 MB unpacked (8 *.Packages, converted json and readable json)
