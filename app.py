from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sai2010**'

@app.route('/auth/<token>')
def authenticate(token):
    if token.strip() != "":
        return "Authentication successful"
    else:
        return "Invalid token"

@app.route('/')
def google():
    return '''<head><meta name="google-site-verification" content="jwjHQ5CVGwwCNeZTGmcRlrQWnlCasUvsrz6LKVN9khw" />
            </head><body>BOOST.IO</body>'''

@app.route('/privacy-policy/')
def policy():
    return """
    <!DOCTYPE html>
<html>

<head>
    <title>Privacy Policy for Boost</title>
</head>

<body style="font-family: Arial, sans-serif; margin: 20px;">
    <h1 style="text-align: center;">Privacy Policy for Boost</h1>

    <p>At Boost, we are committed to protecting the privacy and security of your personal information. This Privacy Policy outlines how we collect, use, disclose, and safeguard your information when you use our services. By accessing or using Boost, you consent to the terms outlined in this Privacy Policy.</p>

    <div style="font-size: 18px; font-weight: bold; margin-top: 20px;">1. Information We Collect</div>
    <p>Personal Information: We may collect personal information such as your name, email address, contact details, and any other information you voluntarily provide to us.</p>
    <p>Usage Information: We may collect information about your Youtube channel</p>
    <p>Cookies and Similar Technologies: We use cookies and similar technologies to enhance your experience, gather information about usage patterns, and track website analytics.</p>

    <div style="font-size: 18px; font-weight: bold; margin-top: 20px;">2. How We Use Your Information</div>
    <p>Provide and Improve Services: We use your information to provide, maintain, and improve our services, customize your experience, and respond to your inquiries or requests.</p>
    <p>Communication: We may use your contact information to send you updates, newsletters, promotional materials, and other communications related to Boost. You can opt-out of these communications at any time.</p>
    <p>Analytics and Aggregated Data: We may use anonymized and aggregated data for research, analytics, and reporting purposes.</p>

    <div style="font-size: 18px; font-weight: bold; margin-top: 20px;">3. How We Share Your Information</div>
    <p>Service Providers: We may share your information with trusted third-party service providers who assist us in delivering our services, such as hosting providers or analytics tools.</p>
    <p>Legal Requirements: We may disclose your information if required by law, regulation, legal process, or governmental request.</p>
    <p>Business Transfers: In the event of a merger, acquisition, or sale of assets, your information may be transferred as part of the transaction. We will notify you of any such change and provide options regarding your information.</p>

    <div style="font-size: 18px; font-weight: bold; margin-top: 20px;">4. Data Security</div>
    <p>We implement industry-standard security measures to protect your information from unauthorized access, disclosure, or alteration.</p>
    <p>However, no method of transmission over the internet or electronic storage is 100% secure. While we strive to protect your information, we cannot guarantee its absolute security.</p>

    <div style="font-size: 18px; font-weight: bold; margin-top: 20px;">5. Children's Privacy</div>
    <p>Boost is not intended for individuals under the age of 13. We do not knowingly collect or solicit personal information from children. If you believe we have inadvertently collected personal information from a child, please contact us immediately.</p>

    <div style="font-size: 18px; font-weight: bold; margin-top: 20px;">6. Your Choices and Rights</div>
    <p>You have the right to access, update, or delete your personal information. You can do so by contacting us directly.</p>
    <p>You can opt-out of receiving promotional communications from us by following the unsubscribe instructions provided in the communication or by contacting us.</p>

    <div style="font-size: 18px; font-weight: bold; margin-top: 20px;">7. Changes to this Privacy Policy</div>
    <p>We reserve the right to update or modify this Privacy Policy at any time. The revised policy will be effective upon posting on our website. We encourage you to review this Privacy Policy periodically.</p>

    <div style="font-size: 18px; font-weight: bold; margin-top: 20px;">8. Contact Us</div>
    <p>If you have any questions or concerns regarding this Privacy Policy or our data practices, please contact us at codingprojects2018@gmail.com.</p>

    <p style="font-style: italic; margin-top: 20px;">Please note that this Privacy Policy applies only to Boost and not to any third-party websites or services linked to or integrated with Boost. We encourage you to review the privacy policies of those third-party platforms.</p>

    <p style="font-weight: bold;">By using Boost, you signify your acceptance of this Privacy Policy.</p>
</body>

</html>

    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
