## Deploy ingress
kubectl apply -f ingress.yaml

## Deploy service
kubecl apply -f service.yaml

## Deploy hpa
kubectl apply f hpa.yaml

## Deploy configmap and secrets
kubectl apply -f configmap.yaml
kubectl apply -f secrets.yaml