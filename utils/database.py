import mysql.connector
from mysql.connector import Error
import numpy as np
from PIL import Image
import os
import uuid


class DatabaseConnector:
    def __init__(self, host_name, user_name, user_password, db_name):
        self.connection = self.create_connection(host_name, user_name, user_password, db_name)

    def create_connection(self, host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection

    def execute_query(self, query, data):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, data)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
            
            
            
class SegmentedObjectSaver:
    def __init__(self, input_image_pil, segmented_output, output_dir, db_connector):
        self.input_image_pil = input_image_pil
        self.segmented_output = segmented_output
        self.output_dir = output_dir
        self.db_connector = db_connector
        self.master_id = str(uuid.uuid4())

        os.makedirs(self.output_dir, exist_ok=True)

    def save_segmented_objects(self):
        unique_labels = np.unique(self.segmented_output)
        
        for label in unique_labels:
            if label == 0:
                continue  # Skip background

            # Create a mask for the current label
            mask = self.segmented_output == label
            
            # Apply the mask to the original image
            object_image = np.array(self.input_image_pil) * np.stack([mask]*3, axis=-1)
            
            # Convert the masked image to a PIL image and save it
            object_image_pil = Image.fromarray(object_image.astype(np.uint8))
            object_path = os.path.join(self.output_dir, f'segmented_object_{label}.png')
            object_image_pil.save(object_path)
            
            # Generate a unique ID for the object
            object_id = str(uuid.uuid4())
            
            # SQL query to insert metadata
            query = """
            INSERT INTO objects_metadata (object_id, master_id, label, image_path) 
            VALUES (%s, %s, %s, %s)
            """
            data = (object_id, self.master_id, int(label), object_path)
            
            # Insert metadata into MySQL database
            self.db_connector.execute_query(query, data)            