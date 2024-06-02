import pyautogui
import time

# Wait for 2 seconds for you to put your mouse on the skills section
time.sleep(2)

# make an array for all the skills
skills = ["Java", "Python", "JavaScript", "TypeScript", "GoLang", "Kotlin", "Bash", "GraphQL", "HTML", "CSS", "MySQL", "MongoDB", "PostgreSQL", "ElasticSearch", "Neo4j", "Redis", "DynamoDB", "Cassandra", "Maven", "Spring", "Spring Boot", "Node.js", "Express.js", "React", "Angular", "PySpark", "Selenium", "Next.js", "Agile", "Test Driven Development", "BDD", "FDD", "Pair Programming", "SDLC", "UML", "Continuous Integration", "Continuous Delivery", "CI/CD", "Microservices", "gRPC", "Protocol Buffers", "Object Oriented Design Patterns", "Service Oriented Architecture", "Software Architecture", "Jenkins", "Postman", "RabbitMQ", "GIT", "Jira", "BootStrap", "MaterialUI", "Bitbucket", "Hadoop", "MapReduce", "AWS S3", "AWS EC2", "AWS Lambda", "AWS EMR", "AWS RDS", "AWS CloudFront", "Azure App Service", "Azure Container Registry", "Azure DevOps", "Spark", "Kafka", "Hive", "MATLAB", "Docker", "Kubernetes", "Azure Functions", "Azure Active Directory", "Google Cloud", "Firebase"]

for skill in skills:
    pyautogui.typewrite(skill)
    pyautogui.press("Enter")
    time.sleep(1)
    pyautogui.press("Space")
    pyautogui.press("up")