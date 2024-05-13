# Kubernetes

## Setup Kubernetes (Minikube)

### a. Prerequisite
- 2 CPUs or more
- 2GB of free memory
- 20GB of free disk space
- Internet connection
- Container or virtual machine manager, such as: Docker, QEMU, Hyperkit, Hyper-V, KVM, Parallels, Podman, VirtualBox, or VMware Fusion/Workstation

note : dalam modul praktikum kali ini, kita akan menggunakan Docker / VirtualBox / VMware

### b. Install Minikube

  Windows
  -
  - Buka Windows PowerShell (Run as Administrator)
  - Jalankan command berikut :
  ```
  New-Item -Path 'c:\' -Name 'minikube' -ItemType Directory -Force
  ```

  ```
  Invoke-WebRequest -OutFile 'c:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing
  ```
  
  - Tambahkan minikube.exe binary ke PATH
  ```
  $oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -inotcontains 'C:\minikube'){
  [Environment]::SetEnvironmentVariable('Path', $('{0};C:\minikube' -f $oldPath), [EnvironmentVariableTarget]::Machine)
}
```

  Linux
  -
  - Jalankan command berikut
  ```
  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  ```
  ```
  sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

  ```
  

  MacOS
  -
  - Jalankan command berikut
  ```
  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64
  ```
  ```
  sudo install minikube-darwin-amd64 /usr/local/bin/minikube

  ```

Source : https://minikube.sigs.k8s.io/docs/start/ 

### c. Start Minikube
```
minikube start
```
Jika sudah berhasil dijalankan, cek statusnya menggunakan command
```
minikube status
```
Output yang benar adalah seperti berikut:
```
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```
Minikube has kubectl as depedency, jadi sudah tidak diperlukan instalansi terpisah untuk kubectl

Pastikan bahwa kubectl sudah terinstal dengan menggunakan command
```
kubectl version --client
```
Jika sudah terinstal, maka outputnya adalah: 
```
Client Version: v1.30.0
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
```
## Main Kubernetes Component

### a. NODE vs POD vs CONTAINER

| Fitur       | Node                                      | Pod                                              | Container                                                |
|-------------|-------------------------------------------|--------------------------------------------------|----------------------------------------------------------|
| Definisi    | Sebuah mesin fisik atau virtual yang menjalankan Kubernetes, dapat berupa server atau instance cloud. | Sebuah unit terkecil yang dapat dijadwalkan dalam Kubernetes, yang berisi satu atau beberapa container. | Unit terkecil dalam sebuah pod, yang berisi aplikasi atau layanan yang dijalankan dalam sebuah pod. |
| Tugas Utama | Menyediakan lingkungan untuk menjalankan pod. | Menjalankan satu atau beberapa container dan menyediakan lingkungan untuk berbagi sumber daya. | Menjalankan aplikasi atau layanan yang spesifik, dan berbagi sumber daya dengan container lain dalam pod yang sama. |
| Isolasi     | Setiap node berjalan dalam lingkungan terisolasi dan memiliki sumber daya komputasi, memori, dan jaringan yang terpisah. | Setiap pod berjalan dalam lingkungan terisolasi tetapi dapat berbagi sumber daya seperti jaringan dan volume. | Setiap container berjalan dalam lingkungan terisolasi dan dapat memiliki sumber daya yang terbatas, seperti CPU dan memori. |
| Manajemen   | Dikelola oleh Kubernetes, dapat ditambahkan atau dihapus dari cluster Kubernetes. | Dikelola oleh Kubernetes, dapat dibuat, dihapus, atau diperbarui. | Dikelola oleh Docker atau runtime container lainnya, dapat dibuat, dihapus, atau dijalankan secara independen. |
| Jaringan     | Node memiliki alamat IP dan dapat berkomunikasi dengan node dan pod lain di dalam cluster. | Pod memiliki alamat IP yang unik dalam cluster, dan setiap pod memiliki kemampuan untuk berkomunikasi dengan pod lain dan node. | Container dapat berkomunikasi dengan container lain dalam pod menggunakan localhost, serta dengan pod dan node lain di dalam cluster menggunakan alamat IP pod dan node. |
| Ketersediaan | Node dapat ditambahkan atau dihapus dari cluster untuk meningkatkan ketersediaan atau kapasitas. | Pod dapat dideploy ulang ke node yang berbeda jika node asalnya gagal, untuk menjaga ketersediaan aplikasi. | Container dapat dimulai ulang atau dihapus dalam pod tanpa mempengaruhi pod lain di dalamnya, untuk menjaga ketersediaan layanan. |


### b. Service & Ingress

  External Service
  - 

  Internal Service
  - 

  Ingress
  - 

### c. ConfigMap
