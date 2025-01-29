# Orgbook Publisher UI

## Administrative tasks

An admin can login with a tenant id + api key from the publisher's traction tenant.

### Issuer onboarding
Once logged in, new issuers can be registered by providing a scope and a name. These values will be mapped to the namespace and identifier portion of the resulting did:
`did:web:example.com:namespace:identifier`

The did will be create and promoted to `pending` state until this issuer is approaved in the related trust registry (typically done through a gh PR, currently the digital trust toolkit). At this point, the state will change from `pending` to `active`.

### Auth Credential Issuance

An admin can offer an auth credential for any `active` issuer, by providing a bc gov employee email. This will generate a short-url which the bc wallet can consume.

Currently this link needs to be transformed to a qr code and sent to the user out of band.