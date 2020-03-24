import boto3
from botocore.client import Config
import zipfile
import io
import mimetypes

def lambda_handler(event, context):
    #sns = boto3.resource('sns')
    #topic = sns.Topic('arn:aws:sns:ap-south-1:319981697737:buildPortfolioTopic')
    loation ={
        "bucketName" : 'portfoliobuild.bhargavamacha.info',
        "objectKey" : 'portfolio.zip'
    }
    job = event.get("CodePipeline.job")
    if job:
        for artifact in job['data']['inputArtifacts']:
            if artifact['name'] == 'MyAppBuild':
                location = artifact['location']['s3Location']

    s3 = boto3.resource("s3", config = Config(signature_version = 's3v4'))
    portfolio_bucket = s3.Bucket('portfolio.bhargavamacha.info')
    build_bucket = s3.Bucket("portfoliobuild.bhargavamacha.info")
    
    portfolio_zip = io.BytesIO()

    build_bucket.download_fileobj('portfolio.zip', portfolio_zip)
    
    with zipfile.ZipFile(portfolio_zip) as myzip:
        for nm in myzip.namelist():
            obj = myzip.open(nm)
            portfolio_bucket.upload_fileobj(obj,nm,ExtraArgs = {'ContentType': mimetypes.guess_type(nm)[0]})
            portfolio_bucket.Object(nm).Acl().put(ACL = 'public-read')
   #sns.Topic('arn:aws:sns:ap-south-1:319981697737:buildPortfolioTopic').publish(Subject = "Portfolio Deployed", Message = "Portfolio Deployed successfully!")
    if job:
       codepipeline  = boto3.client('codepipeline')
       codepipeline.put_job_success_result(jobId = job['id'])
    return 'lambda function executed!:)'
