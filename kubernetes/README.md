# Kubernetes

## Apa itu Kubernetes?

Kubernetes adalah platform open-source yang digunakan untuk mengelola workloads aplikasi yang dikontainerisasi, serta menyediakan konfigurasi dan otomatisasi secara deklaratif. Dikembangkan oleh Google dan sekarang dikelola oleh Cloud Native Computing Foundation (CNCF), Kubernetes memungkinkan orkestrasi terhadap computing, networking, dan infrastruktur penyimpanan.

## Kenapa kok kita pakai Kubernetes?

Misalkan kita mendeploy website/aplikasi kita dengan menggunakan Docker. Dan website yang kita deploy sangat keren sekali sehingga banyak sekali orang yang mengunjungi website kita.

Karena teralu banyak orang yang datang ke website kita, server kita tidak bisa mengatasi traffic yang datang ke website tersebut sehingga website kita down.

Nah, untuk mengatasi solusi tersebut sangat mudah, kita hanya perlu mendeploy website backup serta load balancer sehingga jika website utama kita down, user bisa di arahkan ke website backup.

Namun, jika semakin banyak orang yang datang ke website kita sehingga 2 website saja tidak cukup, maka kita juga harus terus-terus mengkonfigurasi dan mendeploy website. Kalau masih 2 atau 5 mungkin tidak apa-apa, tapi bagaimana jika kita perlu meningkatkan website kita menjadi 100 website dan harus di deploy secara bersamaan dan harus mengkonfigurasi load balancernya?

Kubernetes lah solusinya. Dengan kubernetes kita dapat mengotomatisasi deployment website/aplikasi kita. Dengan kubernetes juga, jika ingin meningkatkan skala website kita (yang sebelumnya hanya 2 website menjadi 100) cukup mudah dan real time!

## Struktur sistem dengan kubernetes

Biasanya, sistem yang menggunakan kubernetes memiliki struktur sebagai berikut:

![Struktur Sistem Kubernetes](/struktur-kubernetes.png)


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

Kubernetes memiliki beberapa fitur dan komponen yang harus diketahui terlebih dahulu sebelum kita memulai menggunakannnya.

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

Hal ini merujuk pada mekanisme yang berbeda untuk mengatur bagaimana aplikasi dan layanan dalam kluster Kubernetes dapat diakses, baik dari dalam maupun luar kluster.

  External Service
  - 
  - External Service memungkinkan layanan Kubernetes untuk diakses dari luar kluster. Ini biasanya dicapai dengan menggunakan jenis layanan **LoadBalancer** atau **NodePort**.

LoadBalancer akan Secara otomatis menyediakan alamat IP eksternal yang dapat diakses dari luar kluster melalui load balancer dari penyedia cloud (misalnya, AWS ELB, Google Cloud Load Balancer).

Contoh Konfigurasi LoadBalancer :
```
apiVersion: v1
kind: Service
metadata:
  name: my-external-service
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```
NodePort akan membuka port tertentu pada semua node dalam kluster dan mem-forward traffic ke Service tersebut.

Contoh Konfigurasi NodePort :
```
apiVersion: v1
kind: Service
metadata:
  name: my-nodeport-service
spec:
  type: NodePort
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
      nodePort: 30000
```
Note : NodePorts are in the 30000-32767 range by default

  Internal Service
  - 
  - Internal Service memungkinkan layanan Kubernetes diakses hanya dari dalam kluster. Ini biasanya menggunakan jenis layanan ClusterIP, yang merupakan default.

Contoh Konfigurasi ClusterIP :
```
apiVersion: v1
kind: Service
metadata:
  name: my-internal-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```
Service ini hanya dapat diakses dari dalam kluster dan tidak menyediakan akses dari luar.

