#Production Kubernetes install

Vps method
-

1. Install Docker, which can be found [here](https://docs.docker.com/engine/install/)
2. Install Docker Engine, which can be found [here](https://docs.docker.com/engine/install/#server), this is different from docker
3. Adapt it for Kubernetes, instructions can be found [here](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#docker)
4. Install kubeadm along kubectl, as can be found [here](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-kubeadm-kubelet-and-kubectl)
5. Setup a cgroup driver, as found [here](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/)

___
Managed method
-
If you wish to use managed hosting like GCP, read the [kubernetes docs for your platform](https://kubernetes.io/docs/setup/production-environment/)