# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACe8e7ad993f9bbc521e6c4d554d1f29b9"
auth_token = "8078c3e20c3dba9d9e94ecf2e7e28662"
verify_sid = "VA8246b23d5a251354739dd65515ba7c22"
verified_number = "+9779827189040"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid).verifications.create(
    to=verified_number, channel="sms"
)
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid).verification_checks.create(
    to=verified_number, code=otp_code
)
print(verification_check.status)
