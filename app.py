from flask import Flask, request, jsonify
    import boto3
    import os

    app = Flask(__name__)

    s3 = boto3.client('s3')
    sns = boto3.client('sns')

    S3_BUCKET = "cicd1" 
    SNS_TOPIC = "arn:aws:sns:us-east-1:752423230467:image-upload" 

    @app.route('/upload', methods=['POST'])
    def upload_photo():
        if 'photo' not in request.files:
            return jsonify({'error': 'No photo!'}, 400)

        photo = request.files['photo']
        try:
            s3.upload_fileobj(photo, S3_BUCKET, photo.filename)
            sns.publish(
                TopicArn=SNS_TOPIC,
                Message=f'Photo {photo.filename} is in the box!'
            )
            return jsonify({'message': 'Photo uploaded!'}, 200)
        except Exception as e:
            print(e)
            return jsonify({'error': 'Oops!'}, 500)

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)
