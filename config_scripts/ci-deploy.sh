#! /bin/bash
# exit script when any command ran here returns with non-zero exit code
set -e

COMMIT_SHA1=$CIRCLE_SHA1

# We must export it so it's available for envsubst
export COMMIT_SHA1=$COMMIT_SHA1

# since the only way for envsubst to work on files is using input/output redirection,
#  it's not possible to do in-place substitution, so we need to save the output to another file
#  and overwrite the original with that one.
envsubst <./k8s/deployment.yml >./k8s/deployment.yml.out
mv ./k8s/deployment.yml.out ./k8s/deployment.yml

echo "$KUBERNETES_CLUSTER_CERTIFICATE" | base64 --decode > cert.crt
./kubectl --insecure-skip-tls-verify --kubeconfig="/dev/null" --server=$KUBERNETES_SERVER --token=$KUBERNETES_TOKEN

# ./kubectl \
#   --kubeconfig=/dev/null \
#   --insecure-skip-tls-verify 
#   --server=$KUBERNETES_SERVER \
#   --certificate-authority=cert.crt \
#   --token=$KUBERNETES_TOKEN \
#   apply -f ./k8s/ -n resourceideaapi