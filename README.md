# Confluent Kafka using Docker
Ingesting data into local directory as a flat files (.CSV) in confluent Kafka.
## Setup 
1. Run the Kafka cluster (with the docker via command prompt with this command, `docker compose up`.
2. Access the Confluent Control Center via the image port in Docker or go to this link http://localhost:9021.
   ![Screenshot (637)](https://user-images.githubusercontent.com/124119569/228171240-fcd49db2-dadb-4aa6-8bf3-4ea3ba16fff6.png)
3. Run Kafka producer to build the Kafka producer. (I already upload the Kafka producer in this repo (**user and email.py**)).
4. Run Kafka consumer to build the Kafka consumer. (I already upload the Kafka consumer in this repo (**student_consumer.py**)).
5. Here you can see the consumer (python_consumer) and topic (students) has been added,
   ![Screenshot (638)](https://user-images.githubusercontent.com/124119569/228173650-57347970-4bf5-4879-8c71-c46ba8bf321d.png)
   ![Screenshot (639)](https://user-images.githubusercontent.com/124119569/228173682-2e19d992-eb96-48ee-b3cf-090d065cd773.png)
   ![Screenshot (640)](https://user-images.githubusercontent.com/124119569/228173697-2cd6407e-b5ed-4bbe-92f2-3b004928902b.png)
6. You can see the ingested .CSV file in this repo (**Users.csv**).
