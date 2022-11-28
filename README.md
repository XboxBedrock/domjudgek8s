# DomJudgeK8s

A little config util to setup domjudge for k8s, spinup as many instances as you wish
I spent 5 hours and my sanity for this so please read carefully

___
Prequsites:
-
- Install Kubernetes with kubectl ([read `prod.yml` for production setup](prod.md))
- Setup cgroups, [read `cgroups.md` for more info](cgroups.md)
- Have an instance of DOMJudge panel

___
The Process
-
> Time to lose sanity

The first step to this process is to create a kubernetes deployment
We have a lucky script to do this, clone this git repository and run `substitute.py`
```sh
python3 substitute.py
```
Fill in the fields as prompted, once done a `domjudge.yml` file will be created, this is important.

To start the deployment run `kubectl apply -f ./domjudge.yml`
To view pod status run `kubectl get pods`
If theres anything fatally wrong and you need to check logs run `kubectl logs <podid>`

This is basically the end of the setup, however you must make sure the prequsites are perfectly executed, as they are the hardest bit of the setup.

Redo the above steps if you deleted or want to setup a new config, this can be done on multiple machines for the same domjudge instance

---
Deleting
-
Suppose something goes fatally wrong and you need to kill all domjudge instances, run this handy command, no data loss will incur
```sh
kubectl delete deployment domjudge-spam
```