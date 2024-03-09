import io
import os
import boto3
import csv
from shareplum import Office365
from shareplum.site import Version
from shareplum import Site

# AWS credentials and region
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
eu_north_1 = 'eu-north-1'

# SharePoint credentials and site URL
# sharepoint_username = 'move_to_secret'
# sharepoint_password = 'move_to_secret'
# sharepoint_site_url = 'https://valid8me.sharepoint.com/'
# sharepoint_folder_path = 'alid8Me-Technology/EsUeqTOj09NMg0aAixcOTNYBBuBeqeYuh13uN9xrf_R-ew?e=iJxFOM'

# Initialize AWS SSM client
ssm_client_ew1 = boto3.client('ssm', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=eu_north_1)
# ssm_client_ew3 = boto3.client('ssm', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=eu_west_3)

# Fetch parameters from AWS Parameter Store by prefix
def fetch_parameters_from_ew1_by_prefix(prefix):
    parameters = {}
    response_ew1 = ssm_client_ew1.get_parameters_by_path(
        Path='/',
        Recursive=True,
        WithDecryption=True,
        ParameterFilters=[
            {
                'Key': 'Name',
                'Option': 'BeginsWith',
                'Values': [prefix]
            }
        ]
    )
    for param in response_ew1['Parameters']:
        parameters[param['Name']] = param['Value']
    return parameters

# def fetch_parameters_from_ew3_by_prefix(prefix):
#     parameters = {}
#     response_ew3 = ssm_client_ew3.get_parameters_by_path(
#         Path='/',
#         Recursive=True,
#         WithDecryption=True,
#         ParameterFilters=[
#             {
#                 'Key': 'Name',
#                 'Option': 'BeginsWith',
#                 'Values': [prefix]
#             }
#         ]
#     )
#     for param in response_ew3['Parameters']:
#         parameters[param['Name']] = param['Value']
#     return parameters

# Connect to SharePoint site
# def connect_to_sharepoint():
#     authcookie = Office365(sharepoint_site_url, username=sharepoint_username, password=sharepoint_password).GetCookies()
#     site = Site(sharepoint_site_url, version=Version.v365, authcookie=authcookie)
#     return site

# Upload parameters to SharePoint
# def upload_parameters_to_sharepoint(parameters, region_name):
#     site = connect_to_sharepoint()
#     folder = site.Folder(sharepoint_folder_path)
    
#     # Prepare CSV data in memory
#     csv_data = io.StringIO()
#     file_name = f"{region_name}_parameters.csv"
#     fieldnames = ['name', 'value', 'region']
#     writer = csv.DictWriter(csv_data, fieldnames=fieldnames)
#     writer.writeheader()
#     for key, value in parameters.items():
#         writer.writerow({'name': key, 'value': value, 'region': region_name})
    
#     # Write CSV data to SharePoint
#     folder.upload_file(io.BytesIO(csv_data.getvalue().encode()), file_name)

if __name__ == "__main__":
    prefix = 'V8'
    parameters = fetch_parameters_from_ew1_by_prefix(prefix)
    print(parameters)
    # upload_parameters_to_sharepoint(parameters, eu_west_1)
    # parameters_ew3 = fetch_parameters_from_ew3_by_prefix(prefix)
    # upload_parameters_to_sharepoint(parameters, eu_west_3)
