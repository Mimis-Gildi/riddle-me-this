#!/usr/bin/env zsh
# Create OpenSSL config to skip CRL checks
cat > /tmp/openssl.cnf <<EOF
openssl_conf = openssl_init

[openssl_init]
ssl_conf = ssl_sect

[ssl_sect]
system_default = system_default_sect

[system_default_sect]
Options = UnsafeLegacyRenegotiation
CipherString = DEFAULT@SECLEVEL=1
EOF

export OPENSSL_CONF=/tmp/openssl.cnf
# shellcheck disable=SC2155
export SSL_CERT_FILE=$(brew --prefix)/etc/openssl@3/cert.pem
# Test
ruby -rnet/http -e "Net::HTTP.get(URI('https://rubygems.org'))"
# If that works:
bundle exec jekyll serve -wolIVt