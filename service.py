apiVersion: v1
kind: Service
metadata:
  annotations:
  labels:
    service: ns-18
    tier: backend
  name: ns-18
  namespace: ns-18
  resourceVersion: 
  selfLink: 
  uid: 
spec:
  clusterIP: 10.98.218.108
  ports:
  - name: service
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: service
    service: ns-18
  sessionAffinity: None
  type: ClusterIP
status:
  loadBalancer: {}
