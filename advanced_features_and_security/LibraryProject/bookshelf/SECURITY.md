# SECURITY NOTES:
# - DEBUG = False disables Django error pages in production.
# - SECURE_CONTENT_TYPE_NOSNIFF prevents MIME sniffing.
# - X_FRAME_OPTIONS avoids clickjacking attacks.
# - CSRF_COOKIE_SECURE + SESSION_COOKIE_SECURE ensure cookies sent over HTTPS.
# - ORM queries prevent SQL injection by parameterizing inputs.
# - CSRF tokens protect POST forms from unauthorized requests.
# - CSP headers prevent malicious external scripts from loading.