Note : ClusterIP merupakan type default dari service, tetapi tetap bisa didefinisikan dengan `type: ClusterIP`

  Ingress
  - 
  - Ingress adalah objek Kubernetes yang mengelola akses eksternal ke layanan dalam kluster, biasanya HTTP dan HTTPS. Ingress menyediakan aturan routing yang fleksibel, mendukung SSL, dan lain-lain.

Contoh Konfigurasi Ingress
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
spec:
  rules:
    - host: my-app.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-internal-service
                port:
                  number: 80
```
Untuk melihat type service yang dijalankan, kita dapat menggunakan command `kubectl get service` atau `kubectl get svc`

### c. ConfigMap

ConfigMap adalah objek Kubernetes yang digunakan untuk menyimpan data konfigurasi dalam bentuk pasangan `key: value`. ConfigMap memungkinkan untuk memisahkan konfigurasi aplikasi dari kode aplikasi, sehingga mempermudah manajemen konfigurasi dan memperbaiki praktik deployment.

Contoh Konfigurasi ConfigMap
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: example-configmap
data:
  # Pasangan key: value
  database_url: "jdbc:mysql://db.example.com:3306/mydatabase"
  database_user: "user123"
  database_password: "password123"
```

### Secret

Secret adalah salah satu fitur kubernetes yang sangat penting. Fungsinya adalah untuk menyimpan data-data/variable yang dibutuhkan oleh semua pods namun bersifat rahasia.

Misalkan kita ingin agar pods kita dapat mengakses pods database. Agar pods dapat mengakses database tentu saja perlu kredensial bukan? dengan menggunakan fitur secret ini, kredensial dapat di enkripsi sehingga tidak dapat dengan mudah diketahui oleh yang tidak berkepentingan.

Contoh konfigurasinya adalah sebagai berikut:
```
apiVersion: v1
kind: Secret
metadata:
  name: mongo-secret
data:
  mongo-user: bW9uZ291c2Vy
  mongo-password: bW9uZ29wYXNzd2Q=
```
Disini, kita setup aplikasi kita untuk bisa mengakses database dengan menggunakan kredensial berikut. Kredesial harus ditulis dengan di encode ke base64 sehingga fitur dapat bekerja.


### Load Balancer

Untuk mensetup load balancer khusus untuk sistem kubernetes kita dapat menggunakan konfigurasi berikut:
```
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
```
Dalam contoh ini, aplikasi yang digunakan adalah nginx. Jika kalian menggunakan aplikasi lain (misalnya apache2) kalian bisa membaca dokumentasi aplikasi tersebut untuk mendeploy Load Balancer menggunakan aplikasi tersebut.

### Deployment

Terakhir, berikut adalah contoh konfigurasi untuk mendeploy aplikasi nginx:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      nodePort: 30080
```
Note:  **Setiap aplikasi bisa jadi memiliki konfigurasi yang berbeda, selalu cek konfigurasi aplikasi tersebut untuk menggunakannya dengan kubernetes**.

Untuk konfigurasi di atas, kita akan mendeploy aplikasi 3 aplikasi nginx sekaligus (dari variable **replicas**) dan di setiap pods nya, nginx dapat di akses di port 80.

Agar kita dapat mengakses nginx, kita akan mengakses via port 30080 yang nantinya akan di forward oleh kubernetes ke port 80 aplikasi nginx.

### Aplikasikan konfigurasi ke kubernetes

Lalu, kita akan menjalankan command berikut untuk mengaplikasikan konfigurasi-konfigurasi yang kita buat ke kubernetes:
```
kubectl apply -f config.yaml
```
Sebagai contoh, misal kita punya aplikasi yang memerlukan mongodb sebagai database (disimpan dalam file mongo.yaml), nginx sebagai web server(webapp.yaml), mongo-secret.yaml untuk menyimopan kredensial, dan mongo-config.yaml untuk menyimpan configurasi. Maka untuk mendeploynya kita perlu command-command berikut:
```
kubectl apply -f webapp.yaml
kubectl apply -f mongo.yaml
kubectl apply -f mongo-config.yaml
kubectl apply -f mongo-secret.yaml
```

## Contoh Project

Kali ini, kita akan mencoba mendeploy nginx menggunakan kubernetes.

Pertama, jalankan minikube
```
minikube start
```
Jalankan command berikut untuk memastikan bahwa minikube sudah menjadi nodes
```
kubectl get nodes
```
Output yang benar adalah
```
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   14h   v1.30.0
```
Setelah minikube berhasil dijalankan, buatlah file dengan nama `nginx.yaml` yang berisi

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      nodePort: 30080
```
Ketika code tersebut dijalankan, maka nginx akan dideploy dengan nama nginx-deployment, dan replica yang dibuat adalah tiga. Nginx yang dideploy diambil dari container/image: nginx:1.14.2

