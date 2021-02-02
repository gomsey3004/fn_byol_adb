import io
import json
import logging
import oci
from fdk import response
signer = oci.auth.signers.get_resource_principals_signer()
db_client = oci.database.DatabaseClient(config={}, signer=signer)
def handler(ctx, data: io.BytesIO = None):
 try:
  body = json.loads(data.getvalue())
  resourceId= body["data"]["resourceId"]
  adb_instance = db_client.get_autonomous_database(autonomous_database_id=resourceId)
  instance = adb_instance.data
  adb_request = oci.database.models.UpdateAutonomousDatabaseDetails()
  adb_request.license_model = adb_request.LICENSE_MODEL_LICENSE_INCLUDED
  print(adb_request)
  db_response = db_client.update_autonomous_database(autonomous_database_id = instance.id, update_autonomous_database_details = adb_request)
 except (Exception, ValueError) as ex:
  logging.getLogger().info('error parsing json payload: ' + str(ex))
 logging.getLogger().info("Inside Python Hello World function")
 return response.Response(ctx, response_data=json.dumps({"message": "Hello"}),headers={"Content-Type": "application/json"})
