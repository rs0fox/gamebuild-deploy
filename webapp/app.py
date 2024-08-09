from flask import Flask, render_template, request, redirect, url_for
import boto3

app = Flask(__name__)

# Replace with your actual S3 bucket and region
S3_BUCKET = "builddb"
S3_REGION = "ap-south-1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Add logic to verify user credentials
        return redirect(url_for('download'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST'):
        # Add logic to register a new user
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/download')
def download():
    s3_client = boto3.client('s3', region_name=S3_REGION)
    url = s3_client.generate_presigned_url('get_object',
                                           Params={'Bucket': S3_BUCKET, 'Key': 'tictactoe-executable.exe'},
                                           ExpiresIn=3600)
    return redirect(url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
