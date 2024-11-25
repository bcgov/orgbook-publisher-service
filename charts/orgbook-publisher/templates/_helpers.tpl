{{- define "global.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "global.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{- define "global.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "common.labels" -}}
app: {{ include "global.name" . }}
helm.sh/chart: {{ include "global.chart" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
{{- end }}

{{- define "common.selectorLabels" -}}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}


{{/*
Returns a secret if it already in Kubernetes, otherwise it creates
it randomly.
*/}}
{{- define "getOrGeneratePass" }}
{{- $len := (default 16 .Length) | int -}}
{{- $obj := (lookup "v1" .Kind .Namespace .Name).data -}}
{{- if $obj }}
{{- index $obj .Key -}}
{{- else if (eq (lower .Kind) "secret") -}}
{{- randAlphaNum $len | b64enc -}}
{{- else -}}
{{- randAlphaNum $len -}}
{{- end -}}
{{- end }}


{{/* BACKEND */}}

{{- define "backend.fullname" -}}
{{ template "global.fullname" . }}
{{- end -}}

{{- define "backend.selectorLabels" -}}
app.kubernetes.io/name: {{ include "backend.fullname" . }}
{{ include "common.selectorLabels" . }}
{{- end -}}

{{- define "backend.labels" -}}
{{ include "common.labels" . }}
{{ include "backend.selectorLabels" . }}
{{- end -}}



{{/*
Returns a secret if it already in Kubernetes, otherwise it creates
it randomly.

Usage:
{{ include "getOrGeneratePass" (dict "Namespace" .Release.Namespace "Kind" "Secret" "Name" (include "vc-authn-oidc.databaseSecretName" .) "Key" "mongodb-root-password" "Length" 32) }}

*/}}
{{- define "getOrGeneratePass" }}
{{- $len := (default 16 .Length) | int -}}
{{- $obj := (lookup "v1" .Kind .Namespace .Name).data -}}
{{- if $obj }}
{{- index $obj .Key -}}
{{- else if (eq (lower .Kind) "secret") -}}
{{- randAlphaNum $len | b64enc -}}
{{- else -}}
{{- randAlphaNum $len -}}
{{- end -}}
{{- end }}

{{/*
Define the name of the database secret to use
*/}}
{{- define "orgbook-publisher.databaseSecretName" -}}
{{- if (empty .Values.database.existingSecret) -}}
{{- printf "%s-%s" .Release.Name "mongodb" | trunc 63 | trimSuffix "-" }}
{{- else -}}
{{- .Values.database.existingSecret -}}
{{- end -}}
{{- end }}

{{/*
Return true if a database secret should be created
*/}}
{{- define "orgbook-publisher.database.createSecret" -}}
{{- if not .Values.database.existingSecret -}}
{{- true -}}
{{- end -}}
{{- end -}}