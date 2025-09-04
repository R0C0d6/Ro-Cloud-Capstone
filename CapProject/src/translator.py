import boto3
import json
import os

s3_client = boto3.client('s3')
translate_client = boto3.client('translate')

def lambda_handler(event, context):
    # Get the bucket and key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Get the file from S3
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        file_content = response['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
    except Exception as e:
        print(f"Error getting or parsing file: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps('Error processing input file.')
        }

    # Get text and target language from the JSON file
    text_to_translate = json_content.get('text')
    target_language = json_content.get('target_language')

    if not text_to_translate or not target_language:
        print("Missing 'text' or 'target_language' in the input JSON.")
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid input format.')
        }

    # Translate the text
    try:
        translation_response = translate_client.translate_text(
            Text=text_to_translate,
            SourceLanguageCode='auto',
            TargetLanguageCode=target_language
        )
        translated_text = translation_response['TranslatedText']
    except Exception as e:
        print(f"Error calling translate: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error during translation.')
        }


    # Prepare the output JSON
    output_json = {
        'original_text': text_to_translate,
        'translated_text': translated_text,
        'target_language': target_language
    }

    # Get the output bucket name from environment variables
    output_bucket_name = os.environ['OUTPUT_BUCKET']
    output_object_key = f"translated-{os.path.basename(object_key)}"

    # Upload the translated file to the output bucket
    try:
        s3_client.put_object(
            Bucket=output_bucket_name,
            Key=output_object_key,
            Body=json.dumps(output_json, ensure_ascii=False, indent=2),
            ContentType='application/json'
        )
    except Exception as e:
        print(f"Error uploading to output bucket: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error saving translated file.')
        }

    return {
        'statusCode': 200,
        'body': json.dumps('Translation successful!')
    }
