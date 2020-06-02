#### download configurtion file

#### kubectl --kubeconfig /home/scott/Documents/k8s-resourceideaapi-kubeconfig.yaml get pods

#### mkdir -p ~/.kube
#### cp /home/scott/Documents/k8s-resourceideaapi-kubeconfig.yaml ~/.kube/config
#### kubectl get pods
#### kubect get nodes

#### kubectl apply -f k8s/namespace.yml
#### kubectl get namespace

#### kubectl apply -f k8s/service-account.yml -n resourceideaapi
#### kubectl get secret -n resourceideaapi
-----
#### TOKEN=$(kubectl get secret -n resourceideaapi $(kubectl get secret -n resourceideaapi | grep cicd-token | awk '{print $1}') -o jsonpath='{.data.token}' | base64 --decode)
----- 
#### kubectl --insecure-skip-tls-verify --kubeconfig="/dev/null" --server=https://1388d674-433c-4da7-8ca0-8fd9c3a54886.k8s.ondigitalocean.com --token=$TOKEN get pods -n resourceideaapi
----- should return error

#### kubectl apply -f k8s/role.yml
#### kubectl apply -f k8s/role-binding.yml

##### kubectl --insecure-skip-tls-verify --kubeconfig="/dev/null" --server=https://1388d674-433c-4da7-8ca0-8fd9c3a54886.k8s.ondigitalocean.com --token=$TOKEN get pods -n resourceideaapi
---- should now work

## tag and push image to dockerhub

#### docker tag img dockerhub-id/img
#### docker login
#### docker push dockerhub-id/img

## manage workloads with k8s manifest files

#### kubectl apply -f k8s/deployment.yml
#### kubectl apply -f k8s/service.yml
#### kubectl get svc -n resourceideaapi