Selain itu, akan ada service yang dibuat juga dengan nama nginx-service, di mana ini adalah external service type NodePort yang menggunakan `nodePort: 30080`

Ketika nginx berhasil dideploy, maka nginx akan dapat diakses melalui url `<minikube-ip>:<nodePort>`

Langkah selanjutnya, adalah menjalankan command kubectl apply
```
kubectl apply -f nginx.yaml
```
Outputnya akan seperti ini
```
deployment.apps/nginx-deployment created
service/nginx-service created
```
Untuk melihat pods yang berhasil dibuat, jalankan command berikut
```
kubectl get pods
```
Output akan menampilkan seluruh pods yang ada seperti ini
```
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-77d8468669-4cplg   1/1     Running   0          61s
nginx-deployment-77d8468669-czbsp   1/1     Running   0          61s
nginx-deployment-77d8468669-sdbjx   1/1     Running   0          61s
```
Untuk melihat deployment yang dilakukan, jalankan command
```
kubectl get deployments
```
Output akan menampilkan seluruh deployment seperti ini
```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   3/3     3            3           11m
```
Untuk melihat service yang ada, jalankan command
```
kubectl get svc 
```
Output akan menampilan service yang tersedia seperti ini
```
NAME            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes      ClusterIP   10.96.0.1       <none>        443/TCP        14h
nginx-service   NodePort    10.109.223.72   <none>        80:30080/TCP   12m
```
Kita juga dapat melihat semuanya sekaligus menggunakan command
```
kubectl get all
```
Outputnya akan memunculkan seperti berikut
```
NAME                                    READY   STATUS    RESTARTS   AGE
pod/nginx-deployment-77d8468669-4cplg   1/1     Running   0          16m
pod/nginx-deployment-77d8468669-czbsp   1/1     Running   0          16m
pod/nginx-deployment-77d8468669-sdbjx   1/1     Running   0          16m

NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes      ClusterIP   10.96.0.1       <none>        443/TCP        14h
service/nginx-service   NodePort    10.109.223.72   <none>        80:30080/TCP   16m

NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/nginx-deployment   3/3     3            3           16m

NAME                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/nginx-deployment-77d8468669   3         3         3       16m
```
Setelah memastikan semuanya sudah ada dan berjalan dengan lancar, kita coba mengakses url untuk memastikan apakah nginx sudah berhasil dideploy

Karena kita menggunakan external service NodePort, maka url akan diakses melalui `<minikube-ip>:<nodeport>`

Jalankan command `minikube ip` untuk mendapatkan alamat IP minikube. Selain itu kita juga dapat menjalankan command `kubectl get nodes -o wide` dan mendapatkan ip nya dari kolom INTERNAL-IP

nodePort dapat dilihat pada service, 
```
NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/nginx-service   NodePort    10.109.223.72   <none>        80:30080/TCP   16m
```
maka nodePort nya adalah 30080

Url akan mengarahkan ke halaman website yang menampilkan **Welcome to nginx!**

Note:

| **Known issue - Minikube IP not accessible**

Jika kalian tidak bisa mengakses url tersebut, coba jalankan command berikut:
```
minikube service nginx-service
```
