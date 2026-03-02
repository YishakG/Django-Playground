# 🔥 JWT — What You Must Never Forget

## 1️⃣ JWT Is Stateless

- Server does NOT store sessions.
- All authentication data is inside the token.
- Every request carries its own authentication proof.
- Scales easily across multiple servers.
  Stateless ≠ secure by default. It just means no server-side session storage.

## 2️⃣ JWT Structure

header.payload.signature

- Header → algorithm
- Payload → user_id, exp, type
- Signature → prevents tampering
  JWT is **signed**, not encrypted.
  Anyone can decode payload.
  Security comes from signature verification.

## 3️⃣ Access Token vs Refresh Token

### Access Token

- Short lived (5–15 min)
- Sent with every protected request
- If stolen → limited damage window

### Refresh Token

- Long lived (days)
- Used ONLY to generate new access tokens
- If stolen → attacker can stay logged in
  Refresh = master key
  Access = temporary key

## 4️⃣ Token Storage (Flutter Side)

❌ Never:

- SharedPreferences
- Plain storage
  ✅ Always:
- `flutter_secure_storage`
- OS-level encryption (Keystore / Keychain)
  If you store tokens badly, your whole system is garbage.

## 5️⃣ Expiration Flow

When access token expires:

1. Backend returns 401
2. Frontend calls refresh endpoint
3. Stores new access token
4. Retries original request
5. If refresh fails → logout
   If you don’t automate this, your UX will be broken.

## 6️⃣ Logout in JWT

JWT is stateless → server doesn’t store access tokens.
So logout means:

- Blacklist refresh token
- Let access token expire naturally
  Session auth = delete session
  JWT = invalidate refresh
  Very different model.

## 7️⃣ Attack Scenarios

### If Access Token Is Stolen

- Attacker can use it until it expires
- Cannot generate new tokens
- Damage window = remaining lifetime
  Mitigation:
- Short lifetime
- HTTPS
- Re-auth for sensitive actions

### If Refresh Token Is Stolen

- Attacker can generate new access tokens
- Until refresh expires
  This is serious.
  Mitigation:
- Rotation enabled
- Blacklist after rotation
- Secure storage

## 8️⃣ Secure Production Setup (SimpleJWT)

Minimum serious configuration:
ROTATE_REFRESH_TOKENS = True
BLACKLIST_AFTER_ROTATION = True
ACCESS_TOKEN_LIFETIME = 5 minutes
REFRESH_TOKEN_LIFETIME = 7 days
Anything less is beginner-level security.
