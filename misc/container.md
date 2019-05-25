# container


## process virtualization


For container, it doens't need a hypervisor, just needs a container engine, and the Container engine isn't even a real thing, it's more like a concept, actually in host OS, just splitting namespace


### implementation 


- namespaces for isolation
- control groups(cgroups)
- linux security modules
- union style filesystems


#### naemspace


7 namespaces provide full virtualization for process.

IPC, Network, Mount, PID, User, UTS and Cgroup

`/proc/<pid>/ns`


- IPC 
    different process ahs its own IPC namespace, 
