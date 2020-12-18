Deployment Guide:

Pre-Requisites: 
1. Setup Python3 environment
2. Install required py libraries using below command
   - pip install -r requirement.txt
3. Port 5000 should be accessible, as this app runs on it.
4. The Application uses Postgresql as the Datastore. Modify the connection string in dboperations.py accordingly.
5. userProfiles.sql files is placed under UserManagement/DB/, which can be used to create the initial DB table.


Application Launch Steps: 
1. Checkout the repository. 
2. cd python/UserManagement/Backend/
3. Run the Application by using the below command 
   - python3 usermanage.py
4. Once the application is fully up and running, use postman client to access the endpoints. 
   - The Postman collection resides at /Postman/userManagement.postman_collection.json
