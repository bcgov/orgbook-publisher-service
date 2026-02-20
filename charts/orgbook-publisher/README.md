# orgbook-publisher

![Version: 0.0.4](https://img.shields.io/badge/Version-0.0.4-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.0.5](https://img.shields.io/badge/AppVersion-0.0.5-informational?style=flat-square)

An api server to register and manage credentials.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.bitnami.com/bitnami | common | 2.x.x |
| oci://registry-1.docker.io/cloudpirates | mongodb | 0.10.3 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| backend.containerSecurityContext | object | `{}` | Security context for backend containers |
| backend.image.pullPolicy | string | `"IfNotPresent"` | Backend image pull policy |
| backend.image.pullSecrets | list | `[]` | Backend image pull secrets |
| backend.image.repository | string | `"ghcr.io/bcgov/orgbook-publisher-service"` | Backend image repository |
| backend.image.tag | string | `"v0.0.2"` | Backend image tag |
| backend.networkPolicy.ingress.podSelector | object | `{}` | Pod selector for backend ingress network policy |
| backend.podAnnotations | object | `{}` | Annotations for backend pods |
| backend.podSecurityContext | object | `{}` | Security context for backend pods |
| backend.replicaCount | int | `1` | Number of backend replicas |
| backend.resources.limits.cpu | string | `"100m"` | CPU limit for backend |
| backend.resources.limits.memory | string | `"512Mi"` | Memory limit for backend |
| backend.resources.requests.cpu | string | `"10m"` | CPU request for backend |
| backend.resources.requests.memory | string | `"128Mi"` | Memory request for backend |
| backend.service.apiPort | int | `8000` | Backend API container port |
| backend.service.servicePort | int | `8000` | Backend service port |
| backend.service.type | string | `"ClusterIP"` | Backend service type |
| database.existingSecret | string | `""` | Use an existing secret for MongoDB credentials (bypasses chart-managed secret creation) |
| externalMongodb.auth.enabled | bool | `true` | Enable authentication for external MongoDB |
| externalMongodb.auth.existingSecret | string | `""` | Name of existing secret containing MongoDB password |
| externalMongodb.auth.existingSecretPasswordKey | string | `"mongodb-password"` | Key in the existing secret containing the MongoDB password |
| externalMongodb.auth.password | string | `""` | MongoDB password. Ignored if existingSecret is set. Use existingSecret for production deployments. |
| externalMongodb.auth.username | string | `"orgbook-publisher"` | MongoDB username |
| externalMongodb.database | string | `"orgbook-publisher"` | Database name to use |
| externalMongodb.host | string | `""` | External MongoDB host (e.g., "mongodb.example.com"). Required when mongodb is disabled. |
| externalMongodb.port | int | `27017` | External MongoDB port |
| fullnameOverride | string | `"orgbook-publisher"` | String to fully override the chart name |
| ingress.annotations | list | `[]` | Annotations for the ingress |
| ingress.labels | list | `[]` | Labels for the ingress |
| ingress.tls | list | `[]` | TLS configuration for the ingress |
| mongodb.auth.enabled | bool | `true` | Enable MongoDB authentication |
| mongodb.auth.existingSecret | string | `"{{ printf \"%s-mongodb\" .Release.Name }}"` | Existing secret with MongoDB credentials (key: `mongodb-root-password`) |
| mongodb.auth.rootUsername | string | `"admin"` | MongoDB root username |
| mongodb.commonLabels | object | `{ app.kubernetes.io/role: database }` | Labels added to all MongoDB resources |
| mongodb.containerSecurityContext | object | `{}` | Set MongoDB container security context |
| mongodb.customUser.database | string | `"orgbook-publisher"` | Name of the MongoDB database |
| mongodb.customUser.existingSecret | string | `"{{ printf \"%s-mongodb\" .Release.Name }}"` | Existing secret containing custom user credentials |
| mongodb.customUser.name | string | `"orgbook-publisher"` | Name of the custom MongoDB user |
| mongodb.customUser.secretKeys.database | string | `"mongodb-database"` | Key name for database in existing secret |
| mongodb.customUser.secretKeys.name | string | `"mongodb-user"` | Key name for username in existing secret |
| mongodb.customUser.secretKeys.password | string | `"mongodb-password"` | Key name for password in existing secret |
| mongodb.enabled | bool | `true` | Enable bundled MongoDB subchart. Set to false when using externalMongodb. |
| mongodb.image.pullPolicy | string | `"IfNotPresent"` | MongoDB image pull policy |
| mongodb.image.registry | string | `"docker.io"` | MongoDB image registry |
| mongodb.image.repository | string | `"mongo"` | MongoDB image repository |
| mongodb.image.tag | string | `"8.0"` | MongoDB image tag |
| mongodb.persistence.enabled | bool | `true` | Enable MongoDB data persistence using PVC |
| mongodb.persistence.size | string | `"8Gi"` | PVC Storage size for MongoDB data volume |
| mongodb.persistence.storageClass | string | `""` | PVC Storage Class for MongoDB data volume |
| mongodb.podLabels | object | `{ app.kubernetes.io/role: database }` | Labels added to MongoDB pods (used by network policy) |
| mongodb.podSecurityContext | object | `{}` | Set MongoDB pod security context |
| mongodb.replicaSet.enabled | bool | `false` | Enable MongoDB replica set mode (standalone if false) |
| mongodb.service.port | int | `27017` | MongoDB service port |
| mongodb.service.type | string | `"ClusterIP"` | MongoDB service type |
| mongodb.targetPlatform | string | `""` | Target platform for MongoDB deployment. Set to "openshift" for OpenShift compatibility, leave empty for standard Kubernetes. |
| nameOverride | string | `"orgbook-publisher"` | String to partially override the chart name |
| networkPolicy.ingress.namespaceSelector | list | `[]` | Namespace selector for ingress network policy |
| selectorLabels | object | `{}` | Additional selector labels applied to all resources |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)
